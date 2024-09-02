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
  
  if(isset($_GET['voucher_optional_id']))
    {
	 $_SESSION['voucher_optional_id'] = $_GET['voucher_optional_id'];
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
						
		$this->SetX($left); $this->Cell(0, 20,'OPTIONAL VOUCHER ', 0, 1,'C');				
			
		$this->SetFont("", "", 15);		
		$this->SetX($left); $this->Cell(0, 1, '__________________________________________________________________', 0, 1,'C');
		$this->Ln(10);		
		$this->SetFont("", "", 10);
		
        $pv_id =$_SESSION['id'];	
		$pv_un =$_SESSION['tmp_un'];			
		$pv_doc_prn =$_SESSION['document_print'];
		$pv_opn_dtl =$_SESSION['voucher_optional_id'];
										   	
		#data dari database
		include('dbconnection.php');
		
		$sql_t_rsv_clt = "select * from t_rsv_clt where id='$pv_id'";  
        $rs_result_t_rsv_clt = mysqli_query($conn, $sql_t_rsv_clt);  
        
		$row_t_rsv_clt = mysqli_fetch_assoc($rs_result_t_rsv_clt);
                
		# date
		$pv_vch_date=date('d/m/Y');
			    						
		# invoice no. (otomatis sama dengan b. code)
	    $pv_inv_no=$row_t_rsv_clt["b_code"];
																
		# client name
		$pv_clt_name=$row_t_rsv_clt["client_name"];
		
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
				
		# total pax
		  # adult
		    $pv_pax_adl=$row_t_rsv_clt["pax_adl"]." Adl";
		  
	   	  # child
		    $pv_pax_chd=$row_t_rsv_clt["pax_chd"]." Chd";
		
		  # infant
		    $pv_pax_inf=$row_t_rsv_clt["pax_inf"]." Inf";
			
		  # tl/foc
		    $pv_pax_foc=$row_t_rsv_clt["pax_foc"]." Foc/TL";
				
		  
          $pv_tot_pax=$pv_pax_adl.", ".$pv_pax_chd.", ".$pv_pax_inf.", ".$pv_pax_foc;  		
		
		
		# b. code
  	      $pv_b_code=$row_t_rsv_clt["b_code"];
		
        
		
		// no urut record
		   $pv_opn_dtl_pos=strpos($pv_opn_dtl,'+');		
		   $pv_id_opn_no=substr($pv_opn_dtl,0,$pv_opn_dtl_pos);
		   
		   //$this->Cell(0, 15,'xx : '.$pv_id_rst_hasil, 0, 1,'L');	
		   
		   		    						   		   		                     							 		             
        // code vendor  
		   $pv_opn_dtl_panjang=strlen($pv_opn_dtl);				   
           $pv_id_opn_hasil=substr($pv_opn_dtl,$pv_opn_dtl_pos+1,$pv_opn_dtl_panjang-$pv_opn_dtl_pos);;
		   
		// $this->Cell(0, 15,'yy : '.$pv_id_rst_no, 0, 1,'L');	
		   
		// no voucher
		   $pv_no_voucher=$pv_b_code.'#'.$pv_id_opn_hasil.'/'.$pv_id_opn_no;		
		
        // nama vendor
           $sql_nama_vnd = "SELECT name FROM d_vendor WHERE id='$pv_id_opn_hasil'";  
           $rs_result_nama_vnd = mysqli_query($conn, $sql_nama_vnd);  
           $row_nama_vnd = mysqli_fetch_assoc($rs_result_nama_vnd);
           $pv_vendor_name=$row_nama_vnd["name"];

		
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
			
			$pv_flight_no_arr=$row_t_rsv_flt_arr["flight_no"];
		 
						  		  
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
							  	
		  $this->Ln(85);	
		  
        # header  		
	  	  $right = $this->GetY();			
		  $this->SetY($right-86); 
		  $this->SetX($left+5);
		  $this->Cell(0, 15,'Date : '.$pv_vch_date, 0, 1,'L');	
		 		  		  		  
          $this->Ln(85);	
  		
          $right = $this->GetY();			
		  $this->SetY($right-86); 
		  $this->SetX($left+5);
		  $this->Cell(0, 15,'Voucher No. : '.$pv_no_voucher, 0, 1,'L');	
		  		 
		  $this->SetY($right-86); 
		  $this->SetX($left+390);		
	      $this->Cell(0, 15,'Invoice No. : '.$pv_inv_no, 0, 1,'L');
		  
		  $this->SetFont("", "", 15);		
		  
		  $right = $this->GetY();			
		  $this->SetY($right-7); 
		  $this->SetX($left); $this->Cell(0, 1, '__________________________________________________________________', 0, 1,'C');
	  	  $this->SetFont("", "", 10);
		  $this->Ln(13);		
		  		  
		  $this->Ln(80);	
  		
          $right = $this->GetY();			
		  $this->SetY($right-86); 
		  $this->SetX($left+5);
		  $this->Cell(0, 15,'To : '.$pv_vendor_name, 0, 1,'L');	
		  $this->SetY($right-86); 
		  $this->SetX($left+390);		
	      $this->Cell(0, 15,'In : '.$pv_flight_date_arr.' '.$pv_flight_no_arr, 0, 1,'L');
		  
		  $this->Ln(85);	
  		
		  $right = $this->GetY();			
		  $this->SetY($right-86); 
		  $this->SetX($left+5);
		  $this->Cell(0, 15,'Client Name : '.$pv_clt_name, 0, 1,'L');	
		  		 
		  $this->Ln(85);	
  		
		  $right = $this->GetY();			
		  $this->SetY($right-86); 
		  $this->SetX($left+5);
		  $this->Cell(0, 15,'Total Pax : '.$pv_tot_pax, 0, 1,'L');	
		  $this->SetY($right-86); 
		  $this->SetX($left+390);		
	      $this->Cell(0, 15,'Out : '.$pv_flight_date_dep.' '.$pv_flight_no_dep, 0, 1,'L');
		  		  		
		  $right = $this->GetY();			
		  $this->SetY($right-5); 
		  $this->SetX($left+5);
		  $this->SetFont("", "", 15);		
		  		  		  	
		  $this->SetX($left); $this->Cell(0, 1, '__________________________________________________________________', 0, 1,'C');
	  	  $this->Ln(13);		
		  		  		  				  		
		$h = 18;
		$left = 40;
		$top = 80;	
												          	
		#DETAIL VOUCHER
		
		$this->SetFillColor(255,255,255);	
		$left = $this->GetX();
		$this->SetFont("", "B", 10);
		       
		$this->SetFillColor(200,200,200);	
				
		$this->SetX($left); $this->Cell(535, $h, 'The Holder of The Official Voucher is Entitled For Following Service', 1, 0, 'C',true);			
						
		$this->Ln(18);										
		$this->SetFont('Arial','',9);
		$this->SetWidths(array(535));
		$this->SetAligns(array('C'));
		$no = 1; $this->SetFillColor(255);
					
		$sql_t_rsv_voucher = "select * from t_rsv_cost_of_sales where code_id_rsv='$pv_id' and id='$pv_id_opn_no'";  
        $rs_result_t_rsv_voucher = mysqli_query($conn, $sql_t_rsv_voucher);          
		        		 
		while ($row_t_rsv_voucher = mysqli_fetch_assoc($rs_result_t_rsv_voucher)) { 
		  		         
          $pv_description =$row_t_rsv_voucher['description_voucher'];     
		  		 		  		 		  		  		  			          													            	
		  $this->Row(
	        array(        
	        $pv_description           	  
		  ));
		  
		}
				
		$this->Ln(25);
		
		// sign
		  $this->SetFont("", "", 10);
          
		  $this->SetX($left+220); 
		  $this->Cell(100, $h, 'Sincerly Yours,', 0, 0, 'C',true);		  
		  $this->Ln(50);
		
       // digital sign
		  $this->Image('img/cap.png',245,290,105,45);	
		  $this->Image('img/ttd.png',245,290,105,45);	 
		
		// user sign
		  $this->SetFont("", "U", 10);
          $this->SetX($left+220); 
		  $this->Cell(100, $h, '(       '.'Josuah'.'       )', 0, 0, 'C',true);		  
		  $this->Ln(15);
          $this->SetFont("", "", 10);
		  $this->SetX($left+220);		  
		  $this->Cell(100, $h, 'Managing Director', 0, 0, 'C',true);		  
		  $this->Ln(15);
		
	   // remarks
          $this->SetFillColor(255,255,255);	
		  $left = $this->GetX();
		  $this->SetFont("", "I", 10);
		  
		  $sql_vch_rmk = "SELECT voucher FROM s_invoice_voucher_remarks";  
          $rs_result_vch_rmk = mysqli_query($conn, $sql_vch_rmk);  
          $row_vch_rmk = mysqli_fetch_assoc($rs_result_vch_rmk);
          $pv_vch_rmk=$row_vch_rmk["voucher"];
		  
		       		 	
		  $this->SetX($left); $this->Cell(535, $h,$pv_vch_rmk, 1, 0, 'C',true);			
		
				  		 		  							  		  		 		 			
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
