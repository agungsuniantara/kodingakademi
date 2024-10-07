<?php
    require 'config.php';
    session_start();
    
    if (!isset($_SESSION['user_id'])) {
        header("Location: login.php");
        exit;
    }
    
    $sql = "SELECT posts.*, users.username FROM posts JOIN users ON posts.user_id = users.id ORDER BY posts.created_at DESC";
    $query = mysqli_query($conn, $sql);
    $fetch = mysqli_fetch_all($query, MYSQLI_ASSOC);
?>