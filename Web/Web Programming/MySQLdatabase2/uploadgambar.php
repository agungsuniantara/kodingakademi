<?php
    session_start();
    include "koneksi.php";

    $KodeOrder = $_POST['id_order'];

    $image = $_FILES['image'];
    $imagefilename = $image['name'];
    $imagefiletmp = $image['tmp_name'];
    $filename_separate = explode('.', $imagefilename);
    $file_extension = strtolower(end($filename_separate));
    $extension = array('jpeg', 'jpg', 'png');
        if(in_array($file_extension,$extension)){
        $upload_image='image/'.$imagefilename;
        move_uploaded_file($imagefiletmp,$upload_image);

        $sql = "update coba.db_order set image='$upload_image' where id_order='$KodeOrder'";

        $query=mysqli_query($koneksi,$sql);

        if($query)
        {
            echo "<script>
            alert ('Edit berhasil');
            location.href='home.php';
            </script>";
        }
        else
        {
            echo "<script>
            alert ('Edit gagal');
            location.href='home.php';
            </script>";	
        }	
    }	
?>