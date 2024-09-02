<?php

$Firstname = $_POST['firstname'];
$Lastname = $_POST['lastname'];
$Email = $_POST['email'];
$Subject = $_POST['subject'];
$Phone = $_POST['phone'];
$Description = $_POST['description'];

use PHPMailer\PHPMailer\PHPMailer;

require 'PHPMailer-master/src/PHPMailer.php';
require 'PHPMailer-master/src/SMTP.php';

$mail = new PHPMailer;

$mail->isSMTP();
$mail->Host = 'smtp.gmail.com';
$mail->SMTPAuth = true;
$mail->Username = 'indonsiabambooster@gmail.com';
$mail->Password = 'ofns awbh pwjr oopr';
$mail->SMTPSecure = 'tls';
$mail->Port = 587;

$mail->setFrom('indonsiabmabooster@gmail.com');
$mail->addAddress($Email);
$mail->Subject = $Subject;
$mail->Body = "Data : \nNama = " . $Firstname . " " . $Lastname . "\nEmail = " . $Email . "\nPhone = " . $Phone . "\nDeskripsi = \n" . $Description;

if (!$mail->send()) {
    echo "Mailer error: " . $mail->ErrorInfo;
} else {
    echo "Message has been sent succesfully";
}
