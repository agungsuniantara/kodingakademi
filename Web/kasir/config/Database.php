<?php
class Database {
    private static $instance = null;
    public static function getInstance() {
        if (!self::$instance) {
            self::$instance = new PDO('mysql:host=localhost;dbname=kasir_db', 'root', 'root');
            self::$instance->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        }
        return self::$instance;
    }
}

?>
