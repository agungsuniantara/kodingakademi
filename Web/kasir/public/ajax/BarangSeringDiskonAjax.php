<?php
    require_once '../../config/Database.php';
    require_once '../../models/DiskonModel.php';
    
    header('Content-Type: application/json');
    $dari = $_GET['dari'] ?? date('Y-m-01');
    $sampai = $_GET['sampai'] ?? date('Y-m-d');
    
    $model = new DiskonModel();
    $data = $model->getBarangSeringDiskon($dari, $sampai, 10);
    
    echo json_encode(['data' => $data]);
?>