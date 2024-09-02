<?php



  
 
  
                        
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
		
								
	   
		$this->SetFont("", "B", 12);
						
		$this->SetX($left); $this->Cell(0, 20,'LAPORAN STOK AKHIR ', 0, 1,'C');				
			
		$this->SetFont("", "", 15);		
		$this->SetX($left); $this->Cell(0, 1, '__________________________________________________________________', 0, 1,'C');
		$this->Ln(10);		
		$this->SetFont("", "", 10);
		
		
       	
		
		
		#data dari database
		include('dbconnection.php');
		
		$sql_t_rsv_clt = "select * from `stok barang`";  
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
		
		# invoice deadline
	    $pv_inv_deadline=$row_t_rsv_clt["invoice_deadline"];
		$pv_thn = substr($pv_inv_deadline,0,4);
        $pv_bln = substr($pv_inv_deadline,5,2);
        $pv_hri = substr($pv_inv_deadline,8,2);
        $pv_inv_deadline = $pv_hri.'-'.$pv_bln.'-'.$pv_thn;
				
		# invoice no. (otomatis sama dengan b. code)
	    $pv_inv_no=$row_t_rsv_clt["b_code"];
					
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
		
		
		# b. code
	    $pv_b_code=$row_t_rsv_clt["b_code"];
						
		# tax
		$pv_tax=$row_t_rsv_clt["tax"];
		
		# currency
		$pv_currency=$row_t_rsv_clt["currency"];
						  		  				  									
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
					
		  $pv_periode=$pv_flight_date_arr.' to '.$pv_flight_date_dep;   
		
		 
		  
        
		  		  		  		
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
		$this->SetX($left += 23); $this->Cell(100, $h, 'Kode Barang', 1, 0, 'C',true);			
		$this->SetX($left += 100); $this->Cell(300, $h, 'Nama Barang', 1, 0, 'C',true);					
		$this->SetX($left += 300); $this->Cell(100, $h, 'Jumlah Stok', 1, 0, 'C',true);				
		$this->Ln(18);										
		$this->SetFont('Arial','',9);
		$this->SetWidths(array(23,100,300,100));
		$this->SetAligns(array('C','L','C','L'));
		$no = 1; $this->SetFillColor(255);
					
		
		
		$sql_t_rsv_name_list = "select * from `stok barang`";  
        $rs_result_t_rsv_name_list = mysqli_query($conn, $sql_t_rsv_name_list);          
		          			 
		while ($row_t_rsv_name_list = mysqli_fetch_assoc($rs_result_t_rsv_name_list)) { 
		  
          $pv_kode_barang=TRIM($row_t_rsv_name_list['kode_barang']);		  
          $pv_nama_barang =$row_t_rsv_name_list['nama_barang'];    
		  $pv_jumlah_stok =$row_t_rsv_name_list['jumlah_stok'];    
		  
		  
		
		  		  		  		  		  
		  $pv_remarks =$row_t_rsv_name_list['remarks'];     
		  		  		 		  		  		  		  			          													            	
		  $this->Row(
	        array($no++,	        
	        $pv_kode_barang,$pv_nama_barang,
			$pv_jumlah_stok          			            		
		  ));
		  
		}
				
		
		  							  		  		 		 				  
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
