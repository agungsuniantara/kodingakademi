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
  
  
# function terbilang



##################### 
  
 
                        
error_reporting(0);

require_once("fpdf/fpdf/fpdf.php");

class FPDF_AutoWrapTable extends FPDF {
  	private $data = array();
  	private $options = array(
  		'filename' => '',
  		'destinationfile' => '',
  		'paper_size'=>'F4',
  		'orientation'=>'P'
  	);
  	
  	function __construct($data = array(), $options = array()) {
    	parent::__construct();
    	$this->data = $data;
    	$this->options = $options;
	}
	
	public function rptDetailData () {
		
		
		
		   			
		//
		$border = 0;
		$this->AddPage();
		$this->SetAutoPageBreak(true,60);
		$this->AliasNbPages();
		$left = 25;
			
		//header
		$this->Image('img/logo.jpg',70,28,450,80);$this->SetFont("", "B", 15);
		$this->Ln(70);
								
	    $this->SetFont("", "", 15);		
		$this->SetX($left); $this->Cell(0, 1, '__________________________________________________________________', 0, 1,'C');
		$this->SetX($left); $this->Cell(0, 2, '__________________________________________________________________', 0, 1,'C');
		$this->Ln(10);
		$this->Ln(5);
		$this->SetFont("", "B", 12);
						
		$this->SetX($left); $this->Cell(0, 20,'FINAL CONFIRMATION/INVOICE ', 0, 1,'C');				
			
		$this->SetFont("", "", 15);		
		$this->SetX($left); $this->Cell(0, 1, '__________________________________________________________________', 0, 1,'C');
		$this->Ln(10);		
		$this->SetFont("", "", 10);
		
					
        $pv_id =$_SESSION['id'];	
		$pv_un =$_SESSION['tmp_un'];			
		$pv_doc_prn =$_SESSION['document_print'];
		
		#data dari database
		include('dbconnection.php');
		
		$sql_t_rsv_clt = "select * from t_rsv_clt where id='$pv_id'";  
        $rs_result_t_rsv_clt = mysqli_query($conn, $sql_t_rsv_clt);  
        
		$row_t_rsv_clt = mysqli_fetch_assoc($rs_result_t_rsv_clt);
        
        # bank account
		$pv_code_bank=$row_t_rsv_clt["code_bank"];
		$sql_bank = "SELECT * FROM s_bank WHERE id='$pv_code_bank'";  
           $rs_result_bank = mysqli_query($conn, $sql_bank);  
           $row_bank = mysqli_fetch_assoc($rs_result_bank);
           $pv_nama_bank=$row_bank["name"];
		   $pv_remarks_bank=$row_bank["remarks"];
		 
		
		
		# agent name
		$pv_code_agt=$row_t_rsv_clt["code_agt"];
		   $sql_nama_agt = "SELECT name,phone,email FROM d_buyer WHERE id='$pv_code_agt'";  
           $rs_result_nama_agt = mysqli_query($conn, $sql_nama_agt);  
           $row_nama_agt = mysqli_fetch_assoc($rs_result_nama_agt);
           $pv_nama_agt=$row_nama_agt["name"];
		   $pv_phone_agt=$row_nama_agt["phone"];
		   $pv_email_agt=$row_nama_agt["email"];
		   
		
		# agent pic
		$pv_agt_att=$row_t_rsv_clt["agt_att"];
		
		# agent b. code
		$pv_agt_bcd=$row_t_rsv_clt["agt_bcd"];
		
		# b. date
		$pv_b_date=$row_t_rsv_clt["b_date"];
	    $pv_thn = substr($pv_b_date,0,4);
        $pv_bln = substr($pv_b_date,5,2);
        $pv_hri = substr($pv_b_date,8,2);
        $pv_b_date = $pv_hri.'-'.$pv_bln.'-'.$pv_thn;
	   
	    # in
		$pv_in=$row_t_rsv_clt["arrival_date"];
	    $pv_thn = substr($pv_in,0,4);
        $pv_bln = substr($pv_in,5,2);
        $pv_hri = substr($pv_in,8,2);
        $pv_in = $pv_hri.'-'.$pv_bln.'-'.$pv_thn;
		
		# out
		$pv_out=$row_t_rsv_clt["departure_date"];
	    $pv_thn = substr($pv_out,0,4);
        $pv_bln = substr($pv_out,5,2);
        $pv_hri = substr($pv_out,8,2);
        $pv_out= $pv_hri.'-'.$pv_bln.'-'.$pv_thn;
										
		# client name
		$pv_clt_name=$row_t_rsv_clt["client_name"];
		
		# total pax
		  # adult
		    $pv_pax_adl=$row_t_rsv_clt["pax_adl"]." Adl";
		  
	   	  # child
		    $pv_pax_chd=$row_t_rsv_clt["pax_chd"]." Chd";
		
		  # infant
		    $pv_pax_inf=$row_t_rsv_clt["pax_inf"]." Inf";
			
		  # tl/foc
		    $pv_pax_foc=$row_t_rsv_clt["pax_foc"]." TL";
				
		  
          $pv_tot_pax=$pv_pax_adl.", ".$pv_pax_chd.", ".$pv_pax_inf.", ".$pv_pax_foc;  		  
		  
	    # description
        $pv_desc=$row_t_rsv_clt["description"];
  		
		# guide (dari di detail reservation guide)		  
		  $sql_kode_gde = "SELECT kode_gde FROM t_rsv_gde WHERE code_id_rsv='$pv_id' order by tanggal_in";  
          $rs_result_kode_gde = mysqli_query($conn, $sql_kode_gde);  
        		   		
		   $pv_gabung_nama_gde="";
		   
		   while ($row_kode_gde = mysqli_fetch_assoc($rs_result_kode_gde)) { 
		          $pv_kode_gde=$row_kode_gde["kode_gde"];
				  				  
				  $sql_nama_gde = "SELECT name FROM d_guide WHERE id='$pv_kode_gde'";  
                  $rs_result_nama_gde = mysqli_query($conn, $sql_nama_gde);  
                  $row_nama_gde = mysqli_fetch_assoc($rs_result_nama_gde);
                  $pv_nama_gde=$row_nama_gde["name"];

  		          $pv_gabung_nama_gde=$pv_gabung_nama_gde.$pv_nama_gde.'+';		  
		   }
		   
		   $pv_gabung_nama_gde=substr($pv_gabung_nama_gde,0,strlen($pv_gabung_nama_gde)-1);    
       	
		# driver
		 $sql_nama_drv = "SELECT nama_drv FROM t_rsv_trn WHERE code_id_rsv='$pv_id' order by tanggal_mulai";  
          $rs_result_nama_drv = mysqli_query($conn, $sql_nama_drv);  
        		   		
		   $pv_gabung_nama_drv="";
		   
		   while ($row_nama_drv = mysqli_fetch_assoc($rs_result_nama_drv)) { 
		   
		          
		   
		   
		          $pv_nama_drv=$row_nama_drv["nama_drv"];
				  				 
  		          $pv_gabung_nama_drv=$pv_gabung_nama_drv.$pv_nama_drv.'+';		  
		   }
		   
		   $pv_gabung_nama_drv=substr($pv_gabung_nama_drv,0,strlen($pv_gabung_nama_drv)-1); 

        # flight 
		  # arrival
		    $pv_arr_dep='1';
		    $sql_t_rsv_flt_arr = "select * from t_rsv_flt where code_id_rsv='$pv_id' and arr_dep='$pv_arr_dep' order by arr_dep,flight_date";  
            $rs_result_t_rsv_flt_arr = mysqli_query($conn, $sql_t_rsv_flt_arr);          
		    $row_t_rsv_flt_arr = mysqli_fetch_assoc($rs_result_t_rsv_flt_arr);
		  
		    $pv_flight_date_arr=$row_t_rsv_flt_arr["flight_date"];
			$pv_thn = substr($pv_flight_date_arr,0,4);
            $pv_bln = substr($pv_flight_date_arr,5,2);
            $pv_hri = substr($pv_flight_date_arr,8,2);
			$pv_flight_date_arr = $pv_hri.'-'.$pv_bln.'-'.$pv_thn;
			
			
			# jika tanggal flight kosong ambil tanggal in reservasi
			  $pv_cek_tgl_flt=$pv_hri.$pv_bln.$pv_thn;
			  
			  if (empty($pv_cek_tgl_flt)) {
				  $pv_flight_date_arr=$pv_in; 				  			
			  }
			
			
            	
		    $pv_flight_no_arr=$row_t_rsv_flt_arr["flight_no"];
		    $pv_time_schedule_arr=$row_t_rsv_flt_arr["time_schedule"];
		    
		  # departure
		    $pv_arr_dep='2';
		    $sql_t_rsv_flt_dep = "select * from t_rsv_flt where code_id_rsv='$pv_id' and arr_dep='$pv_arr_dep' order by arr_dep,flight_date";  
            $rs_result_t_rsv_flt_dep = mysqli_query($conn, $sql_t_rsv_flt_dep);          
		    $row_t_rsv_flt_dep = mysqli_fetch_assoc($rs_result_t_rsv_flt_dep);
		  
		    $pv_flight_date_dep=$row_t_rsv_flt_dep["flight_date"];
			$pv_thn = substr($pv_flight_date_dep,0,4);
            $pv_bln = substr($pv_flight_date_dep,5,2);
            $pv_hri = substr($pv_flight_date_dep,8,2);
            $pv_flight_date_dep = $pv_hri.'-'.$pv_bln.'-'.$pv_thn;
			
			# jika tanggal flight kosong ambil tanggal in reservasi
			  $pv_cek_tgl_flt=$pv_hri.$pv_bln.$pv_thn;
			  
			  if (empty($pv_cek_tgl_flt)) {
				  $pv_flight_date_dep=$pv_out; 				  			
			  }
					
		    $pv_flight_no_dep=$row_t_rsv_flt_dep["flight_no"];
		    $pv_time_schedule_dep=$row_t_rsv_flt_dep["time_schedule"];
		    												            		  		  	
		# booking code
		  $pv_b_code=$row_t_rsv_clt["b_code"];
		
        # currency
		  $pv_currency=$row_t_rsv_clt["currency"];
		
        # tax
          $pv_tax=$row_t_rsv_clt["tax"];
		  		
		 
        # remarks
		  
          $pv_remarks="測試".$row_t_rsv_clt["remarks"];		

		
		$this->SetX($left); $this->Cell(0, 15,'To : '.$pv_nama_agt, 0, 1,'L');	
		
		$right = $this->GetY();			
		$this->SetY($right-15); 
		$this->SetX($left+380);
		$this->Cell(0, 15,'Phone : '.$pv_phone_agt, 0, 1,'L');	
			
		$this->SetX($left); $this->Cell(0, 15,'Attention : '.$pv_agt_att, 0, 1,'L');					
		
		$right = $this->GetY();			
		$this->SetY($right-15); 
		$this->SetX($left+380);
		$this->Cell(0, 15,'E-Mail : '.$pv_email_agt, 0, 1,'L');	
					
		$this->SetX($left); $this->Cell(0, 15,'Ref No. : '.$pv_agt_bcd, 0, 1,'L');
		$this->SetX($left); $this->Cell(0, 15,'B. Date : '.$pv_b_date, 0, 1,'L');
		$this->SetFont("", "", 15);		
		$this->SetX($left); $this->Cell(0, 1, '__________________________________________________________________', 0, 1,'C');
		$this->Ln(10);		
		$this->SetFont("", "", 10);
		
		$this->SetX($left); $this->Cell(0, 15,'To Be Confirmed The Following Details By Both Parties :', 0, 1,'L');
		$this->SetX($left); $this->Cell(0, 15,'Guest/Group Name : '.$pv_clt_name, 0, 1,'L');
		$this->SetX($left); $this->Cell(0, 15,'Total Person (s) : '.$pv_tot_pax, 0, 1,'L');
		$this->SetX($left); $this->Cell(0, 15,'Type of Service (s) : '.$pv_desc, 0, 1,'L');
		$this->SetX($left); $this->Cell(0, 15,'Guide : '.$pv_gabung_nama_gde, 0, 1,'L');
		$this->SetX($left); $this->Cell(0, 15,'Driver : '.$pv_gabung_nama_drv, 0, 1,'L');
		$this->SetX($left); $this->Cell(0, 15,'B. Code : '.$pv_b_code, 0, 1,'L');
		
		$this->SetFont("", "", 15);		
		$this->SetX($left); $this->Cell(0, 1, '__________________________________________________________________', 0, 1,'C');
		$this->Ln(10);		
		$this->SetFont("", "", 10);
				
        $right = $this->GetY();			
		$this->SetY($right-86); 
		$this->SetX($left+275);
		$this->Cell(0, 15,'Arr. Date : '.$pv_flight_date_arr, 0, 1,'L');	
		$this->SetY($right-86); 
		$this->SetX($left+400);		
		$this->Cell(0, 15,'By : '.$pv_flight_no_arr, 0, 1,'L');
        $this->SetY($right-86); 
		$this->SetX($left+475);		
		$this->Cell(0, 15,'ETA : '.$pv_time_schedule_arr, 0, 1,'L');
				
		$right = $this->GetY();			
		$this->SetY($right+30); 
		$this->SetX($left+275);
		$this->Cell(0, 15,'Dep. Date : '.$pv_flight_date_dep, 0, 1,'L');	
        $this->SetY($right+30); 
		$this->SetX($left+400);		
		$this->Cell(0, 15,'By : '.$pv_flight_no_dep, 0, 1,'L');
        $this->SetY($right+30); 
		$this->SetX($left+475);		
		$this->Cell(0, 15,'ETD : '.$pv_time_schedule_dep, 0, 1,'L'); 
					
		$this->Ln(35);
										
		$h = 18;
		$left = 40;
		$top = 80;	
												          	
		#ITINERARY PLAN
		
		$this->SetFillColor(255,255,255);	
		$left = $this->GetX();
		$this->SetFont("", "B", 10);
		$this->Cell(100,$h,'ITINERARY PLAN',1,1,'L',true);	
		       
		$this->SetFillColor(200,200,200);	
		
		$this->Cell(23,$h,'No',1,0,'L',true);
		$this->SetX($left += 23); $this->Cell(52, $h, 'Date', 1, 0, 'C',true);
		$this->SetX($left += 52); $this->Cell(230, $h, 'Land Description', 1, 0, 'C',true);
		$this->SetX($left += 230); $this->Cell(80, $h, 'B\'Fast', 1, 0, 'C',true);		
		$this->SetX($left += 80); $this->Cell(80, $h, 'Lunch', 1, 0, 'C',true);		
		$this->SetX($left += 80); $this->Cell(80, $h, 'Dinner', 1, 0, 'C',true);		
									
		$this->SetFont('Arial','',9);
		$this->SetWidths(array(23,52,230,80,80,80));
		$this->SetAligns(array('C','L','L','L','L','L'));
		$no = 1; $this->SetFillColor(255);
		
		$this->Ln(18);
		
		$sql_t_rsv_la = "select * from t_rsv_la where code_id_rsv='$pv_id' order by tanggal";  
        $rs_result_t_rsv_la = mysqli_query($conn, $sql_t_rsv_la);          
					
		while ($row_t_rsv_la = mysqli_fetch_assoc($rs_result_t_rsv_la)) { 
		  
		  $tgl_trn =$row_t_rsv_la['tanggal'];          
		  $pv_thn = substr($tgl_trn,0,4);
          $pv_bln = substr($tgl_trn,5,2);
          $pv_hri = substr($tgl_trn,8,2);
          $pv_tgl = $pv_hri.'-'.$pv_bln.'-'.$pv_thn;
		  
		  # breakfast (hotel)
		    $pv_vnd_01_htl=$row_t_rsv_la['code_htl_bft'];		  		
		    $sql_vnd_htl_bft = "SELECT name FROM d_hotel WHERE id='$pv_vnd_01_htl'";  
            $rs_result_vnd_htl_bft = mysqli_query($conn, $sql_vnd_htl_bft);  
            $row_vnd_htl_bft = mysqli_fetch_assoc($rs_result_vnd_htl_bft);
            $pv_vnd_bft_01=$row_vnd_htl_bft["name"];
		  
		  # breakfast (restaurant)
		    $pv_vnd_01_rst=$row_t_rsv_la['code_rst_bft'];		  		
		    $sql_vnd_rst_bft = "SELECT name FROM d_restaurant WHERE id='$pv_vnd_01_rst'";  
            $rs_result_vnd_rst_bft = mysqli_query($conn, $sql_vnd_rst_bft);  
            $row_vnd_rst_bft = mysqli_fetch_assoc($rs_result_vnd_rst_bft);          
		    $pv_vnd_bft_02=$row_vnd_rst_bft["name"];
		    
			
			$pv_vnd_bft=$pv_vnd_bft_01.'+'.$pv_vnd_bft_02;
			
				
			if ($pv_vnd_bft_01=='') {
			    $pv_vnd_bft=$pv_vnd_bft_02;	
			}	
			
			if ($pv_vnd_bft_02=='') {
			    $pv_vnd_bft=$pv_vnd_bft_01;	
			}	
			
													           
		  # lunch (hotel)
		    $pv_vnd_02_htl=$row_t_rsv_la['code_htl_lnc'];
		    $sql_vnd_htl_lnc = "SELECT name FROM d_hotel WHERE id='$pv_vnd_02_htl'";  
            $rs_result_vnd_htl_lnc = mysqli_query($conn, $sql_vnd_htl_lnc);  
            $row_vnd_htl_lnc = mysqli_fetch_assoc($rs_result_vnd_htl_lnc);
            $pv_vnd_lnc_01=$row_vnd_htl_lnc["name"];
			
		  # lunch (restaurant)
		    $pv_vnd_02_rst=$row_t_rsv_la['code_rst_lnc'];		  		
		    $sql_vnd_rst_lnc = "SELECT name FROM d_restaurant WHERE id='$pv_vnd_02_rst'";  
            $rs_result_vnd_rst_lnc = mysqli_query($conn, $sql_vnd_rst_lnc);  
            $row_vnd_rst_lnc = mysqli_fetch_assoc($rs_result_vnd_rst_lnc);          
		    $pv_vnd_lnc_02=$row_vnd_rst_lnc["name"];
		    
			
			$pv_vnd_lnc=$pv_vnd_lnc_01.'+'.$pv_vnd_lnc_02;
			
				
			if ($pv_vnd_lnc_01=='') {
			    $pv_vnd_lnc=$pv_vnd_lnc_02;	
			}	
			
			if ($pv_vnd_lnc_02=='') {
			    $pv_vnd_lnc=$pv_vnd_lnc_01;	
			}		
			
		  # dinner (hotel)
		    $pv_vnd_03_htl=$row_t_rsv_la['code_htl_dnr'];
		    $sql_vnd_htl_dnr = "SELECT name FROM d_hotel WHERE id='$pv_vnd_03_htl'";  
            $rs_result_vnd_htl_dnr = mysqli_query($conn, $sql_vnd_htl_dnr);  
            $row_vnd_htl_dnr = mysqli_fetch_assoc($rs_result_vnd_htl_dnr);
            $pv_vnd_dnr_01=$row_vnd_htl_dnr["name"];
			
		  # dinner (restaurant)
		    $pv_vnd_03_rst=$row_t_rsv_la['code_rst_dnr'];		  		
		    $sql_vnd_rst_dnr = "SELECT name FROM d_restaurant WHERE id='$pv_vnd_03_rst'";  
            $rs_result_vnd_rst_dnr = mysqli_query($conn, $sql_vnd_rst_dnr);  
            $row_vnd_rst_dnr = mysqli_fetch_assoc($rs_result_vnd_rst_dnr);          
		    $pv_vnd_dnr_02=$row_vnd_rst_dnr["name"];
		    
			
			$pv_vnd_dnr=$pv_vnd_dnr_01.'+'.$pv_vnd_dnr_02;
			
				
			if ($pv_vnd_dnr_01=='') {
			    $pv_vnd_dnr=$pv_vnd_dnr_02;	
			}	
			
			if ($pv_vnd_dnr_02=='') {
			    $pv_vnd_dnr=$pv_vnd_dnr_01;	
			}			
																		
		  $this->Row(
	        array($no++,
	        $pv_tgl, 
	        $row_t_rsv_la['description'], 
	        $pv_vnd_bft, 
            $pv_vnd_lnc,             		      	       
	        $pv_vnd_dnr
		  
		  ));
		  
		}
				
		$this->Ln(10);
		
		#ACCOMODATION PLAN
		$this->SetFillColor(255,255,255);	
		$left = $this->GetX();
		$this->SetFont("", "B", 10);
		$this->Cell(150,$h,'ACCOMODATION PLAN',1,1,'L',true);	
		
		$no = 1;$this->SetFillColor(200,200,200);
			
		$this->Cell(23,$h,'No',1,0,'L',true);
		$this->SetX($left += 23); $this->Cell(52, $h, 'Date-In', 1, 0, 'C',true);
		$this->SetX($left += 52); $this->Cell(52, $h, 'Date-Out', 1, 0, 'C',true);			
		$this->SetX($left += 52); $this->Cell(190, $h, 'Hotel', 1, 0, 'C',true);
		$this->SetX($left += 190); $this->Cell(80, $h, 'Room Type', 1, 0, 'C',true);
		$this->SetX($left += 80); $this->Cell(37, $h, 'Single', 1, 0, 'C',true);
		$this->SetX($left += 37); $this->Cell(37, $h, 'Double', 1, 0, 'C',true);
	    $this->SetX($left += 37); $this->Cell(37, $h, 'Twin', 1, 0, 'C',true);
	    $this->SetX($left += 37); $this->Cell(37, $h, 'Triple', 1, 0, 'C',true);
		
        $this->SetFont('Arial','',9);
		$this->SetWidths(array(23,52,52,190,80,37,37,37,37));
		$this->SetAligns(array('C','L','L','L','L','C','C','C','C'));
		$no = 1; $this->SetFillColor(255);
		
		$this->Ln(18);
		
		$sql_t_rsv_htl = "select * from t_rsv_htl where code_id_rsv='$pv_id' order by tanggal_in";  
        $rs_result_t_rsv_htl = mysqli_query($conn, $sql_t_rsv_htl);          
					
		while ($row_t_rsv_htl = mysqli_fetch_assoc($rs_result_t_rsv_htl)) { 
		   
		  # tanggal in 
		  $tgl_trn_01 =$row_t_rsv_htl['tanggal_in'];          
		  $pv_thn = substr($tgl_trn_01,0,4);
          $pv_bln = substr($tgl_trn_01,5,2);
          $pv_hri = substr($tgl_trn_01,8,2);
          $pv_tgl_01 = $pv_hri.'-'.$pv_bln.'-'.$pv_thn;
		  
		  # tanggal out
		  $tgl_trn_02 =$row_t_rsv_htl['tanggal_out'];          
		  $pv_thn = substr($tgl_trn_02,0,4);
          $pv_bln = substr($tgl_trn_02,5,2);
          $pv_hri = substr($tgl_trn_02,8,2);
          $pv_tgl_02 = $pv_hri.'-'.$pv_bln.'-'.$pv_thn;
		  
		  # hotel
		    $pv_vnd_htl=$row_t_rsv_htl['kode_htl'];		  		
		    $sql_vnd_htl = "SELECT name FROM d_hotel WHERE id='$pv_vnd_htl'";  
            $rs_result_vnd_htl = mysqli_query($conn, $sql_vnd_htl);  
            $row_vnd_htl = mysqli_fetch_assoc($rs_result_vnd_htl);
            $pv_vnd_htl=$row_vnd_htl["name"];
		  
		  # room type
		    $pv_room_type=$row_t_rsv_htl['code_room_type'];		  		
		    $sql_room_type = "SELECT room_type FROM s_hotel_room_type WHERE id='$pv_room_type'";  
            $rs_result_room_type = mysqli_query($conn, $sql_room_type);  
            $row_room_type = mysqli_fetch_assoc($rs_result_room_type);
            $pv_room_type=$row_room_type["room_type"];
		  
		  # single,double,twin,triple
		    $pv_room_sgl=$row_t_rsv_htl['room_sgl'];
			$pv_room_dbl=$row_t_rsv_htl['room_dbl'];
			$pv_room_twn=$row_t_rsv_htl['room_twn'];
			$pv_room_tpl=$row_t_rsv_htl['room_tpl'];
			
		  
		   $this->Row(
	        array($no++,
	        $pv_tgl_01,
			$pv_tgl_02,				        
	        $pv_vnd_htl, 
            $pv_room_type,
			$pv_room_sgl,
			$pv_room_dbl,
			$pv_room_twn,
			$pv_room_tpl
							        	
		  ));
		   
		}
				
		$this->Ln(10);
				
		#PROFORMA INVOICE
		$this->SetFillColor(255,255,255);	
		$left = $this->GetX();
		$this->SetFont("", "B", 10);
		$this->Cell(150,$h,'PROFORMA INVOICE',1,1,'L',true);	
		
		$no = 1;$this->SetFillColor(200,200,200);
		
		$this->Cell(23,$h,'No',1,0,'L',true);
		$this->SetX($left += 23); $this->Cell(420, $h, 'Description', 1, 0, 'C',true);
		$this->SetX($left += 420); $this->Cell(102, $h, 'Amount Due', 1, 0, 'C',true);			
										
		$this->SetFont('Arial','',9);
		$this->SetWidths(array(23,420,102));
		$this->SetAligns(array('C','L','R'));
		$no = 1; $this->SetFillColor(255);
		
		$this->Ln(18);
		
		$sql_t_rsv_inv = "select * from t_rsv_invoice where code_id_rsv='$pv_id'";  
        $rs_result_t_rsv_inv = mysqli_query($conn, $sql_t_rsv_inv);          
		
        $pv_total=0;
		
		while ($row_t_rsv_inv = mysqli_fetch_assoc($rs_result_t_rsv_inv)) { 
		   		 		
		  # single,double,twin,triple
		    $pv_description=$row_t_rsv_inv['description'];
			$pv_total_selling=$row_t_rsv_inv['total_selling'];
			$pv_total=$pv_total+$pv_total_selling;
		  
		   $this->Row(
	        array($no++,	        
			$pv_description,			
			number_format($pv_total_selling,2)
							       		 
		  ));
		  		  		
		}
		
          $this->Ln(5);  
		// TOTAL
		  $this->SetFont("", "B", 10);
          $this->SetX($left-100); 
		  $this->Cell(100, $h, 'Balance in : '.$pv_currency, 0, 0, 'C',true);
		  $this->SetX($left+2); 
		  $this->Cell(100, $h,number_format($pv_total,2), 0, 0, 'R',true);		
		  $this->Ln(15);
		 
		 $this->SetFont("", "B", 10);
          $this->SetX($left-103); 
		  $this->Cell(100, $h, 'Tax (%) : ', 0, 0, 'C',true);
		  $this->SetX($left+2); 
		  $this->Cell(100, $h,number_format($pv_tax,2), 0, 0, 'R',true);		
		  $this->Ln(15);
		  
		  $this->SetFont("", "B", 10);
          $this->SetX($left-97); 
		  $this->Cell(100, $h, 'Total : ', 0, 0, 'C',true);
		  $this->SetX($left+2); 
		  
		  $pv_total_bersih=$pv_total+(($pv_tax/100)*$pv_total);
		  
		  $this->Cell(100, $h,number_format($pv_total_bersih,2), 0, 0, 'R',true);		
		  
		  $this->Ln(20);
		  		  		  		 
		#PROFORMA INVOICE
	 	
		 $this->SetFillColor(255,255,255);	
		 $left = $this->GetX();
		 $this->SetFont("", "I", 10);
		 
         // terbilang 		 
		 $pv_total_angka="Due : ".number_to_word($pv_total_bersih);
		 $this->MultiCell(545,15,$pv_total_angka,1,'C',true);
		 
         $this->Ln(10);
		 
         $this->SetFont("", "", 10); 		

		// $this->MultiCell(545,15,'Please Send Us Document of Bank Transfer Once You Have Transfer The Above Amount To,',1,'C',true);
		 $this->MultiCell(545,15,'Please Send Us Document of Bank Transfer Once You Have Transfer The Above Amount To, ',1,'C',true);
		 $this->MultiCell(545,15,$pv_remarks_bank,1,'C',true);
		 
		 
		// $this->Cell(545,15,'Please Send Us Document of Bank Transfer Once You Have Transfer The Above Amount To,',1,1,'C',true);						 	 
		// $this->Cell(545,15,'Bank Name : '.$pv_nama_bank.'\r\n'.$pv_remarks_bank,1,1,'C',true);						 	 
		 
		 $this->Ln(5);
		 
		
		 
		 
		
		 
		
		// sign
		  $this->SetFont("", "", 10);
          $this->SetX($left-200); 
		  $this->Cell(100, $h, 'Acceptance by', 0, 0, 'C',true);
		  $this->SetX($left+75); 
		  $this->Cell(100, $h, 'On behalf of Creation Tour & Travel', 0, 0, 'C',true);
		  
		  $this->Ln(50);
		  
		// user sign
		  $this->SetFont("", "", 10);
          $this->SetX($left-200); 
		  $this->Cell(100, $h, '(.......'.$pv_agt_att.'.......)', 0, 0, 'C',true);
		  $this->SetX($left+75); 
		  $this->Cell(100, $h, '(.......'.$pv_un.'.......)', 0, 0, 'C',true);
		  
		   $this->Ln(15);
		
		// date issue
		   $pv_tgl_skrg=date('d/m/Y');
		  $this->SetFont("", "", 10);
          $this->SetX($left-200); 
		  $this->Cell(100, $h, 'To Be Send Back to Creative Tour & Travel', 0, 0, 'C',true);
		  $this->SetX($left+75); 
		  $this->Cell(100, $h, 'Date of Issue : '.$pv_tgl_skrg, 0, 0, 'C',true);
		  
		   $this->Ln(20);
		  
        #remarks
	 	 $this->SetFillColor(255,255,255);	
		 $left = $this->GetX();
		 
		 $this->SetFont("ARIAL", "I", 10);
		 //  $this->SetFont("ARIALUNI", "", 10);
		 
		 $this->MultiCell(545,$h,$pv_remarks,1,'C',true);	
		 
		 $this->Ln(20);
		
		
		//$pv_total_angka=number_to_word($pv_total);
		//$this->MultiCell(545,$h,$pv_total_angka,1,'C',true);	
		
		
		
		 
		 
		// $this->Cell(545,$h,$pv_hasil_huruf,1,'C',true);
		 
		 
		 
			
		# untuk menuliskan nama bulan dengan format Indonesia
		$bln = array(
		  '01' => 'Januari',
		  '02' => 'Februari',
		  '03' => 'Maret',
		  '04' => 'April',
		  '05' => 'Mei',
		  '06' => 'Juni',
		  '07' => 'Juli',
		  '08' => 'Agustus',
		  '09' => 'September',
		  '10' => 'Oktober',
		  '11' => 'November',
		  '12' => 'Desember'
		);

		#tabel footer
//		$this->Ln(20);
//		$this->SetFont("", "", 9);
//		$this->SetX(400); $this->Cell(0, 15, 'Payakumbuh Barat, '.date('d').' '.$bln[date('m')].' '.date('Y').'', 0, 1,'C');
//		$this->SetX(400); $this->Cell(0, 15, 'DIREKTUR', 0, 1,'C');
//		$this->Ln(40);
//		$this->SetX(400); $this->Cell(0, 20, 'ARIE, S.Kom, M.Kom', 0, 1,'C');
	}

	public function printPDF () {
				
		if ($this->options['paper_size'] == "F4") {
			$a = 8.3 * 72; //1 inch = 72 pt
			$b = 13.0 * 72;
			$this->FPDF($this->options['orientation'], "pt", array($a,$b));
		} else {
			$this->FPDF($this->options['orientation'], "pt", $this->options['paper_size']);
		}
		
	    $this->SetAutoPageBreak(false);
	    $this->AliasNbPages();
	    $this->SetFont("helvetica", "B", 10);
	    //$this->AddPage();
	
	    $this->rptDetailData();
			    
	    $this->Output($this->options['filename'],$this->options['destinationfile']);
  	}
	
	
	
	
	
	
  	
  	private $widths;
	private $aligns;

	function SetWidths($w)
	{
		//Set the array of column widths
		$this->widths=$w;
	}

	function SetAligns($a)
	{
		//Set the array of column alignments
		$this->aligns=$a;
	}

	function Row($data)
	{
		//Calculate the height of the row
		$nb=0;
		for($i=0;$i<count($data);$i++)
			$nb=max($nb,$this->NbLines($this->widths[$i],$data[$i]));
		$h=15*$nb;
		//Issue a page break first if needed
		$this->CheckPageBreak($h);
		//Draw the cells of the row
		for($i=0;$i<count($data);$i++)
		{
			$w=$this->widths[$i];
			$a=isset($this->aligns[$i]) ? $this->aligns[$i] : 'L';
			//Save the current position
			$x=$this->GetX();
			$y=$this->GetY();
			//Draw the border
			$this->Rect($x,$y,$w,$h);
			//Print the text
			$this->MultiCell($w,15,$data[$i],0,$a);
			//Put the position to the right of the cell
			$this->SetXY($x+$w,$y);
		}
		//Go to the next line
		$this->Ln($h);
	}

	function CheckPageBreak($h)
	{
		//If the height h would cause an overflow, add a new page immediately
		if($this->GetY()+$h>$this->PageBreakTrigger)
			$this->AddPage($this->CurOrientation);
	}

	function NbLines($w,$txt)
	{
		//Computes the number of lines a MultiCell of width w will take
		$cw=&$this->CurrentFont['cw'];
		if($w==0)
			$w=$this->w-$this->rMargin-$this->x;
		$wmax=($w-2*$this->cMargin)*1000/$this->FontSize;
		$s=str_replace("\r",'',$txt);
		$nb=strlen($s);
		if($nb>0 and $s[$nb-1]=="\n")
			$nb--;
		$sep=-1;
		$i=0;
		$j=0;
		$l=0;
		$nl=1;
		while($i<$nb)
		{
			$c=$s[$i];
			if($c=="\n")
			{
				$i++;
				$sep=-1;
				$j=$i;
				$l=0;
				$nl++;
				continue;
			}
			if($c==' ')
				$sep=$i;
			$l+=$cw[$c];
			if($l>$wmax)
			{
				if($sep==-1)
				{
					if($i==$j)
						$i++;
				}
				else
					$i=$sep+1;
				$sep=-1;
				$j=$i;
				$l=0;
				$nl++;
			}
			else
				$i++;
		}
		return $nl;
	}
	
	function Footer()
   {
        $this->SetY(-10);
        $this->SetFont('Arial', '', 8);
        
	    $this->Cell(0,10,'Page '.$this->PageNo().'/{nb}',0,0,'C');
		
		$this->SetY(-10);
      //  $this->Cell(0,10,"".date('d/m/Y h:i:s'), 0, 0, 'R');
	   $this->Cell(0,10,"".$_SESSION['user_login'].", ".date('d/m/Y h:i:s'), 0, 0, 'R');
   }
   	
	
	
	
} //end of class

//pilihan
$options = array(
	'filename' => '', //nama file penyimpanan, kosongkan jika output ke browser
	'destinationfile' => '', //I=inline browser (default), F=local file, D=download
	'paper_size'=>'F4',	//paper size: F4, A3, A4, A5, Letter, Legal
	'orientation'=>'P' //orientation: P=portrait, L=landscape
);

$tabel = new FPDF_AutoWrapTable($data, $options);
$tabel->printPDF();

# terbilang english
function number_to_word( $num = '' )
{
    $num    = ( string ) ( ( int ) $num );
   
    if( ( int ) ( $num ) && ctype_digit( $num ) )
    {
        $words  = array( );
       
        $num    = str_replace( array( ',' , ' ' ) , '' , trim( $num ) );
       
        $list1  = array('','one','two','three','four','five','six','seven',
            'eight','nine','ten','eleven','twelve','thirteen','fourteen',
            'fifteen','sixteen','seventeen','eighteen','nineteen');
       
        $list2  = array('','ten','twenty','thirty','forty','fifty','sixty',
            'seventy','eighty','ninety','hundred');
       
        $list3  = array('','thousand','million','billion','trillion',
            'quadrillion','quintillion','sextillion','septillion',
            'octillion','nonillion','decillion','undecillion',
            'duodecillion','tredecillion','quattuordecillion',
            'quindecillion','sexdecillion','septendecillion',
            'octodecillion','novemdecillion','vigintillion');
       
        $num_length = strlen( $num );
        $levels = ( int ) ( ( $num_length + 2 ) / 3 );
        $max_length = $levels * 3;
        $num    = substr( '00'.$num , -$max_length );
        $num_levels = str_split( $num , 3 );
       
        foreach( $num_levels as $num_part )
        {
            $levels--;
            $hundreds   = ( int ) ( $num_part / 100 );
            $hundreds   = ( $hundreds ? ' ' . $list1[$hundreds] . ' Hundred' . ( $hundreds == 1 ? '' : 's' ) . ' ' : '' );
            $tens       = ( int ) ( $num_part % 100 );
            $singles    = '';
           
            if( $tens < 20 ) { $tens = ( $tens ? ' ' . $list1[$tens] . ' ' : '' ); } else { $tens = ( int ) ( $tens / 10 ); $tens = ' ' . $list2[$tens] . ' '; $singles = ( int ) ( $num_part % 10 ); $singles = ' ' . $list1[$singles] . ' '; } $words[] = $hundreds . $tens . $singles . ( ( $levels && ( int ) ( $num_part ) ) ? ' ' . $list3[$levels] . ' ' : '' ); } $commas = count( $words ); if( $commas > 1 )
        {
            $commas = $commas - 1;
        }
       
        $words  = implode( ', ' , $words );
       
        $words  = trim( str_replace( ' ,' , ',' , ucwords( $words ) )  , ', ' );
        if( $commas )
        {
            $words  = str_replace( ',' , ' and' , $words );
        }
       
        return $words;
    }
    else if( ! ( ( int ) $num ) )
    {
        return 'Zero';
    }
    return '';
}
##########
	

?>
