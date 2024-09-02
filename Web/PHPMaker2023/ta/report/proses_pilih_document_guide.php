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
   
  if(isset($_GET['document_guide']))
     {
	  $_SESSION['document_guide'] = $_GET['document_guide'];
     }	
	 	 
     $pv_jns_doc_prn =$_SESSION['document_guide'];
        
     // guide instruction
	    if ($pv_jns_doc_prn=="doc1_guide")
		{
                 echo '<script type="text/javascript">window.location="../report_tcpdf/test/pdf_guide_instruction.php" </script>';		 		               		  
        }  	
	    
    
	 // guide cash bon
	    if ($pv_jns_doc_prn=="doc2_guide")
		{
                echo '<script type="text/javascript">window.location="../report_tcpdf/test/pdf_guide_cash_bon.php" </script>';		 		 
        }  	
	 
	 // paging/flayer
	    if ($pv_jns_doc_prn=="doc3_guide")
		{
                echo '<script type="text/javascript">window.location="../report_tcpdf/test/pdf_paging.php" </script>';
        }  	
      
     // name list
	    if ($pv_jns_doc_prn=="doc4_guide")
		{
                echo '<script type="text/javascript">window.location="../report_tcpdf/test/pdf_name_list.php" </script>';
        }  	
      	 
?>
  