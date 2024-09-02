<?php
require 'vendor/autoload.php';

use PhpOffice\PhpSpreadsheet\Spreadsheet;
use PhpOffice\PhpSpreadsheet\Writer\Xlsx;

$spreadsheet = new Spreadsheet();
$writer = new Xlsx($spreadsheet);
$writer->save('example.xlsx');
echo "File Excel berhasil dibuat.";
