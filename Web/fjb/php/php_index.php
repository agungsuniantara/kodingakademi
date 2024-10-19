<?php
    require 'config.php';
    session_start(); 

    $sql = "SELECT posts.id, posts.title, posts.content, users.username, posts.created_at 
            FROM posts 
            JOIN users ON posts.user_id = users.id 
            ORDER BY posts.created_at DESC";

    $query = mysqli_query($conn, $sql);

    if ($query && mysqli_num_rows($query) > 0) {
        $fetch = []; 
        while ($row = mysqli_fetch_assoc($query)) {
            $fetch[] = $row;
        }
    } else {
        $fetch = [];
    }
