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

    $sql = "INSERT INTO posts (user_id, title, content) VALUES ('$user_id', '$title', '$content')";
    $query = mysqli_query($conn, $sql);

    if ($query) {
        header("Location: index.php");
    } else {
        header("Location: create_post.php");
    }
}
?>

<!DOCTYPE html>
<html>

<head>
    <title>Create Post</title>
    <style>
        <?php include "styles/style.css"?>
    </style>
</head>

<body>
    <header>
        <div class="container">
            <div id="branding">
                <h1>Create post</h1>
            </div>
            <nav>
                <ul>
                    <li><a href="index.php">Recent Post</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <div class="container-post">
        <form method="post" class="post-form">
            <label for="title">Title:</label>
            <input type="text" id="title" name="title" required><br>

            <label for="content">Content:</label>
            <textarea id="content" name="content" required></textarea><br>

            <button type="submit">Create</button>
        </form>
    </div>
</body>

</html>