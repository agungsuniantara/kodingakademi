<?php
    require_once '../../config/Database.php'; 
    require_once '../../models/TidaklakuModel.php';
    header('Content-Type: application/json');
    
    $dari = $_GET['dari'] ?? date('Y-m-01');
    $sampai = $_GET['sampai'] ?? date('Y-m-d');
    $model = new TidakLakuModel();
    $data = $model->getData($dari, $sampai);
    
    echo json_encode(['data' => $data]);    
?>