<?php
class TransaksiModel {
    private $db;

    public function __construct() {
        $this->db = Database::getInstance();
    }

    public function getList($from, $to, $minTotal = 0) {
        $stmt = $this->db->prepare(
            "SELECT t.*, 
                (SELECT SUM(quantity) FROM detail_transaksi d WHERE d.id_transaksi = t.id_transaksi) AS total_item,
                (SELECT SUM(subtotal) FROM detail_transaksi d WHERE d.id_transaksi = t.id_transaksi) AS subtotal,
                (SELECT SUM(diskon_item) FROM detail_transaksi d WHERE d.id_transaksi = t.id_transaksi) AS diskon
            FROM transaksi t
            WHERE t.tanggal_transaksi BETWEEN ? AND ?
              AND t.total_harga >= ?
            ORDER BY t.tanggal_transaksi DESC"
        );        
        $stmt->execute([$from, $to, $minTotal]);
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }
    

    public function getSummary($from, $to, $minTotal = 0) {
        $stmt = $this->db->prepare(
            "SELECT 
                COUNT(*) AS total_transaksi,
                COALESCE(SUM(total_harga), 0) AS total_pendapatan,
                COALESCE(AVG(total_harga), 0) AS rata2,
                COALESCE(SUM(diskon), 0) AS total_diskon
            FROM transaksi
            WHERE tanggal_transaksi BETWEEN ? AND ? 
              AND total_harga >= ?"
        );
        $stmt->execute([$from, $to, $minTotal]);
        return $stmt->fetch(PDO::FETCH_ASSOC);
    }

    public function find($id) {
        $stmt = $this->db->prepare("SELECT * FROM transaksi WHERE id_transaksi = ?");
        $stmt->execute([$id]);
        $row = $stmt->fetch(PDO::FETCH_ASSOC);
    
        if ($row) {
            // Ambil detail transaksi
            $stmtDetail = $this->db->prepare("SELECT * FROM detail_transaksi WHERE id_transaksi = ?");
            $stmtDetail->execute([$id]);
            $row['detail'] = $stmtDetail->fetchAll(PDO::FETCH_ASSOC);
        }
    
        return $row;
    }
    

    public function create($data) {
        $stmt = $this->db->prepare(
            "INSERT INTO transaksi (tanggal_transaksi, total_harga, diskon, created_at)
             VALUES (?, ?, ?, NOW())"
        );
        $diskon = isset($data['diskon']) ? $data['diskon'] : 0;
        $simpan = $stmt->execute([
            $data['tanggal_transaksi'],
            $data['total_harga'],
            $diskon
        ]);
        if (!$simpan) return false;
        $id_transaksi = $this->db->lastInsertId();
    
        // Cek & insert detail
        if (!empty($data['detail'])) {
            $detail_list = json_decode($data['detail'], true);
            $stmtDet = $this->db->prepare(
                "INSERT INTO detail_transaksi (id_transaksi, id_barang, quantity, harga_satuan, subtotal, diskon_item)
                 VALUES (?, ?, ?, ?, ?, ?)"
            );
            foreach ($detail_list as $det) {
                $stmtDet->execute([
                    $id_transaksi,
                    $det['id_barang'],
                    $det['quantity'],
                    $det['harga_satuan'],
                    $det['subtotal'],
                    $det['diskon_item']
                ]);
            }
        }
        return true;
    }

    public function update($id, $data) {
        // Update data utama transaksi
        $stmt = $this->db->prepare(
            "UPDATE transaksi SET tanggal_transaksi=?, total_harga=?, diskon=? WHERE id_transaksi=?"
        );
        $diskon = isset($data['diskon']) ? $data['diskon'] : 0;
        $res = $stmt->execute([
            $data['tanggal_transaksi'],
            $data['total_harga'],
            $diskon,
            $id
        ]);
    
        // Hapus semua detail transaksi lama
        $stmtDel = $this->db->prepare("DELETE FROM detail_transaksi WHERE id_transaksi=?");
        $stmtDel->execute([$id]);
    
        // Insert detail baru (jika ada)
        if (!empty($data['detail'])) {
            $detail_list = json_decode($data['detail'], true);
            $stmtDet = $this->db->prepare(
                "INSERT INTO detail_transaksi (id_transaksi, id_barang, quantity, harga_satuan, subtotal, diskon_item)
                 VALUES (?, ?, ?, ?, ?, ?)"
            );
            foreach ($detail_list as $det) {
                $stmtDet->execute([
                    $id,
                    $det['id_barang'],
                    $det['quantity'],
                    $det['harga_satuan'],
                    $det['subtotal'],
                    $det['diskon_item']
                ]);
            }
        }
    
        return $res;
    }
    
    public function delete($id) {
        $stmt = $this->db->prepare("DELETE FROM transaksi WHERE id_transaksi=?");
        return $stmt->execute([$id]);
    }
}
