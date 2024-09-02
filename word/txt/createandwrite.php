<?php
$filename = 'example.txt';
$content = 'create and write file txt php';

if (file_put_contents($filename, $content)) {
    echo 'File written successfully.';
} else {
    echo 'Error: Unable to create file ' . $filename;
}
