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
            <h3>Add Employee</h3>
        </div>
        <div class="form-table">
            <form action="employee.php" method="post">
                <div class="employee">
                    <div>
                        <label for="name">Name :</label>
                        <input type="text" placeholder="Enter Username" name="name" required>
                    </div>
                    <div>
                        <label for="email">Email :</label>
                        <input type="email" placeholder="Enter Email" name="email" required>
                    </div>
                    <div>
                        <label for="address">Address :</label>
                        <input type="text" placeholder="Enter Address" name="address" required>
                    </div>
                    <div>
                        <label for="phone">Phone :</label>
                        <input type="number" placeholder="Enter Phone" name="phone" required>
                    </div>
                    <div>
                        <div>
                            <input type="submit" value="Submit">
                            <a href="index.php">View Table</a>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    </div>
</body>

</html>