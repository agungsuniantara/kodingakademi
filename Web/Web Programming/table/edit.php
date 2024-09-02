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
            <h3>Edit Employee</h3>
        </div>
        <div class="form-table">
            <form action="edit_employee.php" method="post">
                <div class="employee">
                    <?php
                    include "config.php";
                    $id = $_GET['id'];

                    $sql = "select * from kodingakademi.employees where id = '$id'";
                    $query = mysqli_query($conn, $sql);

                    foreach ($query as $data) {
                    ?>
                        <input type="text" value="<?php echo $id ?>" name="id" hidden>
                        <div>
                            <label for="name">Name :</label>
                            <input type="text" value="<?php echo $data['name'] ?>" name="name">
                        </div>
                        <div>
                            <label for="email">Email :</label>
                            <input type="email" value="<?php echo $data['email'] ?>" name="email">
                        </div>
                        <div>
                            <label for="address">Address :</label>
                            <input type="text" value="<?php echo $data['address'] ?>" name="address">
                        </div>
                        <div>
                            <label for="phone">Phone :</label>
                            <input type="text" value="<?php echo $data['phone'] ?>" name="phone">
                        </div>
                        <div>
                            <div>
                                <input type="submit" value="Submit">
                                <a href="index.php">View Table</a>
                            </div>
                        </div>
                    <?php
                    }
                    ?>
                </div>
            </form>
        </div>
    </div>
</body>

</html>