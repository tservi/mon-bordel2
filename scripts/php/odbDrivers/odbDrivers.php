<?php

/*Définition des structures de base : l'objet */
$objectStructure=array(
	'objType'=>'text',
	'idContainer'=>'bigint',
	'hierarchy'=>'bigint',
	'state'=>'bigint',
	'properties'=>'text',
	'methods'=>'text'
	);

/*Définition des structures de base : le protocole */
$protocolStructure=array(
	'creationDate'=>'text',
	'creationTime'=>'text',
	'userId'=>'text',
	'operation'=>'text',
	'idBefore'=>'bigint',
	'idAfter'=>'bigint'
	);

/*Définition d'une interface objectDbDrivers */
interface objectDbDriver
{
	public function insert($namesAndValues);
	public function delete($oldId);
	public function select($namesAndValues);
	public function update($namesAndValues,$oldId);
	public function getFilliation($id);
}

/*Définition d'une classe odd qui hérite de l'interface ci-dessus */
class odd implements objectDbDriver
{
	function odd()
	{}
	public function insert($namesAndValues){}
	public function delete($oldId){}
	public function select($namesAndValues){}
	public function update($namesAndValues,$oldId){}
	public function getFilliation($id){}
}

/*Définition d'une classe postgresODD qui hérite de la classe odd */
class pgODD extends odd
{
	var $objectStructure;
	var $protocolStructure;
	var $host;
	var $dbname;
	var $user;
	var $pass;
	var $connected;

	function pgODD($host,$user,$pass,$database)
	{
		$standardname='objects';
		global $protocolStructure;
		global $objectStructure;
		$this->protocolStructure=$protocolStructure;
		$this->objectStructure=$objectStructure;
		$this->connected=false;
		$this->host=$host;
		$this->dbname=$standardname;
		$this->user=$user;
		$this->pass=$pass;
		$dbconn = pg_connect('host='.$host.' dbname='.$database.' user='.$user.' password='.$pass.' ') or die('Connexion impossible : ' . pg_last_error());
		$query = 'SELECT datname FROM pg_database;';
		$result = pg_query($query) or die('Échec requête : ' . pg_last_error());
		// test si il existe une base de donnée appelée objects (stocké dans $standardname)
		$isObjectDatabasePresent=false;
		while ($line = pg_fetch_array($result, null, PGSQL_ASSOC))
			{
				foreach ($line as $col_value)
					{if($col_value==$standardname) {$isObjectDatabasePresent=true;}}
			}
		pg_free_result($result);
		pg_close($dbconn);
		if($isObjectDatabasePresent)
		{
			/*echo "everything nice!!!";*/
			//vérifier si les tables nécessaires sont présentent
			$objectsBody='';
			foreach ($this->objectStructure as $k=>$v)
			  {$objectsBody.=$k.' '.$v.', ';}
			$protocolsBody='';
			foreach ($this->protocolStructure as $k=>$v)
			  {$protocolsBody.=$k.' '.$v.', ';}
			$tables=array(
			'objects'=>'create table objects ('.$objectsBody.' id bigserial NOT NULL, CONSTRAINT "idPrimaryKeyObjects" PRIMARY KEY (id) )  ',
			'protocols'=>'create table protocols ('.$protocolsBody.' id bigserial NOT NULL, CONSTRAINT "idPrimaryKeyProtocols" PRIMARY KEY (id) )'
			);
			$tablesExists=true;
			foreach($tables as $k => $v)
			{
				$thistableexists=true;
				$dbconn = pg_connect('host='.$host.' dbname='.$standardname.' user='.$user.' password='.$pass.' ') or $tablesExists=false;
				$query = 'SELECT * FROM '.$k.';';
				$result = pg_query($query) or  $thistableexists=false;
				pg_close($dbconn);
				if(!$thistableexists)
				{
					$dbconn = pg_connect('host='.$host.' dbname='.$standardname.' user='.$user.' password='.$pass.' ') or $tablesExists=false;
					$query = $v ;
					$result = pg_query($query) or  $thistableexists=false;
					pg_close($dbconn);
				}
				if(!$thistableexists)
				{$tablesExists=false;}
			}
			if($tablesExists)
			{
				$this->connected=true;
			}
			else
			{echo "Oups! You need to create the tables manually!!!<br/>".'\n';}
		}
		else
		{echo "Create one database called 'objects' in your DB!<br/>".'\n';}
	}

	private function insertObject($namesAndValues)
	{
		$ret=0;
		$dbconn = pg_connect('host='.$this->host.' dbname='.$this->dbname.' user='.$this->user.' password='.$this->pass.' ') or $ret=1; // pas de connection
		$query='INSERT INTO objects ( ';
		$cols=' ';
		$values=' ';
		$selectClause='SELECT id FROM objects where';
		foreach($namesAndValues as $k=>$v)
			{
				$cols.=$k.' ,';
				$values.='\''.$v.'\' ,';
				$selectClause.=' '.$k.'=\''.$v.'\' and';
			}
		$cols=substr($cols,0,strlen($cols)-1);
		$values=substr($values,0,strlen($values)-1);
		$selectClause=substr($selectClause,0,strlen($selectClause)-3);
		$selectClause.=' ORDER by id DESC ; ';
		$query.=$cols.') VALUES ('.$values.' ) ; ';
		//echo $query;
		$result = pg_query($query) or $ret=-2;  // erreur d'insertion;
		pg_close($dbconn);
		$dbconn = pg_connect('host='.$this->host.' dbname='.$this->dbname.' user='.$this->user.' password='.$this->pass.' ') or $ret=1; // pas de connection
		//echo $selectClause;
		$result = pg_query($selectClause) or $ret=-3;  // erreur de select;
        $row = pg_fetch_row($result);
		$ret=$row[0];
		return $ret;
	}

	private function insertProtocol($user,$action,$idBefore,$idAfter)
	{
		$ret=0
		pg_close($dbconn);
		$protocol='INSERT INTO protocols ( creationDate, creationTime, userId, operation, idBefore, idAfter ) VALUES ( ';
		$protocol.='\''.date("Ymd").'\', ';
		$protocol.='\''.date("H:i:s.u").'\', ';
		$protocol.='\''.$user.'\', ';
		$protocol.='\''.$action.'\', ';
		$protocol.='\''.$idBefore.'\', ';
		$protocol.='\''.$idAfter.'\' ';
		$protocol.=' ) ; ';
		$dbconn = pg_connect('host='.$this->host.' dbname='.$this->dbname.' user='.$this->user.' password='.$this->pass.' ') or $ret=1; // pas de connection
		pg_query($protocol) or $ret=-4;  // erreur d'insertion dans le protocol;
		pg_close($dbconn);
		return $ret
	}

	public function insert($namesAndValues)
	{

		$ret=0;
		/*
		$dbconn = pg_connect('host='.$this->host.' dbname='.$this->dbname.' user='.$this->user.' password='.$this->pass.' ') or $ret=1; // pas de connection
		$query='INSERT INTO objects ( ';
		$cols=' ';
		$values=' ';
		$selectClause='SELECT id FROM objects where';
		foreach($namesAndValues as $k=>$v)
			{
				$cols.=$k.' ,';
				$values.='\''.$v.'\' ,';
				$selectClause.=' '.$k.'=\''.$v.'\' and';
			}
		$cols=substr($cols,0,strlen($cols)-1);
		$values=substr($values,0,strlen($values)-1);
		$selectClause=substr($selectClause,0,strlen($selectClause)-3);
		$selectClause.=' ORDER by id DESC ; ';
		$query.=$cols.') VALUES ('.$values.' ) ; ';
		//echo $query;
		$result = pg_query($query) or $ret=2;  // erreur d'insertion;
		pg_close($dbconn);
		$dbconn = pg_connect('host='.$this->host.' dbname='.$this->dbname.' user='.$this->user.' password='.$this->pass.' ') or $ret=1; // pas de connection
		//echo $selectClause;
		$result = pg_query($selectClause) or $ret=3;  // erreur de select;
        $row = pg_fetch_row($result);
		$oId=$row[0];
		*/
		$oId=$this->insertObject($namesAndValues);
		//echo $oId;
		/*
		pg_close($dbconn);
		$protocol='INSERT INTO protocols ( creationDate, creationTime, userId, operation, idBefore, idAfter ) VALUES ( ';
		$protocol.='\''.date("Ymd").'\', ';
		$protocol.='\''.date("H:i:s.u").'\', ';
		$protocol.='\'pgODD\', ';
		$protocol.='\'insert\', ';
		$protocol.='\'0\', ';
		$protocol.='\''.$oId.'\' ';
		$protocol.=' ) ; ';
		$dbconn = pg_connect('host='.$this->host.' dbname='.$this->dbname.' user='.$this->user.' password='.$this->pass.' ') or $ret=1; // pas de connection
		pg_query($protocol) or $ret=4;  // erreur d'insertion dans le protocol;
		pg_close($dbconn);
		*/
		$ret=$this->insertProtocol('pgODD','insert','0',$oId);
		return $ret;
	}

	public function update($namesAndValues,$oldId)
	{
		$newObject=array();
		$ret=0;
		$dbconn = pg_connect('host='.$this->host.' dbname='.$this->dbname.' user='.$this->user.' password='.$this->pass.' ') or $ret=1; // pas de connection
		$select='SELECT * FROM objects where id=\''.$oldId.'\' ; ';
		$resultSelect = pg_query($select) or $ret=3;  // erreur de select;
		//print_r($this->objectStructure);
		$index=0;
		$row = pg_fetch_row($resultSelect);
		pg_close($dbconn);
		foreach ($this->objectStructure as $k=>$v)
		{
			$newObject[$k]=$row[$index];
			$index++;
		}
		//print_r($newObject);
		foreach($namesAndValues as $k=>$v)
			{$newObject[$k]=$v;}
		$oId=$this->insertObjet($newObject);
		$update='';
		$selectNew='';
		$insertProtocol='';
		return $ret;
	}
	public function delete($oldId){}
	public function select($namesAndValues){}
	public function getFilliation($id){}
}

$PGODD=new pgODD('localhost','jean','pass','postgres');
//echo $PGODD->connected;
$objectTest=array(
	'objType'=>'test',
	'idContainer'=>'0',
	'hierarchy'=>'0',
	'state'=>'0',
	'properties'=>'testupdate',
	'methods'=>'test'
	);
//echo $PGODD->insert($objectTest);
echo $PGODD->update($objectTest,'1');
?>