<?php
    require 'config.php';
    session_start();
    
    if (!isset($_SESSION['user_id'])) {
        header("Location: login.php");
        exit;
    }
    
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $title = $_POST['title'];
        $content = $_POST['content'];
        $user_id = $_SESSION['user_id'];
    
        $sql = "INSERT INTO posts (user_id, title, content) 
                VALUES ('$user_id', '$title', '$content')";
        $query = mysqli_query($conn, $sql);
    
        if ($query) {
            header("Location: index.php");
        } else {
            header("Location: create_post.php");
        }
    }