<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <table>
        <tr>
            <td>Nama</td>
            <td>Price</td>
            <td>Date</td>
        </tr>
        <?php
        $koneksi = mysqli_connect("localhost", "root", "", "project");

        $sql = "select * from project.product";

        $query = mysqli_query($koneksi, $sql);

        foreach ($query as $data) {
        ?>
            <tr>
                <td><?php echo $data['name'] ?></td>
                <td><?php echo $data['price'] ?></td>
                <td><?php echo $data['date'] ?></td>
            </tr>
        <?php
        }
        ?>
    </table>
</body>

</html>