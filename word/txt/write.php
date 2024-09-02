<?php
$filename = 'example.txt';
$content = 'This is some example text that we want to write to a file.';

$file = fopen($filename, 'w');

if ($file) {
    fwrite($file, $content);
    fclose($file);
    echo 'File written successfully.';
} else {
    echo 'Error: Unable to create file ' . $filename;
}
