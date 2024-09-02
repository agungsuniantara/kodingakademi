<?php
require 'config.php';
session_start();

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit;
}

$post_id = $_GET['id'];

$sql_post = "SELECT posts.*, users.username FROM posts JOIN users ON posts.user_id = users.id WHERE posts.id = '$post_id'";
$query_post = mysqli_query($conn, $sql_post);
$fetch_post = mysqli_fetch_assoc($query_post);

$sql_comment = "SELECT comments.*, users.username FROM comments JOIN users ON comments.user_id = users.id WHERE comments.post_id = '$post_id' ORDER BY comments.created_at ASC";
$query_comment = mysqli_query($conn, $sql_comment);
$fetch_comment = mysqli_fetch_all($query_comment, MYSQLI_ASSOC);

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_SESSION['user_id'])) {
    $content = $_POST['content'];
    $user_id = $_SESSION['user_id'];

    $sql = "INSERT INTO comments (post_id, user_id, content) VALUES ('$post_id', '$user_id', '$content')";
    $query = mysqli_query($conn, $sql);

    header("Location: view_post.php?id=$post_id");
}
?>

<!DOCTYPE html>
<html>

<head>
    <title>View Post</title>
    <style>
        <?php include "styles/style.css"?>
    </style>
</head>

<body>
    <header>
        <div class="container">
            <div id="branding">
                <h1>View post</h1>
            </div>
            <nav>
                <ul>
                    <li><a href="index.php">Recent post</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <div class="container">
        <article class="post">
            <h2><?= $fetch_post['title'] ?></h2>
            <p><?= $fetch_post['content'] ?></p>
            <p class="meta">By: <?= $fetch_post['username'] ?> at <?= $fetch_post['created_at'] ?></p>
        </article>

        <section class="comments">
            <h3>Comments</h3>
            <?php foreach ($fetch_comment as $comment) : ?>
                <div class="comment">
                    <p><?= $comment['content'] ?></p>
                    <p class="meta">By: <?= $comment['username'] ?> at <?= $comment['created_at'] ?></p>
                </div>
            <?php endforeach; ?>

            <?php if (isset($_SESSION['user_id'])) : ?>
                <form method="post" class="comment-form">
                    <textarea name="content" required></textarea><br>
                    <button type="submit">Comment</button>
                </form>
            <?php endif; ?>
        </section>
    </div>
</body>

</html>