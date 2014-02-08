<?php

/**************************************************************************************************
* auteur : Jean Tinguely Awais - pas de licence - pas de copyright - heureux de l'avoir écrit!
* but : créer un adapteur pour postgresql 
* contact : jeantinguelyawais@gmail.com - http://www.t-servi.com
* remarque  : retour d'erreur, plutôt -1 que FALSE et 0 que TRUE 
**************************************************************************************************/

/*Définition d'une interface iDbWrappers */
interface iDbWrappers
{
	public function dbExist();
	public function createTable($table,$fields,$constraint='');
	public function tableExist($table);
	public function dropTable($table);
	public function insert($table,$namesAndValues,$insertClause='');
	public function delete($table,$deleteClause='',$deleteNamesAndValues=array());
	public function select($table,$selectClause='',$selectNamesAndValues=array());
	public function update($table,$namesAndValues,$updateClause='',$updateNamesAndValues=array());
}

/*Définition d'une classe dbWrappers qui hérite de l'interface ci-dessus, classe "abstraite" */
class dbWrappers implements iDbWrappers
{
	/***********************************************************************************************
	* todo : 
	* fonction dump
	***********************************************************************************************/
	function dbWrappers(){ /* compatibilité php4 */ $this->__construct();}
	function __construct(){}
	public function dbExist(){}
	public function tableExist($table){}
	public function createTable($table,$fields,$constraint=''){}
	public function dropTable($table){}
	public function insert($table,$namesAndValues,$insertClause=''){}
	public function delete($table,$deleteClause='',$deleteNamesAndValues=array()){}
	public function select($table,$selectClause='',$selectNamesAndValues=array()){}
	public function update($table,$namesAndValues,$updateClause='',$updateNamesAndValues=array()){}
}

class pgsql extends dbWrappers
{
	var $host;
	var $dbname;
	var $user;
	var $pass;
	var $port;
	var $connected;
	
	function pgsql($host,$dbname,$user,$pass,$port='5432' )
	{
		/* compatibilité php4 */
		$this->__construct($host,$dbname,$user,$pass,$port);
	}
	
	function __construct($host,$dbname,$user,$pass,$port='5432' )
	{
		$this->connected=(int)0;
		$this->host=$host;
		$this->dbname=$dbname;
		$this->user=$user;
		$this->pass=$pass;
		$this->port=$port;
		$dbconn = pg_connect('host='.$host.' dbname='.$dbname.' user='.$user.' password='.$pass.' port='.$port.' ') or $this->connected=-1;
		pg_close($dbconn);
	}
	
	public function dbExist()
	{return $this->connected;}
	public function tableExist($table)
	{
		$ret=-1;
		if($this->connected>=0)
		{
			
				$select='SELECT * from '.$table.' ; ';
				$dbconn = pg_connect('host='.$this->host.' dbname='.$this->dbname.' user='.$this->user.' password='.$this->pass.' port='.$this->port.'  ') or $this->connected=-1;
				$result = pg_query($select);
				if (!$result)
					{$ret=-1;}
				else
					{$ret=0;} 
				pg_close($dbconn);
		}
		return $ret;
	}
	public function createTable($table,$fields,$constraint='')
	{
		$ret=-1;
		if($this->connected>=0)
		{
			$this->dropTable($table);
			$createTable='CREATE TABLE '.$table.' ( ';
			$index=0;
			foreach($fields as $k=>$v)
			{
				$createTable.=$k.' '.$v['type'];
				if(count($fields)>1 && $index<count($fields)-1)
				{$createTable.=' , ';}
				$index++;
			}
			$createTable.=$constraint.' ) ';
			//echo $createTable;
			$dbconn = pg_connect('host='.$this->host.' dbname='.$this->dbname.' user='.$this->user.' password='.$this->pass.' port='.$this->port.'  ') or $this->connected=-1;
			$result = pg_query($createTable) or $ret=-1;
			pg_close($dbconn);			
		}
		return $ret;
	}
	public function dropTable($table)
	{
		$ret=-1;
		if($this->connected>=0 && $this->tableExist($table)>=0)
		{
			$ret=0;
			$drop='DROP TABLE IF EXISTS '.$table;
			$dbconn = pg_connect('host='.$this->host.' dbname='.$this->dbname.' user='.$this->user.' password='.$this->pass.' port='.$this->port.'  ') or $this->connected=-1;
			$result=pg_query($drop) or $ret=-1;
			if(!$result)
				{$ret=-1;}
			pg_close($dbconn);			
		}
		return $ret;
	}
	public function insert($table,$namesAndValues,$insertClause='')
	{
		$ret=array();
		if($this->tableExist($table)>=0)
		{
			$insert='INSERT INTO '.$table.' ';
			$keys='';
			$values='';
			$index=0;
			foreach($namesAndValues as $k=>$v)
			{
				$keys.=$k; 
				$values.='\''.$v.'\' ';
				if(count($namesAndValues)>1 && $index<count($namesAndValues)-1)
				{
					$keys.=' , ';
					$values.=' , ';
				}
				$index++;
			}
			$insert.=' ( '.$keys.' ) VALUES ( '.$values.' ) '.$insertClause.' RETURNING * ';
			$dbconn = pg_connect('host='.$this->host.' dbname='.$this->dbname.' user='.$this->user.' password='.$this->pass.' port='.$this->port.'  ') or $this->connected=-1;
			$result = pg_query($insert);
			if (!$result)
				{}
			else
			{
				while ($row = pg_fetch_array($result)) 
					{array_push($ret,$row);}
			}
			pg_close($dbconn);
		}
		return $ret;
	}
	public function delete($table,$deleteClause='',$deleteNamesAndValues=array())
	{
		$ret=0;
		if($this->tableExist($table)>=0)
		{
			$delete='DELETE from '.$table.' ';
			if(count($deleteNamesAndValues)>0)
				{$delete.=' where ';}
			$index=0;
			foreach($deleteNamesAndValues as $k=>$v)
			{
					$delete.=' '.$k.'=\''.$v.'\' ';
					if($index<count($deleteNamesAndValues)-1)
						{$delete.=' and ';}
					$index++;	
			}
			$delete.=$deleteClause;
			$dbconn = pg_connect('host='.$this->host.' dbname='.$this->dbname.' user='.$this->user.' password='.$this->pass.' port='.$this->port.'  ') or $this->connected=-1;
			$result = pg_query($delete) or $ret=-1;
			pg_close($dbconn);
		}
		return $ret;
	}
	public function select($table,$selectClause='',$selectNamesAndValues=array())
	{
		$ret=array();
		if($this->tableExist($table)>=0)
		{
			$select='SELECT * from '.$table.' ';
			if(count($selectNamesAndValues)>0 || strlen($selectClause)>0 )
				{$select.=' where ';}
			$index=0;
			foreach($selectNamesAndValues as $k=>$v)
			{
					$select.=' '.$k.'=\''.$v.'\' ';
					if($index<count($selectNamesAndValues)-1)
						{$select.=' and ';}
					$index++;	
			}
			if(strlen($selectClause)>0)
				{$select.=$selectClause;}
			$dbconn = pg_connect('host='.$this->host.' dbname='.$this->dbname.' user='.$this->user.' password='.$this->pass.' port='.$this->port.'  ') or $this->connected=-1;
			$result = pg_query($select) or $ret=array();
			while ($row = pg_fetch_array($result)) 
				{array_push($ret,$row);}
			pg_close($dbconn);
		}
		return $ret;
	}
	public function update($table,$namesAndValues,$updateClause='',$updateNamesAndValues=array())
	{
		$ret=array();
		if($this->tableExist($table)>=0)
		{
			$update='UPDATE '.$table.' SET ';
			$index=0;
			foreach($namesAndValues as $k=>$v)
			{
				$update.=' '.$k.' = \''.$v.'\' ';
				if(count($namesAndValues)>1 && $index<count($namesAndValues)-1)
				{$update.=', ';}
				$index++;
			}
			$update.='   ';
			if(count($updateNamesAndValues)>0)
			{
				$update.=' WHERE ';
				$index=0;
				foreach($updateNamesAndValues as $k=>$v)
				{
					$update.=' '.$k.' = \''.$v.'\'';	
					if(count($updateNamesAndValues)>1 && $index<count($updateNamesAndValues)-1)
						{$update.=' AND ';}
					$index++;
				}
			}
			$update.=$updateClause;
			$update.=' RETURNING * ';
			$dbconn = pg_connect('host='.$this->host.' dbname='.$this->dbname.' user='.$this->user.' password='.$this->pass.' port='.$this->port.'  ') or $this->connected=-1;
			$result = pg_query($update);
			if(!$result)
				{}
			else
			{
				while ($row = pg_fetch_array($result)) 
					{array_push($ret,$row);}
					
			}		
			pg_close($dbconn);	
		}
		return $ret;
	}
}

?>
