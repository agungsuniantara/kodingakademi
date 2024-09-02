<?php
$filename = 'coba2.txt';
$content = 'This is some example text that we want to write to a file.';

if (file_put_contents($filename, $content)) {
    echo 'File written successfully.';
} else {
    echo 'Error: Unable to create file ' . $filename;
}
