<?php

require_once("fpdf/fpdf/fpdf.php");


$pdf=new fpdf(); 
$pdf->AddPage();
$pdf->addFont('cid0ct','','cid0ct.php');
$pdf->SetFont('cid0ct','',45);
$pdf->Cell(0,60,'Tutor Joes');
$pdf->Output();

?>