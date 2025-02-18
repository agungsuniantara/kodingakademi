<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="hasilassignment.php" method="POST">
        <label for="angka1">Angka 1 : </label>
        <input type="number" id="angka1" name="angka1"><br><br>
        <label for="operator">Operator : </label>
        <select name="operator" id="operator">
            <option value="tambah">tambah</option>
            <option value="kurang">kurang</option>
            <option value="bagi">bagi</option>
            <option value="kali">kali</option>
        </select><br><br>
        <label for="angka2">Angka 2 : </label>
        <input type="number" id="angka2" name="angka2">
        <input type="submit" value="Submit">
    </form>
</body>
</html>