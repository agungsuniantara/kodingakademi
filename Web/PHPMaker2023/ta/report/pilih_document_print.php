<?php

session_start(); //memulai session
     
  if(isset($_GET['id']))
     {
	  $_SESSION['id'] = $_GET['id'];
     }	
	  
     $pv_id =$_SESSION['id'];
  
   
  if(isset($_GET['tmp_un']))
     {
	  $_SESSION['tmp_un'] = $_GET['tmp_un'];
     }	

  
  if(isset($_GET['tmp_acs_rsv']))
     {
	  $_SESSION['tmp_acs_rsv'] = $_GET['tmp_acs_rsv'];
     }	
	
	$pv_acs_rsv =$_SESSION['tmp_acs_rsv'];
	
  if(isset($_GET['tmp_acs_opr']))
     {
	  $_SESSION['tmp_acs_opr'] = $_GET['tmp_acs_opr'];
     }	
	 
	 $pv_acs_opr =$_SESSION['tmp_acs_opr'];
	 	   
  if(isset($_GET['document_print']))
    {
	 $_SESSION['document_print'] = $_GET['document_print'];
    }	
	 	 	 	 
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document Print</title>
   
<!-- CSS untuk bootstrap -->
	<link rel="stylesheet" href="css/bootstrap.css" type="text/css">
	<!-- CSS untuk bootstrap datetimepicker -->
	<link rel="stylesheet" href="css/bootstrap-datetimepicker.min.css" type="text/css">   


  <!-- bootstrap css  
	
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
        integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
	
-->


	
</head>

<body>
<br>

   

    
	
	<?php
	 include('dbconnection.php');

        $conn = mysqli_connect($servername, $username, $password, $dbname) or die("Connection failed: " . mysqli_connect_error());
       
	   /* check connection */
          if (mysqli_connect_errno()) {
              printf("Connect failed: %s\n", mysqli_connect_error());
          exit();
          } 
      
        
	   
       
                			
	?>
	



<!-- JIKA USER OPERATION  -->	
	<?php 
      if ($pv_acs_opr != '1')
	  {        
    ?>
		  
	<!-- DOCUMENT PRINT -->
	<div align="center" class="container jumbotron">
    <!-- membuat form dropdown document print dengan id = form_id -->
        
		
		<form action="proses_pilih_document_print.php" method="GET" id="form_id_01">
            <div class="form-group">
                <div>
				<label for="exampleInputEmail1">Document Print</label>
				</div>
                <!-- gunakan event onchange untuk mengirim data secara otomatis  -->
			
                <select class="col-lg-4 col-lg-offset-4" name="document_print">                    
                    <option value="doc1">Final Confirmation</option> 

					<?php if ($pv_acs_rsv != '1')
	                  { 
				    ?>
					
                    <option value="doc2">Cost of Sales</option>
	                <option value="doc3">Profit/Loss</option>
					
					<?php
					}
					?>
					
					
					
                </select>
								             
			</div>
			
		     <br>
		
     			<button type="submit" class="btn btn-primary">PDF</button>
			
									
        </form>
		
		
		
    </div>
	<?php 
      }        
    ?>
	
 
	
	
	 <!-- GUIDE INSTRUCTION -->
	<div align="center" class="container jumbotron">
    <!-- membuat form dropdown document print dengan id = form_id -->
        
		
		  <form action="..\report_tcpdf\test\pdf_guide_instruction.php" method="GET" id="form_id_02"> 
		
		
            <div class="form-group">
                <div>
				<label for="exampleInputEmail1">Guide Instruction</label>
				</div>
                <!-- gunakan event onchange untuk mengirim data secara otomatis  -->
			
                <select class="col-lg-4 col-lg-offset-4" name="guide_id">                    
                    
					     <?php
							// $pv_blank="";
							//   echo "<option value='".$pv_blank."'>"."SEMUA LEMBAGA"."</option>";
						 

                         // query
						    $sql_guide_instruction ="SELECT * FROM t_rsv_gde WHERE code_id_rsv='$pv_id' order by tanggal_in_gde";		        					  						        		        		 
 		                    $rs_result_guide_instruction = mysqli_query($conn, $sql_guide_instruction);   
				 
							
					     while ( $d=mysqli_fetch_assoc($rs_result_guide_instruction)) {
							 
							     $pv_kode_gde=$d['kode_gde'];
								
		                         $sql_nama_gde = "SELECT name FROM d_guide WHERE id='$pv_kode_gde'";  
                                 $rs_result_nama_gde = mysqli_query($conn, $sql_nama_gde);  
                                 $row_nama_gde = mysqli_fetch_assoc($rs_result_nama_gde);
                                 $pv_guide_name=$row_nama_gde["name"];
							   
                                							   
                               echo "<option value='".$d['kode_gde']."'>".$pv_guide_name."</option>";
							   							  
                            }
					      ?>
					
                </select>
								             
			</div>
			
		         
			 
		     <br>
		
     			<button type="submit" class="btn btn-primary">PDF</button>
			            									
        </form>
		        	
    <!-- </div> -->
	
		
	 <!-- GUIDE CASH BON -->
<!--	 <div align="center" class="container jumbotron"> -->
    <!-- membuat form dropdown document print dengan id = form_id -->
        
		<br>
		<br>
		
		
		  <form action="..\report_tcpdf\test\pdf_guide_cash_bon.php" method="GET" id="form_id_02"> 
		
		
            <div class="form-group">
                <div>
				<label for="exampleInputEmail1">Guide Cash Bon</label>
				</div>
                <!-- gunakan event onchange untuk mengirim data secara otomatis  -->
			
                <select class="col-lg-4 col-lg-offset-4" name="guide_id_kb">                    
                    
					     <?php
							// $pv_blank="";
							//   echo "<option value='".$pv_blank."'>"."SEMUA LEMBAGA"."</option>";
						 

                         // query
						    $sql_guide_instruction ="SELECT * FROM t_rsv_gde WHERE code_id_rsv='$pv_id' order by tanggal_in_gde";		        					  						        		        		 
 		                    $rs_result_guide_instruction = mysqli_query($conn, $sql_guide_instruction);   
				 
							
					     while ( $d=mysqli_fetch_assoc($rs_result_guide_instruction)) {
							 
							     $pv_kode_gde=$d['kode_gde'];
								
		                         $sql_nama_gde = "SELECT name FROM d_guide WHERE id='$pv_kode_gde'";  
                                 $rs_result_nama_gde = mysqli_query($conn, $sql_nama_gde);  
                                 $row_nama_gde = mysqli_fetch_assoc($rs_result_nama_gde);
                                 $pv_guide_name=$row_nama_gde["name"];
							   
                                							   
                               echo "<option value='".$d['kode_gde']."'>".$pv_guide_name."</option>";
							   							  
                            }
					      ?>
					
                </select>
								             
			</div>
					         			
		     <br>
		
     			<button type="submit" class="btn btn-primary">PDF</button>
			            									
        </form>
		        	
    </div>
	
						
	<!-- HOTEL VOUCHER -->
	<div align="center" class="container jumbotron">
    <!-- membuat form dropdown document print dengan id = form_id -->
             
<!--		<form action="pdf_voucher_hotel.php" method="GET" id="form_id_02"> -->
 <form action="..\report_tcpdf\test\pdf_voucher_hotel.php" method="GET" id="form_id_02">
 


            <div class="form-group">
                <div>
				<label for="exampleInputEmail1">Hotel Voucher</label>
				</div>
                <!-- gunakan event onchange untuk mengirim data secara otomatis  -->
			
                <select class="col-lg-4 col-lg-offset-4" name="voucher_hotel_id">                    
                    
					     <?php
							// $pv_blank="";
							//   echo "<option value='".$pv_blank."'>"."SEMUA LEMBAGA"."</option>";
						 

                         // query
						    $pv_code_vnd_category='2'; // hotel
						    $sql_hotel_voucher ="SELECT * FROM t_rsv_nett WHERE code_id_rsv='$pv_id' and code_vnd_category='$pv_code_vnd_category'";		        					  						        		        		 
 		                    $rs_result_hotel_voucher = mysqli_query($conn, $sql_hotel_voucher);   
				 
							
					     while ( $d=mysqli_fetch_assoc($rs_result_hotel_voucher)) {
							     
								 // record ke berapa ?
								 $pv_code_rcd=$d['id'];
								 
							     $pv_code_vnd=$d['code_id_gbg'];
								 
								 // gabungkan
								 $pv_id_gabung=$pv_code_rcd.'+'.$pv_code_vnd;
								
		                         $sql_nama_htl = "SELECT name FROM d_vendor_gbg WHERE id='$pv_code_vnd'";  
                                 $rs_result_nama_htl = mysqli_query($conn, $sql_nama_htl);  
                                 $row_nama_htl = mysqli_fetch_assoc($rs_result_nama_htl);
                                 $pv_hotel_name=$row_nama_htl["name"];
							                                   							  
                              if ($pv_hotel_name != '') {
								 
								 echo "<option value='".$pv_id_gabung."'>".$pv_hotel_name."</option>";
							     
								 }
							   							  
                            }
					      ?>
					
                </select>
								             
			</div>
			
		         
			 
		     <br>
		
     			<button type="submit" class="btn btn-primary">PDF</button>
			
            
			
									
        </form>
		        	
    </div>
	
	
	<!-- RESTAURANT VOUCHER -->
	<div align="center" class="container jumbotron">
    <!-- membuat form dropdown document print dengan id = form_id -->
        		
  <!--		<form action="pdf_voucher_restaurant.php" method="GET" id="form_id_02"> -->
  <form action="..\report_tcpdf\test\pdf_voucher_restaurant.php" method="GET" id="form_id_02">
 
       

	   <div class="form-group">
                <div>
				<label for="exampleInputEmail1">Restaurant Voucher</label>
				</div>
                <!-- gunakan event onchange untuk mengirim data secara otomatis  -->
			
                <select class="col-lg-4 col-lg-offset-4" name="voucher_restaurant_id">                    
                    
					     <?php
							// $pv_blank="";
							//   echo "<option value='".$pv_blank."'>"."SEMUA LEMBAGA"."</option>";
						 

                         // query
						    $pv_code_vnd_category='3'; // restaurant
						    $sql_restaurant_voucher ="SELECT * FROM t_rsv_nett WHERE code_id_rsv='$pv_id' and code_vnd_category='$pv_code_vnd_category'";		        					  						        		        		 
 		                    $rs_result_restaurant_voucher = mysqli_query($conn, $sql_restaurant_voucher);   
				 
							
					     while ( $d=mysqli_fetch_assoc($rs_result_restaurant_voucher)) {
							     
								 // record ke berapa ?
								 $pv_code_rcd=$d['id'];
								 
							     $pv_code_vnd=$d['code_id_gbg'];
								 
								 // gabungkan
								 $pv_id_gabung=$pv_code_rcd.'+'.$pv_code_vnd;
								
		                         $sql_nama_restaurant = "SELECT name FROM d_vendor_gbg WHERE id='$pv_code_vnd'";  
                                 $rs_result_nama_restaurant = mysqli_query($conn, $sql_nama_restaurant);  
                                 $row_nama_restaurant = mysqli_fetch_assoc($rs_result_nama_restaurant);
                                 $pv_restaurant_name=$row_nama_restaurant["name"];
							                                   							  
                              if ($pv_restaurant_name != '') {
								 
								 echo "<option value='".$pv_id_gabung."'>".$pv_restaurant_name."</option>";
							     
								 }
							   							  
                            }
					      ?>
					
                </select>
								             
			</div>
			
		         
			 
		     <br>
		
     			<button type="submit" class="btn btn-primary">PDF</button>
			
            
			
									
        </form>
		        	
    </div>
	
	
	
<!-- ACTIVITY VOUCHER -->
	<div align="center" class="container jumbotron">
    <!-- membuat form dropdown document print dengan id = form_id -->
        		
	<!--	<form action="pdf_voucher_activity.php" method="GET" id="form_id_02"> -->
	<form action="..\report_tcpdf\test\pdf_voucher_activity.php" method="GET" id="form_id_02">
 
	
            <div class="form-group">
                <div>
				<label for="exampleInputEmail1">Activity Voucher</label>
				</div>
                <!-- gunakan event onchange untuk mengirim data secara otomatis  -->
			
                <select class="col-lg-4 col-lg-offset-4" name="voucher_activity_id">                    
                    
					     <?php
							// $pv_blank="";
							//   echo "<option value='".$pv_blank."'>"."SEMUA LEMBAGA"."</option>";
						 

                         // query
						    $pv_code_vnd_category='5'; // activity
						    $sql_activity_voucher ="SELECT * FROM t_rsv_nett WHERE code_id_rsv='$pv_id' and code_vnd_category='$pv_code_vnd_category'";		        					  						        		        		 
 		                    $rs_result_activity_voucher = mysqli_query($conn, $sql_activity_voucher);   
				 
							
					     while ( $d=mysqli_fetch_assoc($rs_result_activity_voucher)) {
							     
								 // record ke berapa ?
								 $pv_code_rcd=$d['id'];
								 
							     $pv_code_vnd=$d['code_id_gbg'];
								 
								 // gabungkan
								 $pv_id_gabung=$pv_code_rcd.'+'.$pv_code_vnd;
								
		                         $sql_nama_activity = "SELECT name FROM d_vendor_gbg WHERE id='$pv_code_vnd'";  
                                 $rs_result_nama_activity = mysqli_query($conn, $sql_nama_activity);  
                                 $row_nama_activity = mysqli_fetch_assoc($rs_result_nama_activity);
                                 $pv_activity_name=$row_nama_activity["name"];
							                                   							  
                              if ($pv_activity_name != '') {
								 
								 echo "<option value='".$pv_id_gabung."'>".$pv_activity_name."</option>";
							     
								 }
							   							  
                            }
					      ?>
					
                </select>
								             
			</div>
			
		         
			 
		     <br>
		
     			<button type="submit" class="btn btn-primary">PDF</button>
			
            									
        </form>
		        	
    </div>
		
<!-- TRANSPORT VOUCHER -->
	<div align="center" class="container jumbotron">
    <!-- membuat form dropdown document print dengan id = form_id -->
        		
	<!--	<form action="pdf_voucher_transport.php" method="GET" id="form_id_02"> -->
		<form action="..\report_tcpdf\test\pdf_voucher_transport.php" method="GET" id="form_id_02">
 
		
            <div class="form-group">
                <div>
				<label for="exampleInputEmail1">Transport Voucher</label>
				</div>
                <!-- gunakan event onchange untuk mengirim data secara otomatis  -->
			
                <select class="col-lg-4 col-lg-offset-4" name="voucher_transport_id">                    
                    
					     <?php
							// $pv_blank="";
							//   echo "<option value='".$pv_blank."'>"."SEMUA LEMBAGA"."</option>";
						 

                         // query
						    $pv_code_vnd_category='6'; // transport
						    $sql_transport_voucher ="SELECT * FROM t_rsv_nett WHERE code_id_rsv='$pv_id' and code_vnd_category='$pv_code_vnd_category'";		        					  						        		        		 
 		                    $rs_result_transport_voucher = mysqli_query($conn, $sql_transport_voucher);   
				 
							
					     while ( $d=mysqli_fetch_assoc($rs_result_transport_voucher)) {
							     
								 // record ke berapa ?
								 $pv_code_rcd=$d['id'];
								 
							     $pv_code_vnd=$d['code_id_gbg'];
								 
								 // gabungkan
								 $pv_id_gabung=$pv_code_rcd.'+'.$pv_code_vnd;
								
		                         $sql_nama_transport = "SELECT name FROM d_vendor_gbg WHERE id='$pv_code_vnd'";  
                                 $rs_result_nama_transport = mysqli_query($conn, $sql_nama_transport);  
                                 $row_nama_transport = mysqli_fetch_assoc($rs_result_nama_transport);
                                 $pv_transport_name=$row_nama_transport["name"];
							                                   							  
                              if ($pv_transport_name != '') {
								 
								 echo "<option value='".$pv_id_gabung."'>".$pv_transport_name."</option>";
							     
								 }
							   							  
                            }
					      ?>
					
                </select>
								             
			</div>
			
		         
			 
		     <br>
		
     			<button type="submit" class="btn btn-primary">PDF</button>
			
            
			
									
        </form>
		        	
    </div>
	
</body>

</html>
 
