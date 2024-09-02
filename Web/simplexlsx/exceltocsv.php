<?php
require 'SimpleXLSX.php';

if ($xlsx = Shuchkin\SimpleXLSX::parse('books.xlsx')) {
    $f = fopen('books.csv', 'wb');
    foreach ($xlsx->readRows() as $r) {
        fwrite($f, implode(',', $r) . PHP_EOL);
    }
    fclose($f);
} else {
    echo Shuchkin\SimpleXLSX::parseError();
}