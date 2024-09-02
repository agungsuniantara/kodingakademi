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
										
		$this->SetX($left); $this->Cell(0, 20,'COST OF SALES', 0, 1,'C');					
			
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
        
        
		# invoice date
		$pv_inv_date=$row_t_rsv_clt["invoice_date"];
		$pv_inv_date_query=$pv_inv_date;
		
	    $pv_thn = substr($pv_inv_date,0,4);
        $pv_bln = substr($pv_inv_date,5,2);
        $pv_hri = substr($pv_inv_date,8,2);
        $pv_inv_date = $pv_hri.'-'.$pv_bln.'-'.$pv_thn;
		
		
		# payment 
		$pv_cek_payment=$row_t_rsv_clt["cash_credit"];
	    		
			$pv_payment='Credit';	
		if ($pv_cek_payment=='1')
		{
			$pv_payment='Cash';				
		}
								
		# client name
		$pv_clt_name=$row_t_rsv_clt["client_name"];
		
		# b. code
	    $pv_b_code=$row_t_rsv_clt["b_code"];
		
		
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
		
		
		# invoice no. (otomatis sama dengan b. code)
	    $pv_inv_no=$pv_b_code;
		
		# tax
		$pv_tax=$row_t_rsv_clt["tax"];
		
		# currency
		$pv_currency=$row_t_rsv_clt["currency"];
		
		# convert ke mata uang sesuai record cost of sales		 
		  //$sql_curr_global = "SELECT * FROM s_bookkeeping WHERE '$pv_inv_date' BETWEEN tanggal_dari AND tanggal_smpi AND currency='$pv_currency'";  
         // $sql_curr_global = "SELECT * FROM s_bookkeeping WHERE currency='$pv_currency'";  
          
		  $sql_curr1 = "SELECT * FROM s_bookkeeping WHERE '$pv_inv_date_query'";  
		  $sql_curr2 = " BETWEEN tanggal_dari AND tanggal_smpi AND currency='$pv_currency'";  
		  $sql_curr_global=$sql_curr1.$sql_curr2;
		  
		  $rs_result_curr_global = mysqli_query($conn, $sql_curr_global);  
          $row_curr_global = mysqli_fetch_assoc($rs_result_curr_global);
            
		  $pv_jml_kurs_global=$row_curr_global["jumlah_kurs"];	
		  		  				  											
		# periode
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
			
					
		  $pv_periode=$pv_flight_date_arr.' to '.$pv_flight_date_dep;   
		
		 
		  $this->Ln(85);	
		  
        # header  		
	  	  $right = $this->GetY();			
		  $this->SetY($right-86); 
		  $this->SetX($left+5);
		  $this->Cell(0, 15,'Invoice Date : '.$pv_inv_date, 0, 1,'L');	
		  $this->SetY($right-86); 
		  $this->SetX($left+390);		
	      $this->Cell(0, 15,'B. Code : '.$pv_b_code, 0, 1,'L');
		  
		  		   
		//  $this->SetX($left+5);
		//  $this->SetY($right-90); 
		//  $this->Cell(0, 15,'Payment : '.$pv_payment, 0, 1,'L');	
		//  $this->SetX($left+400);		
	    //  $this->Cell(0, 15,'Invoice No. : '.$pv_inv_no, 0, 1,'L');
		  
          $this->Ln(85);	
  		
          $right = $this->GetY();			
		  $this->SetY($right-86); 
		  $this->SetX($left+5);
		  $this->Cell(0, 15,'Payment : '.$pv_payment, 0, 1,'L');	
		  $this->SetY($right-86); 
		  $this->SetX($left+390);		
	      $this->Cell(0, 15,'Invoice No. : '.$pv_inv_no, 0, 1,'L');
		  
		  $this->Ln(85);	
  		
          $right = $this->GetY();			
		  $this->SetY($right-86); 
		  $this->SetX($left+5);
		  $this->Cell(0, 15,'Client Name : '.$pv_clt_name, 0, 1,'L');	
		  $this->SetY($right-86); 
		  $this->SetX($left+390);		
	      $this->Cell(0, 15,'Period : '.$pv_flight_date_arr.' to '.$pv_flight_date_dep, 0, 1,'L');
		  
		  $right = $this->GetY();			
		  $this->SetY($right-5); 
		  $this->SetX($left+5);
		  $this->SetFont("", "", 15);		
		  
		  $this->SetX($left); $this->Cell(0, 1, '__________________________________________________________________', 0, 1,'C');
	  	  $this->Ln(13);		
		  		  		  		
		  ##
		 
		$h = 18;
		$left = 40;
		$top = 80;	
												          	
		#ITINERARY PLAN
		
		$this->SetFillColor(255,255,255);	
		$left = $this->GetX();
		$this->SetFont("", "B", 10);
		       
		$this->SetFillColor(200,200,200);	
		
		$this->Cell(23,$h,'No',1,0,'L',true);
		$this->SetX($left += 23); $this->Cell(85, $h, 'Vendor Category', 1, 0, 'C',true);	
		$this->SetX($left += 85); $this->Cell(120, $h, 'Vendor Name', 1, 0, 'C',true);
		$this->SetX($left += 120); $this->Cell(200, $h, 'Description', 1, 0, 'C',true);		
        $this->SetX($left += 200); $this->Cell(30, $h, 'Curr.', 1, 0, 'C',true);		
		$this->SetX($left += 30); $this->Cell(80, $h, 'Sub Total', 1, 0, 'C',true);				
		$this->Ln(18);										
		$this->SetFont('Arial','',9);
		$this->SetWidths(array(23,85,120,200,30,80));
		$this->SetAligns(array('C','L','L','L','L','R'));
		$no = 1; $this->SetFillColor(255);
					
		$sql_t_rsv_cost_of_sales = "select * from t_rsv_nett where code_id_rsv='$pv_id'";  
        $rs_result_t_rsv_cost_of_sales = mysqli_query($conn, $sql_t_rsv_cost_of_sales);          
		
          $pv_total=0;	
		  
		while ($row_t_rsv_cost_of_sales = mysqli_fetch_assoc($rs_result_t_rsv_cost_of_sales)) { 
		  
		    
			$pv_code_id_gbg=$row_t_rsv_cost_of_sales['code_id_gbg'];		  
		    $sql_vnd_gabung = "SELECT * FROM d_vendor_gbg WHERE id='$pv_code_id_gbg'";  
            $rs_result_vnd_gabung = mysqli_query($conn, $sql_vnd_gabung);  
            $row_vnd_gabung = mysqli_fetch_assoc($rs_result_vnd_gabung);
            
			$pv_vnd_name=$row_vnd_gabung["name"];	 
		  
		    $pv_code_vnd_category=$row_t_rsv_cost_of_sales['code_vnd_category'];
		  		  		           		  		             		  		  
          
		  $pv_description =$row_t_rsv_cost_of_sales['description'];     
		  
		    $pv_currency_contract =$row_t_rsv_cost_of_sales['currency'];   
		  
		  $pv_sub_total =$row_t_rsv_cost_of_sales['total_price']; 
		  		  		  		  		  		
          //$pv_total=$pv_total+$pv_sub_total;		  
		  		  		  	
		 
          # convert ke mata uang sesuai record cost of sales		 
		    //$sql_curr = "SELECT * FROM s_bookkeeping WHERE '$pv_inv_date' BETWEEN tanggal_dari AND tanggal_smpi AND currency='$pv_currency_contract'";  
            $sql_curr1 = "SELECT * FROM s_bookkeeping WHERE '$pv_inv_date_query'";  
			$sql_curr2 = " BETWEEN tanggal_dari AND tanggal_smpi AND currency='$pv_currency_contract'";  
			$sql_curr=$sql_curr1.$sql_curr2;
			
			            		
			$rs_result_curr = mysqli_query($conn, $sql_curr);  
            $row_curr = mysqli_fetch_assoc($rs_result_curr);
            
			$pv_jml_kurs_record=$row_curr["jumlah_kurs"];	
			
			    $pv_hasil_kurs=$pv_sub_total;
																			
			if ($pv_jml_kurs_global < $pv_jml_kurs_record) {
				$pv_hasil_kurs=$pv_sub_total*$pv_jml_kurs_record;										
			}
			
			if ($pv_jml_kurs_global > $pv_jml_kurs_record) {
				$pv_hasil_kurs=$pv_sub_total/$pv_jml_kurs_global;										
			}
			
			$pv_total=$pv_total+$pv_hasil_kurs;	
			
          											  						
			$sql_vnd_category = "SELECT * FROM s_vendor_category WHERE id='$pv_code_vnd_category'";  
            $rs_result_vnd_category = mysqli_query($conn, $sql_vnd_category);  
            $row_vnd_category = mysqli_fetch_assoc($rs_result_vnd_category);
            
			$pv_vnd_category=$row_vnd_category["vendor_category"];	  
           											
		  $this->Row(
	        array($no++,	        
	        $pv_vnd_category, 
	        $pv_vnd_name, 
            $pv_description,   
            $pv_currency_contract,			
	        number_format($pv_sub_total,2)		  
		  ));
		  
		}
		

		
		// misc.
		$sql_t_msc_cost_of_sales = "select * from t_rsv_msc where code_id_rsv='$pv_id'";  
        $rs_result_t_msc_cost_of_sales = mysqli_query($conn, $sql_t_msc_cost_of_sales);    
		
		while ($row_t_msc_cost_of_sales = mysqli_fetch_assoc($rs_result_t_msc_cost_of_sales)) { 
		
		
		       $pv_description =$row_t_msc_cost_of_sales['description'];     
		  
		       $pv_currency_contract =$row_t_msc_cost_of_sales['currency'];   
		  
		       $pv_sub_total =$row_t_msc_cost_of_sales['total_price']; 
		  		  		  		  		  		          		  		  			
             # convert ke mata uang sesuai record cost of sales		 
		       $sql_curr1 = "SELECT * FROM s_bookkeeping WHERE '$pv_inv_date_query'";  
		   	   $sql_curr2 = " BETWEEN tanggal_dari AND tanggal_smpi AND currency='$pv_currency_contract'";  
			   $sql_curr=$sql_curr1.$sql_curr2;
						            	
			   $rs_result_curr = mysqli_query($conn, $sql_curr);  
               $row_curr = mysqli_fetch_assoc($rs_result_curr);
            
			   $pv_jml_kurs_record=$row_curr["jumlah_kurs"];	
			
			       $pv_hasil_kurs=$pv_sub_total;
																			
			   if ($pv_jml_kurs_global < $pv_jml_kurs_record) {
			  	   $pv_hasil_kurs=$pv_sub_total*$pv_jml_kurs_record;										
			   }
			
			   if ($pv_jml_kurs_global > $pv_jml_kurs_record) {
				   $pv_hasil_kurs=$pv_sub_total/$pv_jml_kurs_global;										
			   }
			
			   $pv_total=$pv_total+$pv_hasil_kurs;	
			          											  								            									
		       $this->Row(
	             array($no++,	        
	             '', 
	             '', 
                 $pv_description,   
                 $pv_currency_contract,			
	             number_format($pv_sub_total,2)		  
		       ));
				       		  		  		 
		}
			
		//////////////////////////////////////////////////////////////////////////////////
		
								
		$this->Ln(5);
		
	   // TOTAL
		  $this->SetFont("", "B", 10);
          $this->SetX($left-120); 
		  $this->Cell(100, $h, 'Balance in : '.$pv_currency, 0, 0, 'C',true);
		  $this->SetX($left-20); 
		  $this->Cell(100, $h,number_format($pv_total,2), 0, 0, 'R',true);		
		  $this->Ln(15);
		 
		 $this->SetFont("", "B", 10);
          $this->SetX($left-123); 
		  $this->Cell(100, $h, 'Tax (%) : ', 0, 0, 'C',true);
		  $this->SetX($left-20); 
		  $this->Cell(100, $h,number_format($pv_tax,2), 0, 0, 'R',true);		
		  $this->Ln(15);
		  
		  $this->SetFont("", "B", 10);
          $this->SetX($left-117); 
		  $this->Cell(100, $h, 'Total : ', 0, 0, 'C',true);
		  $this->SetX($left-20); 
		  
		  $pv_total_bersih=$pv_total+(($pv_tax/100)*$pv_total);
		  
		  $this->Cell(100, $h,number_format($pv_total_bersih,2), 0, 0, 'R',true);		
		  
		 
		  
		
		
	//	$this->Cell(23,$h,'No',1,1,'L',true);
	//	$this->SetX($left += 52); $this->Cell(100, $h, 'Reservation Type', 1, 1, 'C',true);
	//	$this->SetX($left += 52); $this->Cell(230, $h, 'Vendor', 1, 1, 'C',true);
//		$this->SetX($left += 230); $this->Cell(80, $h, 'Description', 1, 1, 'C',true);		
//		$this->SetX($left += 80); $this->Cell(80, $h, 'Currency', 1, 1, 'C',true);		
//		$this->SetX($left += 80); $this->Cell(80, $h, 'Amount', 1, 1, 'C',true);		
        
  //     $this->Ln(85);			

		
	//	$this->SetFont('Arial','',9);
	//	$this->SetWidths(array(23,52,230,80,80,80));
	//	$this->SetAligns(array('C','L','L','L','L','L'));
	//	$no = 1; $this->SetFillColor(255);
		
	//	$this->Ln(18);
		  
		  
		 
		 
		
		  
		  
		   	
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
