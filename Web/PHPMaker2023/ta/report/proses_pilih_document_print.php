<?php   
  session_start(); //memulai session
  
  if(isset($_GET['id']))
     {
	  $_SESSION['id'] = $_GET['id'];
     }	 
   
  if(isset($_GET['tmp_un']))
     {
	  $_SESSION['tmp_un'] = $_GET['tmp_un'];
     }	
   
  if(isset($_GET['document_print']))
     {
	  $_SESSION['document_print'] = $_GET['document_print'];
     }	
	 	 
     $pv_jns_doc_prn =$_SESSION['document_print'];
        
     // jika fc
	    if ($pv_jns_doc_prn=="doc1")
		{
            //   echo '<script type="text/javascript">window.location="pdf_final_confirmation.php" </script>';		 		 
                 echo '<script type="text/javascript">window.location="../report_tcpdf/test/pdf_final_confirmation.php" </script>';		 		 
              		   
        }  	
	    
    
	 // jika cost of sales
	    if ($pv_jns_doc_prn=="doc2")
		{
             // echo '<script type="text/javascript">window.location="pdf_cost_of_sales.php" </script>';		 		 
			    echo '<script type="text/javascript">window.location="../report_tcpdf/test/pdf_cost_of_sales.php" </script>';		 		 
        }  	
	 
	 // jika profit/loss
	    if ($pv_jns_doc_prn=="doc3")
		{
           // echo '<script type="text/javascript">window.location="pdf_invoice.php" </script>';		 		 
		   echo '<script type="text/javascript">window.location="../report_tcpdf/test/pdf_profit_loss.php" </script>';
        }  	
	 	 	 				 
?>
  