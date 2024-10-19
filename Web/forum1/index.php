<?php
    // require 'php/php_index.php';
?>

<!DOCTYPE html>
<html>
<head>
    <title>Forum Jual Beli</title>
    <style>
        <?php include "styles/style.css"?>
    </style>
</head>
<body>
    <header>
        <div class="container">
            <div id="branding">
                <h1>Forum</h1>
            </div>
            <nav>
                <ul>
                    <li><a href="create_post.php">Create Post</a></li>
                    <li><a href="php/logout.php">Logout</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <div class="container">
        <h2>Recent post</h2>
        <?php foreach ($fetch as $post): ?>
            <div class="posts">
                <h4><a href="view_post.php?id=<?= $post['id'] ?>"><?= $post['title'] ?></a></h4>
                <p><?= $post['content'] ?></p>
                <p class="meta">By: <?= $post['username'] ?> at <?= $post['created_at'] ?></p>
            </div>
        <?php endforeach; ?>
    </div>
</body>
</html>
