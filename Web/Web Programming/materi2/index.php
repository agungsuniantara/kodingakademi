<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Koding Akademi Employees</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
</head>

<body>
    <div class="container mt-4">
        <div class="row">
            <div class="col-md-12">
                <div class="card">
                    <div class="card-header">
                        <h4>Employees List
                            <a href="create.php" class="btn btn-primary float-end">Add Employees</a>
                        </h4>
                    </div>
                    <div class="card-body">

                        <table class="table table-bordered table-striped">
                            <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th>Email</th>
                                    <th>Address</th>
                                    <th>Phone</th>
                                    <th>Action</th>
                                </tr>
                            </thead>
                            <tbody>
                                <?php
                                $query = "SELECT * FROM employees";
                                $query_run = mysqli_query($con, $query);

                                if (mysqli_num_rows($query_run) > 0) {
                                    foreach ($query_run as $employee) {
                                ?>
                                        <tr>
                                            <td>
                                                <?= $employee['id']; ?>
                                            </td>
                                            <td>
                                                <?= $employee['name']; ?>
                                            </td>
                                            <td>
                                                <?= $employee['email']; ?>
                                            </td>
                                            <td>
                                                <?= $employee['address']; ?>
                                            </td>
                                            <td>
                                                <?= $employee['phone']; ?>
                                            </td>
                                            <td>
                                                <a href="view.php?id=<?= $employee['id']; ?>" class="btn btn-info btn-sm">View</a>
                                                <a href="edit.php?id=<?= $employee['id']; ?>" class="btn btn-success btn-sm">Edit</a>
                                                <form action="crud.php" method="POST" class="d-inline">
                                                    <button type="submit" name="delete_employee" value="<?= $employee['id']; ?>" class="btn btn-danger btn-sm">Delete</button>
                                                </form>
                                            </td>
                                        </tr>
                                <?php
                                    }
                                } else {
                                    echo "<h5> No Record Found </h5>";
                                }
                                ?>

                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous">
    </script>
</body>

</html>