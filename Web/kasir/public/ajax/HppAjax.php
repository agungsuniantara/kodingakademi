<?php
require_once '../../config/Database.php'; 
require_once '../../models/HppModel.php';

header('Content-Type: application/json');
$dari = $_GET['dari'] ?? date('Y-m-01');
$sampai = $_GET['sampai'] ?? date('Y-m-d');
$model = new HppModel();
$data = $model->getData($dari, $sampai);
echo json_encode($data);
