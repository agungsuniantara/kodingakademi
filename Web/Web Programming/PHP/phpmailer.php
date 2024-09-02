<?php

$email = $_POST['email'];

use PHPMailer\PHPMailer\PHPMailer;

require 'PHPMailer-master\src\PHPMailer.php';
require 'PHPMailer-master\src\SMTP.php';

$mail = new PHPMailer;

$mail->isSMTP();
$mail->Host = 'smtp.gmail.com';
$mail->SMTPAuth = true;
$mail->Username = 'agungsuniantara@gmail.com';
$mail->Password = 'uyxf dflp pfhd fotq';
$mail->SMTPSecure = 'tls';
$mail->Port = 587;

$mail->setFrom('agungsuniantara@gmail.com');
$mail->addAddress($email);
$mail->Subject = 'Subject of the Email';
$mail->Body = 'berhasil registrasi !!!';

if (!$mail->send()) {
    echo "Mailer error: " . $mail->ErrorInfo;
} else {
    echo "Message has been sent succesfully";
}
