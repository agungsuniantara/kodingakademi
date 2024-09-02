<?php
require 'SimpleXLSX.php';

if ($xlsx = Shuchkin\SimpleXLSX::parse('books.xlsx')) {
    print_r($xlsx->rows());
} else {
    echo Shuchkin\SimpleXLSX::parseError();
}
