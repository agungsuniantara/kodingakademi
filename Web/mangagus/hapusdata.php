<?php
    session_start();
    include "koneksi.php";
    $id = $_GET['id'];

    $sql = "delete from finalproject.barang where id='$id'";

    mysqli_query($koneksi,$sql);
	
	echo "
		<script>
			alert ('Data sudah dihapus');
			location.href='home.php';
		</script>
	";
