<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>

  <?php
  $data = [2, "prabu", "denpasar", "0999009", "prab0900@gmail.com"];
  $data2 = [2, "agungu", "ddfvdfvdfvnpasar", "0999009", "prab0900@gmail.com"];
   $data = [2, "prabu", "denpasar", "0999009", "prab0900@gmail.com"];
  $data2 = [2, "agungu", "ddfvdfvdfvnpasar", "0999009", "prab0900@gmail.com"];
  
  ?>

  <table border="solid 1pxn  ">
    <tr>
      <th>no</th>
      <th>nama</th>
      <th>alamat</th>
      <th>no telfn</th>
      <th>email</th>
    </tr>
    <tr>
      <td><?php echo "$data[0]" ?></td>
      <td><?php echo "$data[1]" ?></td>
      <td><?php echo "$data[2]" ?></td>
      <td><?php echo "$data[3]" ?></td>
      <td><?php echo "$data[4]" ?></td>
    </tr>

  </table>

  <table border="solid 1pxn  ">
    <tr>
      <th>no</th>
      <th>nama</th>
      <th>alamat</th>
      <th>no telfn</th>
      <th>email</th>
    </tr>

    <tr>
      <?php 
      foreach($data as $e) {

          
      ?>
      <td><?php echo $e ?></td>
    <?php  
      }
    ?>
    </tr>


    <tr>
      <?php 
      foreach($data2 as $r) {

          
      ?>
      <td><?php echo $r ?></td>
    <?php  
      }
    ?>
    </tr>
    <tr>
      <?php
      foreach ($data as $a){
        echo "<td>$a</td>";
      }
      ?>
    </tr>

  </table>

  
</body>

</html>