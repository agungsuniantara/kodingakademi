<?php
class BarangModel {
    private $db;
    public function __construct() {
        $this->db = Database::getInstance();
    }
    public function all($search = '') {
        if ($search) {
            $stmt = $this->db->prepare("SELECT * FROM barang WHERE nama_barang LIKE ? OR kategori LIKE ? ORDER BY id_barang DESC");
            $stmt->execute(['%' . $search . '%', '%' . $search . '%']);
        } else {
            $stmt = $this->db->query("SELECT * FROM barang ORDER BY id_barang DESC");
        }
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }
    
    public function find($id) {
        $stmt = $this->db->prepare("SELECT * FROM barang WHERE id_barang = ?");
        $stmt->execute([$id]);
        return $stmt->fetch(PDO::FETCH_ASSOC);
    }
    public function create($data) {
        $stmt = $this->db->prepare("INSERT INTO barang (nama_barang, harga_beli, harga_jual, stok, kategori, created_at, updated_at) VALUES (?, ?, ?, ?, ?, NOW(), NOW())");
        return $stmt->execute([
            $data['nama_barang'], $data['harga_beli'], $data['harga_jual'],
            $data['stok'], $data['kategori']
        ]);
    }
    public function update($id, $data) {
        $stmt = $this->db->prepare("UPDATE barang SET nama_barang=?, harga_beli=?, harga_jual=?, stok=?, kategori=?, updated_at=NOW() WHERE id_barang=?");
        return $stmt->execute([
            $data['nama_barang'], $data['harga_beli'], $data['harga_jual'],
            $data['stok'], $data['kategori'], $id
        ]);
    }
    public function delete($id) {
        $stmt = $this->db->prepare("DELETE FROM barang WHERE id_barang = ?");
        return $stmt->execute([$id]);
    }

    // BarangModel.php
    public function getArrayIdNama() {
        $stmt = $this->db->query("SELECT id_barang, nama_barang FROM barang");
        $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
        $map = [];
        foreach ($result as $row) {
            $map[$row['id_barang']] = $row['nama_barang'];
        }
        return $map;
    }

}
