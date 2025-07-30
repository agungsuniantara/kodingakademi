<?php
require_once '../../config/Database.php';
require_once '../../models/TransaksiModel.php';

header('Content-Type: application/json');
$transaksi = new TransaksiModel();

$action = $_REQUEST['action'] ?? '';

switch ($action) {
    case 'list':
        // Filter
        $tanggal_dari    = $_GET['tanggal_dari'] ?? date('Y-m-01');
        $tanggal_sampai  = $_GET['tanggal_sampai'] ?? date('Y-m-d');
        $total_min       = $_GET['total_min'] ?? 0;

        // Data transaksi
        $data = $transaksi->getList($tanggal_dari, $tanggal_sampai, $total_min);
        
        // Hitung summary
        $summary = $transaksi->getSummary($tanggal_dari, $tanggal_sampai, $total_min);

        echo json_encode([
            'status'  => 'success',
            'data'    => $data,
            'summary' => $summary
        ]);
        break;

    case 'get':
        $id = $_GET['id_transaksi'] ?? 0;
        $data = $transaksi->find($id);
        if ($data) {
            echo json_encode(['status' => 'success', 'data' => $data]);
        } else {
            echo json_encode(['status' => 'error', 'message' => 'Transaksi tidak ditemukan']);
        }
        break;

    case 'create':
        $result = $transaksi->create($_POST);
        echo json_encode(['status' => $result ? 'success' : 'error']);
        break;

    case 'edit':
        $id = $_POST['id_transaksi'] ?? 0;
        $result = $transaksi->update($id, $_POST);
        echo json_encode(['status' => $result ? 'success' : 'error']);
        break;

    case 'delete':
        $id = $_POST['id_transaksi'] ?? 0;
        $result = $transaksi->delete($id);
        echo json_encode(['status' => $result ? 'success' : 'error']);
        break;

    default:
        echo json_encode(['status' => 'error', 'message' => 'Invalid action']);
        break;
}
