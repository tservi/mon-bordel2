<?php

/*
**********************************************************************************************************************************************
Auteur : Jean Tinguely Awais aka t-servi.com
- pas de licence - pas de copyright - heureux de l'avoir écrit -
But : faire un ensemble de classe permettant de créer et de savoir l'étât d'un verrou
**********************************************************************************************************************************************
*/

interface lockers
{
	public function keymaker($key='test');
	public function lock();
	public function unlock();
	public function status();
}

class dirLock implements lockers
{
	/* pose un repertoire vide comme verrou - ne fonctionne que sous certaines conditions! */

	var $key      ;
	var $out = '' ; /* variable qui stocke un éventuel résultat de retour de l'objet */

	function lockers($key='test')
	{
		/* compatibilité php4 */
		$this->__construct(($key));
	}

	function __construct($key='test')
		{$this->key = $this->keymaker($key);}

	public function keymaker($key='test')
		{return 'lockers/'.$key.'_locking';}

	public function lock()
	{
		$lock = $this->key;
		@mkdir($lock);
		$this->out = 'locking : '.$lock;
	}

	public function unlock()
	{
		$lock = $this->key;
		if(is_dir($lock))
			{rmdir($lock);}
		$this->out = 'unlocking : '.$lock;
	}

	public function status()
	{
		$lock      = $this->key;
		$this->out = file_exists($lock);
		return $this->out;
		//return is_dir($lockDir);  dans ce cas is_dir ne fonctionne pas ...
	}

}

class fileLock implements lockers
{
	/* pose un fichier vide comme verrou */

	var $key      ;
	var $out = '' ; /* variable qui stocke un éventuel résultat de retour de l'objet */

	function lockers($key='test')
	{
		/* compatibilité php4 */
		$this->__construct(($key));
	}

	function __construct($key='test')
		{$this->key = $this->keymaker($key);}

	public function keymaker($key='test')
		{return 'lockers/'.$key.'_locking';}

	public function lock()
	{
		$lock = $this->key;
		fopen($lock,'w+');
	}

	public function unlock()
	{
		$lock = $this->key;
		if(file_exists($lock))
			{unlink($lock);} // if
	}

	public function status()
	{
		$lock      = $this->key;
		$this->out = file_exists($lock);
		return $this->out;
	}

}

class semLock implements lockers
{
	/* pose un semaphore comme verrou */

	var $key      ;
	var $sem      ;
	var $locked   ;
	var $out = '' ; /* variable qui stocke un éventuel résultat de retour de l'objet */

	function lockers($key='test')
	{
		/* compatibilité php4 */
		$this->__construct(($key));
	}

	function __construct($key='test')
		{$this->key = $this->keymaker($key);}

	public function keymaker($key='test')
		{return 'lockers/'.$key.'_locking';}

	public function lock()
	{
		$lock         = $this->key        ;
		$this->sem    = sem_get ( $lock ) ;
		$this->locked = sem_acquire ( $this->sem )     ;
	}

	public function unlock()
	{
		if( $this->locked )
			{ $this->locked = !( sem_release ( $this->sem ) ) ; } // locked est faux si le semaphore est libere
	}

	public function status()
	{
		$this->out = $this->locked ;
		return $this->out          ;
	}

}

class popenLock implements lockers
{
	/* pose un fichier vide comme verrou, avec l'aide des commandes systeme */

	var $key      ;
	var $out = '' ; /* variable qui stocke un éventuel résultat de retour de l'objet */

	function lockers($key='test')
	{
		/* compatibilité php4 */
		$this->__construct(($key));
	}

	function __construct($key='test')
		{$this->key = $this->keymaker($key);}

	public function keymaker($key='test')
		{return 'lockers/'.$key.'_locking';}

	public function lock()
	{
		$lock = $this->key;
		$handle = popen("touch ".$lock , "r");
		pclose ( $handle );
	}

	public function unlock()
	{
		$lock = $this->key;
		if(file_exists($lock))
			{unlink($lock);} // if
	}

	public function status()
	{
		$lock      = $this->key;
		$this->out = file_exists($lock);
		return $this->out;
	}

}

?>

