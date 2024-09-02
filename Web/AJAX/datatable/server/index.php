<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>DataTables with AJAX</title>
  <link rel="stylesheet" href="https://cdn.datatables.net/1.10.23/css/jquery.dataTables.min.css" />
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
  <script src="https://cdn.datatables.net/1.10.23/js/jquery.dataTables.min.js"></script>
  <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/responsive/2.2.7/css/responsive.dataTables.min.css">
  <script src="https://cdn.datatables.net/responsive/2.2.7/js/dataTables.responsive.js"></script>
  <link rel="stylesheet" href="style.css" />
</head>

<body>
  <table id="myDataTable">
    <thead>
      <tr>
        <th>Name</th>
        <th>Email</th>
        <th>Number</th>
        <th>Phone</th>
        <th>File</th>
        <th>Password</th>
        <th>Actions</th>
      </tr>
    </thead>
    <tbody></tbody>
  </table>
  <script src="ajax.js"></script>
</body>

</html>