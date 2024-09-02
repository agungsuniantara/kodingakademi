<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>


  <table border=solid 1px>
    <tr>
      <th>id</th>
      <th>nama</th>
      <th>alamat</th>
      <th>umur</th>
      <th>email</th>
      
    </tr>

    
      <?php
      $sambung = mysqli_connect("localhost", "root", "", "dbprabu");

      $sql = "SELECT * FROM dbprabu.user";
      $prab = mysqli_query($sambung, $sql);


      foreach ($prab as $d) {
        echo "<tr>";
        echo "<td>$d[id]</td>";
        echo "<td>$d[nama]</td>";
        echo "<td>$d[alamat]</td>";
        echo "<td>$d[umur]</td>";
        echo "<td>$d[email]</td>";
        echo "</tr>";
      }


      ?>

  </table>

</body>

</html>