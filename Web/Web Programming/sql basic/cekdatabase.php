<?php
	include "koneksi.php"; //buka koneksi

	if ($koneksi)
	{
		echo "berhasil terkoneksi";
	}
	else
	{
		echo "gagal terkoneksi";
	}
?>
