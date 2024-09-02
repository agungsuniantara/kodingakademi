<?php 
$dbhost="localhost"; 
$dbName="coba"; 
$user="root"; 
$pass=""; 
$conn = new mysqli($dbhost,$user,$pass,$dbName); 
try{ 
echo "Successfully connected with newdb database"; 
} 
catch(Exception $e){ 
die("Connection failed".$e->getMessage()); 
} 
?>