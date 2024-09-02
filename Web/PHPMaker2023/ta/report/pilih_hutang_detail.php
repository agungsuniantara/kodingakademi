

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Report</title>
   
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
              	                          
    //jika jurusan sudah diset maka masukkan datanya ke dalam variabel $cari
    if(isset($_GET['id_vendor_category'])){
        $cari = $_GET['id_vendor_category'];

        //ambil data dari database, dimana pencarian sesuai dengan variabel cari
        $data = mysqli_query($conn, "select * from d_vendor_gbg where id_vendor_category = '$cari' order by name");
		
    }else{

        //tapi jika jurusan belum diset, maka jangan tampilkan apapun
        $data = [];		
    }
		
?>

	
	 <!--  -->
	<div align="center" class="container jumbotron">
    <!-- membuat form dropdown document print dengan id = form_id -->
        
    
		
		 <form action="pilih_hutang_detail.php" method="GET" id="form_id">
		 
		  
				            			
            <div class="col-lg-4 col-lg-offset-4">
	
				<div class="row">
                <label for="exampleInputEmail1">Vendor Category</label>
                <!-- gunakan event onchange untuk mengirim data secara otomatis  -->
                
				 <select class="form-control" name="id_vendor_category" onChange="document.getElementById('form_id').submit();">
                   <!-- <option value="">--Pilih Jurusan--</option> -->
                    <option <?php 
					           if(!empty($cari))
							     { 
							       echo $cari == '1' ? 'selected':''; 								   								  								   								
							     } 
							?> 
							value="1">Airline
				     </option>
                    
					 <option <?php 
					           if(!empty($cari))
							     { 
							       echo $cari == '2' ? 'selected':''; 
								   
							     } 
							?> 
							value="2">Hotel
				     </option>
					 
					 <option <?php 
					           if(!empty($cari))
							     { 
							       echo $cari == '3' ? 'selected':''; 
								   
							     } 
							?> 
							value="3">Restaurant
				     </option>
					 
					 <option <?php 
					           if(!empty($cari))
							     { 
							       echo $cari == '4' ? 'selected':''; 
								   
							     } 
							?> 
							value="4">Guide
				     </option>
					 
					 <option <?php 
					           if(!empty($cari))
							     { 
							       echo $cari == '5' ? 'selected':''; 
								   
							     } 
							?>
							value="5">Activity
				     </option>
					 
					 <option <?php 
					           if(!empty($cari))
							     { 
							       echo $cari == '6' ? 'selected':''; 
								   
							     } 
							?> 
							value="6">Transport
				     </option>
					 
					 <option <?php 
					           if(!empty($cari))
							     { 
							       echo $cari == '7' ? 'selected':''; 
								   
							     } 
							  ?>
							value="7">Enterance 
				     </option>
					 
					 					 					 					                      	
                </select>
            
			
			</div>
			
			<label for="exampleInputEmail1"></label>
			
							
           <div class="row">
                <label for="exampleInputPassword1">Vendor Name</label>
                <select class="form-control" name="id_vendor">
                  <!--  <option value="">--Pilih Mahasiswa--</option> -->
                    <!-- data ditampilkan berdasarkan jurusan yang dipilih
                    untuk logikanya ada pada line 24 hingga 33 -->
					
					
                    <?php 
					
					echo "<option value='".''."'>".'<< All Vendor >>'."</option>";
					
					
					while($d = mysqli_fetch_array($data)){ ?>
                        
						
						<?php
						echo "<option value='".$d['id_vendor']."'>".$d['name']."</option>";
						?>
						
                    <?php } ?>
                </select>
            </div>
			
			
			<label for="exampleInputEmail1"></label>
	
				<div class="row">
				
					<div class="form-group">
						<label class="control-label"><small>Dari Tgl : </small></label>
						<div class='input-group date' id='dtp_default1'>
							<input type="text"  class="form-control" id="input_dtp_default1" name="tgl_01" />
							<span class="input-group-addon">
		                        <span class="glyphicon glyphicon-calendar"></span>
		                    </span>
						</div>
				
				</div>
				</div>
				
				
				<div class="row">

				
					<div class="form-group">
						<label class="control-label"><small>Sampai Tgl : </small></label>
                		<div class='input-group date' id='dtp_default2'>
							<input type="text" class="form-control" id="input_dtp_default2" name="tgl_02" />
							<span class="input-group-addon">
		                        <span class="glyphicon glyphicon-calendar"></span>
		                    </span>
						</div>
				
				</div>
				
				
				
				
				
				

				</div>
												
             <div class="col-lg-4 col-lg-offset-4">
	
				<div class="row">
				
                <div>
				<label for="exampleInputEmail1">Currency</label>
				</div>
                <!-- gunakan event onchange untuk mengirim data secara otomatis  -->
			
                
                <select class="form-control" name="id_currency">			 	

                       <!-- <option value="">All</option> 	-->			
                    
					     <?php
							 $pv_blank="";
							   echo "<option value='".$pv_blank."'>"."ALL"."</option>";
						 

                         // query
						    $pv_not_active="0";
							
						    $sql_currency_instruction ="SELECT currency FROM s_regional_country WHERE not_active='$pv_not_active'";		        					  						        		        		 
 		                    $rs_result_currency_instruction = mysqli_query($conn, $sql_currency_instruction);   
				 
							
					     while ( $d=mysqli_fetch_assoc($rs_result_currency_instruction)) {
							 
							    
								 $pv_nm_curr=$d['currency'];
										                        							                                   							
                               echo "<option value='".$d['currency']."'>".$pv_nm_curr."</option>";
							   							  
                            }
					      ?>
					
                </select>
								             
			</div>
</div>

           
		   	 
                
				
			 <div class="col-lg-4 col-lg-offset-4">	
	            <div class="row">
				 <label for="exampleInputEmail1"></label>
				                		
					<div class="form-group">
		                 <button type="submit" class="btn btn-primary" formaction="..\report_tcpdf\test\pdf_acc_detail_hutang.php">PDF</button>		

                     </div>
				

				</div>		
				
			</div>	
			 
			
			 
			 
			
			
        </form>
		
				
    </div>





</div>	
	
	<!-- js untuk jquery -->
	<script src="js/jquery-1.11.2.min.js"></script>
	<!-- js untuk bootstrap -->
	<script src="js/bootstrap.js"></script>
	<!-- js untuk moment -->
	<script src="js/moment.js"></script>
	<!-- js untuk bootstrap datetimepicker -->
	<script src="js/bootstrap-datetimepicker.min.js"></script>

	<script type="text/javascript">
		$(document).ready(function(){
              
              var date = new Date();
              var firstDay = new Date(date.getFullYear(), date.getMonth(), 1);
              var lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0);
			  
			 $('#dtp_default1').datetimepicker({
			 	format : 'DD/MM/YYYY',
				defaultDate:firstDay
			 });

			 $('#dtp_default2').datetimepicker({
			 	format : 'DD/MM/YYYY',
				defaultDate:lastDay
			 
			 });
			               			
			 $('#dtp_default1').data("DateTimePicker").date();

		});
	</script>
	
	
</body>

</html>
 
