<?php
    session_start();
    include "alert.php";
    // Store cart data before destroying session
    $cart = isset($_SESSION['cart']) ? $_SESSION['cart'] : array();
    session_destroy();
    
    // Start new session and restore cart
    session_start();
    $_SESSION['cart'] = $cart;

    showAlert('Berhasil Logout', 'success', 'login.php');
?>