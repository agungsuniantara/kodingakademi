<?php
require 'SimpleXLSX.php';

if ($xlsx = Shuchkin\SimpleXLSX::parse('books.xlsx')) {
    $f = fopen('books.csv', 'wb');
    foreach ($xlsx->readRows() as $r) {
        fwrite($f, implode(',', $r) . PHP_EOL);
    }
    fclose($f);
    $message = 'CSV file generated successfully.';
    $downloadLink = '<a href="books.csv" download>Download Books CSV</a>';
} else {
    $message = 'Error: ' . Shuchkin\SimpleXLSX::parseError();
    $downloadLink = '';
}
?>

<!DOCTYPE html>
<html>

<head>
    <title>Convert XLSX to CSV</title>
</head>

<body>
    <p><?php echo $message; ?></p>
    <p><?php echo $downloadLink; ?></p>
</body>

</html>