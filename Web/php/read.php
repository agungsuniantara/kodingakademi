<?php
$filename = 'coba.txt';
$file = fopen($filename, 'r');

if ($file) {
    while ($line = fgets($file)) {
        echo $line . '<br>';
    }
    fclose($file);
} else {
    echo 'Error: Unable to open file ' . $filename;
}
