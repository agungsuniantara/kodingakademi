<?php

session_start(); //memulai session

  if(isset($_GET['tgl_01']))
     {
	  $_SESSION['tgl_01'] = $_GET['tgl_01'];
     }	

  
  if(isset($_GET['tgl_02']))
     {
	  $_SESSION['tgl_02'] = $_GET['tgl_02'];
     }	

  
  if(isset($_GET['status_id']))
    {
	 $_SESSION['status_id'] = $_GET['status_id'];
    }	
  
                        
error_reporting(0);

require_once("fpdf/fpdf/fpdf.php");

class FPDF_AutoWrapTable extends FPDF {
  	private $data = array();
  	private $options = array(
  		'filename' => '',
  		'destinationfile' => '',
  		'paper_size'=>'A4',
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
		//header
		$this->Image('img/lambang.png',60,28,60,60);		
		$this->SetFont("", "B", 15);
		$this->SetX($left); $this->Cell(0, 20, 'PT. CREATION INDONESIA TOUR & TRAVEL', 0, 1,'C');
		$this->SetFont("", "", 9);
		$this->SetX($left); $this->Cell(0, 10, 'Address  : Jl. Pulau Singkep No. 3, Kecamatan Pedungan, Denpasar Selatan-Bali', 0, 1,'C');
		$this->SetX($left); $this->Cell(0, 10, 'E-Mail   : info@creationtourandmice.com | joshua@creationtourandmice.com', 0, 1,'C');
		$this->SetX($left); $this->Cell(0, 10, 'Phone/WA : +62 812-3902-6772 / +62 88-7355-4087', 0, 1,'C');
		$this->SetX($left); $this->Cell(0, 10, 'Website  : http://www.creationtourandmice.com', 0, 1,'C');
	    $this->SetX($left); $this->Cell(0, 1, '__________________________________________________________________', 0, 1,'C');
		$this->Ln(10);					
		$this->SetFont("", "B", 12);							
		$this->SetX($left); $this->Cell(0, 20,'GENERAL JOURNAL REPORT', 0, 1,'C');										
			
		$this->SetFont("", "", 10);
		                  
		$pv_tgl_01=$_SESSION['tgl_01'];	
		$pv_tgl_02=$_SESSION['tgl_02'];			
		$pv_status_id =$_SESSION['status_id'];	
						    
        #data dari database
		include('dbconnection.php');
						  				
		$pv_filter=$pv_tgl_01.' to '.$pv_tgl_02;
					
		$this->SetX($left-10); $this->Cell(0, 20,'Period : '.$pv_filter, 0, 1,'L');										
				                  
        #summary		
		$this->SetFont("", "BI", 9);
		$this->SetFillColor(200,200,200);
		$h = 18;
        $left = 10;		
		$this->SetX($left); $this->Cell(52, $h, 'Date', 1, 0, 'C',true);
		$this->SetX($left += 52); $this->Cell(100, $h, 'Ref. No.', 1, 0, 'C',true);			
		$this->SetX($left += 100); $this->Cell(100, $h, 'T. Category', 1, 0, 'C',true);
		$this->SetX($left += 100); $this->Cell(175, $h, 'Description', 1, 0, 'C',true);
		$this->Ln(18);
		
		$left=25;
        $this->SetFont("", "B", 9);
		$this->SetX($left); $this->Cell(70, $h, 'Account ID', 1, 0, 'C',true);
		$this->SetX($left += 70); $this->Cell(150, $h, 'Account Name', 1, 0, 'C',true);
		$this->SetX($left += 150); $this->Cell(185, $h, 'Description', 1, 0, 'C',true);
		$this->SetX($left += 185); $this->Cell(75, $h, 'Debit', 1, 0, 'C',true);
		$this->SetX($left += 75); $this->Cell(75, $h, 'Credit', 1, 0, 'C',true);
		$this->Ln(18);														
        						
		# 
		  $pv_hri = substr($pv_tgl_01,0,2);
          $pv_bln = substr($pv_tgl_01,3,2);
          $pv_thn = substr($pv_tgl_01,6,4);		
	  	  $pv_tgl_01=$pv_thn.'-'.$pv_bln.'-'.$pv_hri;
		
		  $pv_hri = substr($pv_tgl_02,0,2);
          $pv_bln = substr($pv_tgl_02,3,2);
          $pv_thn = substr($pv_tgl_02,6,4);		
	 	  $pv_tgl_02=$pv_thn.'-'.$pv_bln.'-'.$pv_hri;
		         		
		# t_jurnal_umum	               	
		      $sql_jrl_umum_01 = "SELECT * FROM t_jurnal_umum";
			  $sql_jrl_umum_02=  " WHERE tanggal BETWEEN '$pv_tgl_01' AND '$pv_tgl_02'  order by tanggal";  
              $sql_jrl_umum=$sql_jrl_umum_01.$sql_jrl_umum_02;
			  
			  $rs_result_jrl_umum = mysqli_query($conn, $sql_jrl_umum);  
        		   				   
		# detail italic
          $this->SetFont("", "I", 9);
		  
		  while ($row_jrl_umum = mysqli_fetch_assoc($rs_result_jrl_umum)) { 
		          
			  // jurnal umum
			     $pv_id=$row_jrl_umum["id"];				  
			     
				 $pv_tgl_ju=$row_jrl_umum["tanggal"];	
                 $pv_thn = substr($pv_tgl_ju,0,4);
                 $pv_bln = substr($pv_tgl_ju,5,2);
                 $pv_hri = substr($pv_tgl_ju,8,2);
                 $pv_tanggal = $pv_hri.'-'.$pv_bln.'-'.$pv_thn;

				 
				 $pv_no_bukti=$row_jrl_umum["no_bukti"];				  
				 $pv_kode_jns_trn=$row_jrl_umum["kode_jns_trn"];	
				 $pv_keterangan=$row_jrl_umum["keterangan"];
              
			  // jenis transaksi
			     $sql_jenis_trn = "SELECT jenis_trn FROM d_jenis_trn WHERE id='$pv_kode_jns_trn'";  
                 $rs_result_jenis_trn = mysqli_query($conn, $sql_jenis_trn);  
                 $row_jenis_trn = mysqli_fetch_assoc($rs_result_jenis_trn);
                 $pv_nama_jns_trn=$row_jenis_trn["jenis_trn"];
		  			  			 
              // tampilkan record summary			     
			     $this->SetX(10);
				 $this->SetFont('Arial','BI',9);
		         $this->SetWidths(array(52,100,100,175));
		         $this->SetAligns(array('L','L','L','L'));
		         $this->SetFillColor(255);
				 				
				 $this->Row(
	                          array($pv_tanggal,
	                                $pv_no_bukti,
			                        $pv_nama_jns_trn,				        
	                                $pv_keterangan
							        
		                 ));	
               
                // $this->Ln(18);  


              // detail
                        $sql_t_dtl_jrl = "select * from t_djurnal_umum where id_no_bukti='$pv_id'";  
                        $rs_result_t_dtl_jrl = mysqli_query($conn, $sql_t_dtl_jrl);  

                        $pv_total_dtl_dbt=0;
 						$pv_total_dtl_krd=0;
 						
					    						
		                while ($row_t_dtl_jrl = mysqli_fetch_assoc($rs_result_t_dtl_jrl)) { 
		   		 		
		                     # 
		                       $pv_id_kode_prk=$row_t_dtl_jrl['id_kode_prk'];		  		
		                       $sql_kode_prk = "SELECT nama_prk FROM d_perkiraan WHERE id='$pv_id_kode_prk'";  
                               $rs_result_kode_prk = mysqli_query($conn, $sql_kode_prk);  
                               $row_kode_prk = mysqli_fetch_assoc($rs_result_kode_prk);
                               $pv_nama_prk=$row_kode_prk["nama_prk"];
							   
                               $pv_keterangan=$row_t_dtl_jrl['keterangan'];
                               $pv_debet=$row_t_dtl_jrl['jumlah_dbt'];
							   $pv_kredit=$row_t_dtl_jrl['jumlah_krd'];
							   
							   $pv_total_dtl_dbt=$pv_total_dtl_dbt+$pv_debet;
							   $pv_total_dtl_krd=$pv_total_dtl_krd+$pv_kredit;
							    						 													   						
                               // tampilkan record detail
				                  $this->SetX(25);
								  $this->SetFont('Arial','',9);
		                          $this->SetWidths(array(70,150,185,75,75));
		                          $this->SetAligns(array('L','L','L','R','R'));
		                          $this->SetFillColor(255);
								  
								  $this->Row(
	                                  array($pv_kode_prk,
	                                        $pv_nama_prk,
			                                $pv_keterangan,			
											number_format($pv_debet),			
											number_format($pv_kredit)
							        
		                             ));	
               							   
		                } 
                         
						
						// subtotal debet/kredit
						$this->SetX(25);
						$this->SetFont('Arial','BI',9);
		                $this->SetWidths(array(70,150,185,75,75));
		                $this->SetAligns(array('L','L','L','R','R'));
		                $this->SetFillColor(255);
                        						
						$this->Row(
	                                  array('',
	                                        '',
			                                '',			
											number_format($pv_total_dtl_dbt),			
											number_format($pv_total_dtl_krd)
                         											
                        )); 
                        						                   								
		  }
		  		  
		# normal
          $this->SetFont("", "", 9);
						                       		         
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
	   $this->Cell(0,10,"".$_SESSION['tmp_un'].", ".date('d/m/Y h:i:s'), 0, 0, 'R');
   }
   	
	
} //end of class

//pilihan
$options = array(
	'filename' => '', //nama file penyimpanan, kosongkan jika output ke browser
	'destinationfile' => '', //I=inline browser (default), F=local file, D=download
	'paper_size'=>'A4',	//paper size: F4, A3, A4, A5, Letter, Legal
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
