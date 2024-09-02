

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
	
	
	
	
	
	
	 <!--  -->
	<div align="center" class="container jumbotron">
    <!-- membuat form dropdown document print dengan id = form_id -->
        
		
		<form action="pdf_operation_summary.php" method="GET" id="form_id_02">
		

		<div class="col-lg-4 col-lg-offset-4">
	
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
			</div>

			<div class="col-lg-4 col-lg-offset-4">
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
			</div>
			
			
			
			<div class="col-lg-4 col-lg-offset-4">
				<div class="row">
				<label for="exampleInputEmail1">Reservation Status</label>
			</div>
			</div>
			
			
                <div class="col-lg-4 col-lg-offset-4">
				<div class="row">
			
				
				<select class="col-lg-4 col-lg-offset-4" name="status_id">                    
                    
					     <?php
						    $pv_not_active='1';
							$pv_blank="All";
							echo "<option value='".$pv_blank."'>"."All"."</option>";
						 

                         // query
						    $sql_status ="SELECT * FROM s_status WHERE not_active <> '$pv_not_active'";		        					  						        		        		 
 		                    $rs_result_status = mysqli_query($conn, $sql_status);   
				 							
					     while ( $d=mysqli_fetch_assoc($rs_result_status)) {
							 
							    
                                 $pv_status_name=$d["status"];
							   
                                							   
                               echo "<option value='".$d['id']."'>".$pv_status_name."</option>";
							   							  
                            }
					      ?>
					
                </select>
				</div>				          
				
                <!-- gunakan event onchange untuk mengirim data secara otomatis  -->
			
                   
		
		     
           
			
		     <br>
		     <div class="col-lg-4 col-lg-offset-4">
				<div class="row">
     			<button type="submit" class="btn btn-primary">PDF</button>
			   </div>
			 </div>
			   
									
        </form>
		        	
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
 
