<?php
require_once '../../config/Database.php'; 
require_once '../../models/TerlarisModel.php';

header('Content-Type: application/json');

$dari = $_GET['dari'] ?? date('Y-m-01');
$sampai = $_GET['sampai'] ?? date('Y-m-d');
$limit = $_GET['limit'] ?? 10;

$model = new TerlarisModel();
$data = $model->getData($dari, $sampai, $limit);

echo json_encode(['data'=>$data]);
