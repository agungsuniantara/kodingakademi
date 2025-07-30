<?php
class Database {
    private $host = 'localhost';
    private $username = 'root';
    private $password = 'root';
    private $database = 'kasir_db';
    private $connection;
    private $inTransaction = false;
    
    public function __construct() {
        $this->connect();
    }
    
    private function connect() {
        try {
            $this->connection = new PDO(
                "mysql:unix_socket=/Applications/MAMP/tmp/mysql/mysql.sock;dbname={$this->database}",
                $this->username,
                $this->password,
                [
                    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
                ]
            );
        } catch (PDOException $e) {
            die("Connection failed: " . $e->getMessage());
        }
    }
    
    public function getConnection() {
        return $this->connection;
    }
    
    public function query($sql, $params = []) {
        try {
            $stmt = $this->connection->prepare($sql);
            $stmt->execute($params);
            return $stmt;
        } catch (PDOException $e) {
            throw new Exception("Query failed: " . $e->getMessage());
        }
    }
    
    public function fetchAll($sql, $params = []) {
        return $this->query($sql, $params)->fetchAll();
    }
    
    public function fetch($sql, $params = []) {
        return $this->query($sql, $params)->fetch();
    }
    
    public function lastInsertId() {
        return $this->connection->lastInsertId();
    }

    /**
     * Begin a database transaction
     * @throws Exception if a transaction is already active
     */
    public function beginTransaction() {
        try {
            if ($this->inTransaction) {
                throw new Exception("Transaction already in progress");
            }
            $this->connection->beginTransaction();
            $this->inTransaction = true;
        } catch (PDOException $e) {
            throw new Exception("Failed to begin transaction: " . $e->getMessage());
        }
    }

    /**
     * Commit the current transaction
     * @throws Exception if no transaction is active
     */
    public function commit() {
        try {
            if (!$this->inTransaction) {
                throw new Exception("No active transaction to commit");
            }
            $this->connection->commit();
            $this->inTransaction = false;
        } catch (PDOException $e) {
            throw new Exception("Failed to commit transaction: " . $e->getMessage());
        }
    }

    /**
     * Rollback the current transaction
     * @throws Exception if no transaction is active
     */
    public function rollback() {
        try {
            if (!$this->inTransaction) {
                throw new Exception("No active transaction to rollback");
            }
            $this->connection->rollBack();
            $this->inTransaction = false;
        } catch (PDOException $e) {
            throw new Exception("Failed to rollback transaction: " . $e->getMessage());
        }
    }

    /**
     * Check if a transaction is currently active
     * @return bool
     */
    public function inTransaction() {
        return $this->inTransaction;
    }
}
?>