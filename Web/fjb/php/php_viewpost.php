<?php
    require 'config.php';
    session_start();
    
    if (!isset($_SESSION['user_id'])) {
        header("Location: login.php");
        exit;
    }
    
    $post_id = $_GET['id'];
    
    $sql_post = "SELECT posts.*, users.username 
                 FROM posts 
                 JOIN users ON posts.user_id = users.id 
                 WHERE posts.id = '$post_id'";

    $query_post = mysqli_query($conn, $sql_post);
    $fetch_post = mysqli_fetch_assoc($query_post);
    
    $sql_comment = "SELECT comments.*, users.username 
                    FROM comments 
                    JOIN users ON comments.user_id = users.id 
                    WHERE comments.post_id = '$post_id' 
                    ORDER BY comments.created_at ASC";

    $query_comment = mysqli_query($conn, $sql_comment);
    $fetch_comment = mysqli_fetch_all($query_comment, MYSQLI_ASSOC);
    
    if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_SESSION['user_id'])) {
        $content = $_POST['content'];
        $user_id = $_SESSION['user_id'];
    
        $sql = "INSERT INTO comments (post_id, user_id, content) 
                VALUES ('$post_id', '$user_id', '$content')";
        $query = mysqli_query($conn, $sql);
    
        header("Location: view_post.php?id=$post_id");
    }