<?php
require_once '../../config/Database.php'; 
require_once '../../models/BarangModel.php';
$barang = new BarangModel();

header('Content-Type: application/json');

switch ($_REQUEST['action'] ?? '') {
    case 'list':
        $search = $_GET['search'] ?? '';
        $data = $barang->all($search);
        echo json_encode(['status'=>'success', 'data'=>$data]);
        break;
    case 'get':
        $id = $_GET['id_barang'] ?? 0;
        $data = $barang->find($id);
        echo json_encode(['status'=>'success', 'data'=>$data]);
        break;
    case 'create':
        $result = $barang->create($_POST);
        echo json_encode(['status'=> $result ? 'success' : 'error']);
        break;
    case 'edit':
        $result = $barang->update($_POST['id_barang'], $_POST);
        echo json_encode(['status'=> $result ? 'success' : 'error']);
        break;
    case 'delete':
        $result = $barang->delete($_POST['id_barang']);
        echo json_encode(['status'=> $result ? 'success' : 'error']);
        break;
    default:
        echo json_encode(['status'=>'error','message'=>'Invalid action']);
}
