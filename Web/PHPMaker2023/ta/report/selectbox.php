<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Latihan Form Filter Data</title>
    <!-- bootstrap css  -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
        integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
</head>
<?php
  
    //sesuaikan dengan database, username, dan password kalian masing-masing
    $servername     = "localhost";
    $database       = "travel_web"; 
    $username       = "root";
    $password       = "";

    // membuat koneksi
    $conn   = mysqli_connect($servername, $username, $password, $database);

    //jika jurusan sudah diset maka masukkan datanya ke dalam variabel $cari
    if(isset($_GET['code_vnd_category'])){
        $cari = $_GET['code_vnd_category'];

        //ambil data dari database, dimana pencarian sesuai dengan variabel cari
        $data = mysqli_query($conn, "select * from d_vendor where code_vnd_category = '$cari'");
		
    }else{

        //tapi jika jurusan belum diset, maka jangan tampilkan apapun
        $data = [];		
    }
?>
<body>
<br>
    <div class="container jumbotron">
    <!-- membuat form dropdown jurusan dengan id = form_id -->
        <form action="selectbox.php" method="GET" id="form_id">
            <div class="form-group">
                <label for="exampleInputEmail1">Vendor Category</label>
                <!-- gunakan event onchange untuk mengirim data secara otomatis  -->
                <select class="form-control" name="code_vnd_category" onChange="document.getElementById('form_id').submit();">
                  
                    <option 'Airline Ticket' value="1">Airline Ticket</option>													
                    <option 'Hotel' value="2">Hotel</option>
                    <option 'Restaurant' value="3">Restaurant</option>
                    <option 'Activity' value="4">Activity</option>
					<option 'Guide' value="5">Guide</option>
					<option 'Transport' value="6">Transport</option>
					<option 'Others' value="7">Others</option>
					
                </select>
            </div>
        </form>
        <form>
            <hr>
            <div class="form-group">
                <label for="exampleInputPassword1">Vendor</label> 
                <select class="form-control">
                
                    <!-- data ditampilkan berdasarkan jurusan yang dipilih
                    untuk logikanya ada pada line 24 hingga 33 -->
                    <?php while($d = mysqli_fetch_array($data)){ ?>
                        <option><?php echo $d['name']; ?></option>
                    <?php } ?>
                </select>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</body>

</html>