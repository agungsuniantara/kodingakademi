<?php
    session_start();
    include "koneksi.php";
    $KodeOrder = $_GET['KodeOrder'];

    $sql = "delete from coba.db_order where id_order='$KodeOrder'";

    mysqli_query($koneksi,$sql);
	
	echo "
		<script>
			alert ('Data sudah dihapus');
			location.href='home.php';
		</script>
	";
?>