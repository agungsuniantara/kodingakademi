<?php
    require 'php/php_viewpost.php';
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