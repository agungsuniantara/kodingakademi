<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRUD</title>
    <style>
        <?php include "style.css" ?>
    </style>
</head>

<body>
    <div class="wrapper">
        <div class="add-employee">
            <h3>Employee List</h3>
            <div class="search-employee">
                <form action="index.php" action="get">
                    <input type="text" name="cari" placeholder="Cari Nama" style="height: 24px; width:150px;" value="<?php echo $_GET['cari'] ?? '' ?>">
                    <input type="submit" value="Search">
                </form>
                <a href="add.php" class="add">Add Employees</a>
            </div>
        </div>
        <div class="form-table">
            <table>
                <tr>
                    <th>No</th>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Address</th>
                    <th>Phone</th>
                    <th>Action</th>
                </tr>

                <?php
                include "config.php";

                $sql = "select * from kodingakademi.employees";
                $query = mysqli_query($conn, $sql);
                $no = 1;

                if (isset($_GET['cari'])) {
                    $keyword = $_GET['cari'];
                    $sql =
                        "SELECT * FROM kodingakademi.employees WHERE name LIKE '%$keyword%'";
                    $query_cari = mysqli_query($conn, $sql);

                    foreach ($query_cari as $data) {
                ?>
                        <tr>
                            <td><?php echo $no ?></td>
                            <td><?php echo $data['name'] ?></td>
                            <td><?php echo $data['email'] ?></td>
                            <td><?php echo $data['address'] ?></td>
                            <td><?php echo $data['phone'] ?></td>
                            <td>
                                <a href="edit.php?id=<?php echo $data['id'] ?>" class="edit">Edit</a>
                                <a href="delete.php?id=<?php echo $data['id'] ?>" class="delete">Delete</a>
                            </td>
                        </tr>
                    <?php
                        $no++;
                    }
                } else {
                    // Tampilkan semua data jika tidak ada pencarian
                    foreach ($query as $data) {
                    ?>
                        <tr>
                            <td><?php echo $no ?></td>
                            <td><?php echo $data['name'] ?></td>
                            <td><?php echo $data['email'] ?></td>
                            <td><?php echo $data['address'] ?></td>
                            <td><?php echo $data['phone'] ?></td>
                            <td>
                                <a href="edit.php?id=<?php echo $data['id'] ?>" class="edit">Edit</a>
                                <a href="delete.php?id=<?php echo $data['id'] ?>" class="delete">Delete</a>
                            </td>
                        </tr>
                <?php
                        $no++;
                    }
                }
                ?>

            </table>
        </div>
    </div>
</body>

</html>