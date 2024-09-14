<?php
    $koneksi=mysqli_connect('localhost','root','','coba');

    if ($koneksi)
	{
		echo "berhasil terkoneksi";
	}
	else
	{
		echo "gagal terkoneksi";
	}
?>