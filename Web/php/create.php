<?php
$filename = 'example.txt';

$file = fopen($filename, 'w');

if ($file) {
    fclose($file);
    echo 'File created successfully.';
} else {
    echo 'Error: Unable to create file ' . $filename;
}
?>