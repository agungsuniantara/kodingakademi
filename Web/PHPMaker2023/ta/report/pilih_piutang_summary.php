

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
              	                          
    
		
?>

	
	 <!--  -->
	<div align="center" class="container jumbotron">
    <!-- membuat form dropdown document print dengan id = form_id -->
        
    
		
		 <form action="pilih_piutang_summary.php" method="GET" id="form_id">
		 		  				            
			    <div class="col-lg-4 col-lg-offset-4">
	
				<div class="row">
				
                <div>
				<label for="exampleInputEmail1">Buyer</label>
				</div>
                <!-- gunakan event onchange untuk mengirim data secara otomatis  -->
			
                
                <select class="form-control" name="id_buyer">			 	

                       <!-- <option value="">All</option> 	-->			
                    
					     <?php
							// $pv_blank="";
							//   echo "<option value='".$pv_blank."'>"."SEMUA LEMBAGA"."</option>";
						 
						 echo "<option value='".''."'>".'<< All Buyer >>'."</option>";

                         // query
						    $pv_not_active="0";
							
						    $sql_buyer_instruction ="SELECT * FROM d_buyer WHERE not_active='$pv_not_active'";		        					  						        		        		 
 		                    $rs_result_buyer_instruction = mysqli_query($conn, $sql_buyer_instruction);   
				 
							
					     while ( $d=mysqli_fetch_assoc($rs_result_buyer_instruction)) {
							 
							     $pv_id_buyer=$d['id'];
								 $pv_nm_buyer=$d['name'];
										                        							                                   							
                               echo "<option value='".$d['id']."'>".$pv_nm_buyer."</option>";
							   							  
                            }
					      ?>
					
                </select>
								             
			</div>
         </div>								
											
											
            <div class="col-lg-4 col-lg-offset-4">
																					           		
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
							// $pv_blank="";
							//   echo "<option value='".$pv_blank."'>"."SEMUA LEMBAGA"."</option>";
						 

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
		                 <button type="submit" class="btn btn-primary" formaction="..\report_tcpdf\test\pdf_acc_rekap_piutang.php">PDF</button>		

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
 
