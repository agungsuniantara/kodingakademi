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
  		'orientation'=>'L'
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
		$left = 38;
		
		//header
		//header
		$this->Image('img/logo.jpg',200,28,450,80);$this->SetFont("", "B", 15);
		$this->Ln(70);
								
	    $this->SetFont("", "", 15);		
		$this->SetX($left); $this->Cell(0, 1, '__________________________________________________________________', 0, 1,'C');
		$this->SetX($left); $this->Cell(0, 2, '__________________________________________________________________', 0, 1,'C');
		$this->Ln(10);
		$this->Ln(5);
		$this->SetFont("", "B", 12);
		
		$this->SetX($left); $this->Cell(0, 20,'OPERATION SUMMARY REPORT ', 0, 1,'C');				
			
		$this->Ln(10);		
		$this->SetFont("", "", 10);
			
		                  
		$pv_tgl_01=$_SESSION['tgl_01'];	
		$pv_tgl_02=$_SESSION['tgl_02'];			
		$pv_status_id =$_SESSION['status_id'];	
						    
        #data dari database
		include('dbconnection.php');
						  	
		// status filter //////////////////////////////////////////////////////////                       
		       $pv_nama_sts_id='All';
			   
		   if ($pv_status_id != 'All') {
		       $sql_nama_sts_id = "SELECT status FROM s_status WHERE id='$pv_status_id'";  
               $rs_result_nama_sts_id = mysqli_query($conn, $sql_nama_sts_id);  
               $row_nama_sts_id = mysqli_fetch_assoc($rs_result_nama_sts_id);
		       $pv_nama_sts_id=$row_nama_sts_id["status"]; 
		   }		             
        ///////////////////////////////////////////////////////////////////////////		
		
		$pv_filter=$pv_tgl_01.' to '.$pv_tgl_02.'#Status='.$pv_nama_sts_id;
					
		$this->SetX($left-10); $this->Cell(0, 20,'Period : '.$pv_filter, 0, 1,'L');										
				                  
        #summary		
		$this->SetFont("", "B", 9);
		$this->SetFillColor(200,200,200);
		$h = 18;				
		$this->SetX($left-10); $this->Cell(52, $h, 'Arv. Date', 1, 0, 'C',true);
		$this->SetX($left += 42); $this->Cell(40, $h, 'Flt. No.', 1, 0, 'C',true);			
		$this->SetX($left += 40); $this->Cell(30, $h, 'ETA', 1, 0, 'C',true);
		$this->SetX($left += 30); $this->Cell(30, $h, 'PU', 1, 0, 'C',true);
		$this->SetX($left += 30); $this->Cell(52, $h, 'Dep. Date', 1, 0, 'C',true);
		$this->SetX($left += 52); $this->Cell(40, $h, 'Flt. No.', 1, 0, 'C',true);
	    $this->SetX($left += 40); $this->Cell(30, $h, 'ETD', 1, 0, 'C',true);
	    $this->SetX($left += 30); $this->Cell(30, $h, 'PU', 1, 0, 'C',true);
		$this->SetX($left += 30); $this->Cell(80, $h, 'Client Name', 1, 0, 'C',true);
		$this->SetX($left += 80); $this->Cell(30, $h, 'T. Pax', 1, 0, 'C',true);
		$this->SetX($left += 30); $this->Cell(75, $h, 'Desc./Service', 1, 0, 'C',true);
		$this->SetX($left += 75); $this->Cell(65, $h, 'Guide', 1, 0, 'C',true);
		$this->SetX($left += 65); $this->Cell(65, $h, 'Driver', 1, 0, 'C',true);
		$this->SetX($left += 65); $this->Cell(75, $h, 'Hotel', 1, 0, 'C',true);
		$this->SetX($left += 75); $this->Cell(75, $h, 'Enterence', 1, 0, 'C',true);
		$this->SetX($left += 75); $this->Cell(75, $h, 'Remarks', 1, 0, 'C',true);
		$this->SetX($left += 75); $this->Cell(45, $h, 'Status', 1, 0, 'C',true);
																
        $this->SetFont('Arial','',9);
		$this->SetWidths(array(52,40,30,30,52,40,30,30,80,30,75,65,65,75,75,75,45));
		$this->SetAligns(array('L','L','L','L','C','C','C','C','L','L','L','L','C','C','C','C','C'));
		$no = 1; $this->SetFillColor(255);
				
		$this->Ln(18);  
		                      
		$pv_hri = substr($pv_tgl_01,0,2);
        $pv_bln = substr($pv_tgl_01,3,2);
        $pv_thn = substr($pv_tgl_01,6,4);		
		$pv_start_date=$pv_thn.'-'.$pv_bln.'-'.$pv_hri;
		
		$pv_hri = substr($pv_tgl_02,0,2);
        $pv_bln = substr($pv_tgl_02,3,2);
        $pv_thn = substr($pv_tgl_02,6,4);		
		$pv_end_date=$pv_thn.'-'.$pv_bln.'-'.$pv_hri;
					
        $pv_selisih_hari=((strtotime($pv_end_date)-strtotime($pv_start_date))/24/3600);
				
		$pv_prm_rsv_clt='';
		
		if ($pv_status_id != 'All') {
			$pv_prm_rsv_clt=" and code_sts='$pv_status_id'";
		}
		        
		for ($pv_cacah = 0; $pv_cacah <= $pv_selisih_hari; $pv_cacah++) {
			
			//			         
			$pv_tgl_cari=date('Y-m-d', strtotime($pv_start_date. ' + '.$pv_cacah.' days'));
					
			# t_rsv_clt		               	
		      $sql_rsv_clt_01 = "SELECT id,client_name,description,pax_adl,pax_chd,pax_inf,pax_foc,remarks,code_sts FROM t_rsv_clt";
			  $sql_rsv_clt_02=  " WHERE arrival_date='$pv_tgl_cari'".$pv_prm_rsv_clt." order by arrival_date,departure_date";  
              $sql_rsv_clt=$sql_rsv_clt_01.$sql_rsv_clt_02;
			  
			  $rs_result_rsv_clt = mysqli_query($conn, $sql_rsv_clt);  
        		   				   
		      while ($row_rsv_clt = mysqli_fetch_assoc($rs_result_rsv_clt)) { 
		          
				     // client
					    $pv_id=$row_rsv_clt["id"];				  
				        $pv_clt_name=$row_rsv_clt["client_name"];
				        $pv_description=$row_rsv_clt["description"];					 
					    $pv_tot_pax=$row_rsv_clt["pax_adl"]+$row_rsv_clt["pax_chd"]+$row_rsv_clt["pax_inf"]+$row_rsv_clt["pax_foc"];
						$pv_remarks=$row_rsv_clt["remarks"];
											
                     // status                       
		                $pv_code_sts=$row_rsv_clt["code_sts"];
		                $sql_nama_sts = "SELECT status FROM s_status WHERE id='$pv_code_sts'";  
                        $rs_result_nama_sts = mysqli_query($conn, $sql_nama_sts);  
                        $row_nama_sts = mysqli_fetch_assoc($rs_result_nama_sts);
                        $pv_nama_sts=$row_nama_sts["status"];
						
						//$this->SetX($left-100); $this->Cell(0, 20, 'optional  '.$pv_gabung_nama_oth, 0, 1,'C'); 
						
		          	 			  				 
                     // flight
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
		                  $pv_flight_no_arr=$row_t_rsv_flt_arr["flight_no"];
		                  $pv_time_schedule_arr=$row_t_rsv_flt_arr["time_schedule"]; 
                          $pv_flight_pu_arr=$row_t_rsv_flt_arr["pick_up"];	

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
		                  $pv_flight_no_dep=$row_t_rsv_flt_dep["flight_no"];
		                  $pv_time_schedule_dep=$row_t_rsv_flt_dep["time_schedule"];						  
						  $pv_flight_pu_dep=$row_t_rsv_flt_dep["pick_up"];	
                       
					 // guide (dari di detail reservation guide)		  
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
					   
					 // driver
		                $sql_nama_drv = "SELECT nama_drv FROM t_rsv_trn WHERE code_id_rsv='$pv_id' order by tanggal_mulai";  
                        $rs_result_nama_drv = mysqli_query($conn, $sql_nama_drv);  
        		   		
		                $pv_gabung_nama_drv="";
		   
		                while ($row_nama_drv = mysqli_fetch_assoc($rs_result_nama_drv)) { 
		                       $pv_nama_drv=$row_nama_drv["nama_drv"];
				  				 
  		                       $pv_gabung_nama_drv=$pv_gabung_nama_drv.$pv_nama_drv.'+';		  
		                }
		   
		                       $pv_gabung_nama_drv=substr($pv_gabung_nama_drv,0,strlen($pv_gabung_nama_drv)-1);    	
						
					 // hotel
                        $sql_t_rsv_htl = "select * from t_rsv_htl where code_id_rsv='$pv_id' order by tanggal_in";  
                        $rs_result_t_rsv_htl = mysqli_query($conn, $sql_t_rsv_htl);          
					    
						$pv_gabung_nama_htl="";
		                while ($row_t_rsv_htl = mysqli_fetch_assoc($rs_result_t_rsv_htl)) { 
		   		 		
		                     # hotel
		                       $pv_vnd_htl=$row_t_rsv_htl['kode_htl'];		  		
		                       $sql_vnd_htl = "SELECT name FROM d_hotel WHERE id='$pv_vnd_htl'";  
                               $rs_result_vnd_htl = mysqli_query($conn, $sql_vnd_htl);  
                               $row_vnd_htl = mysqli_fetch_assoc($rs_result_vnd_htl);
                               $pv_vnd_htl=$row_vnd_htl["name"];
							   
							   $pv_gabung_nama_htl=$pv_gabung_nama_htl.$pv_vnd_htl.'+';	
		  		  					  		
		                } 
						
						$pv_gabung_nama_htl=substr($pv_gabung_nama_htl,0,strlen($pv_gabung_nama_htl)-1);  
					 
				      
					  // others/enterence fee
                        $sql_t_rsv_oth = "select * from t_rsv_oth where code_id_rsv='$pv_id' order by tanggal_in";  
                        $rs_result_t_rsv_oth = mysqli_query($conn, $sql_t_rsv_oth);          
					    
						$pv_gabung_nama_oth="";
		                while ($row_t_rsv_oth = mysqli_fetch_assoc($rs_result_t_rsv_oth)) { 
		   		 		
		                     # others/enterence fee
		                       $pv_vnd_oth=$row_t_rsv_oth['kode_oth'];		  		
		                       $sql_vnd_oth = "SELECT name FROM d_others WHERE id='$pv_vnd_oth'";  
                               $rs_result_vnd_oth = mysqli_query($conn, $sql_vnd_oth);  
                               $row_vnd_oth = mysqli_fetch_assoc($rs_result_vnd_oth);
                               $pv_vnd_oth=$row_vnd_oth["name"];
							   
							   $pv_gabung_nama_oth=$pv_gabung_nama_oth.$pv_vnd_oth.'+';	
		  		  					  		
		                } 
						
						$pv_gabung_nama_oth=substr($pv_gabung_nama_oth,0,strlen($pv_gabung_nama_oth)-1);  
					


                    // tampilkan record 
					    
					   $this->Row(
	                          array($pv_flight_date_arr,
	                                $pv_flight_no_arr,
			                        $pv_time_schedule_arr,				        
	                                $pv_flight_pu_arr, 
                                    $pv_flight_date_dep,
	                                $pv_flight_no_dep,
			                        $pv_time_schedule_dep,				        
	                                $pv_flight_pu_dep, 
						  	        $pv_clt_name,
									$pv_tot_pax,
									$pv_description,
									$pv_gabung_nama_gde,
									$pv_gabung_nama_drv,
									$pv_gabung_nama_htl,
									$pv_gabung_nama_oth,
									$pv_remarks,
									$pv_nama_sts
							        
		                 ));
						 
						
						 						 															  				    
		      }  // end : t_rsv_clt
		       		   		
			             			 			  		
        } // end : for
		

       

      

		
		
		
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
	'paper_size'=>'F4',	//paper size: F4, A3, A4, A5, Letter, Legal
	'orientation'=>'L' //orientation: P=portrait, L=landscape
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
