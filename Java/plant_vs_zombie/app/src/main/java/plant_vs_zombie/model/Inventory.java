package plant_vs_zombie.model;

import java.util.ArrayList;
import java.util.List;

public class Inventory {
    private List<String> data = new ArrayList<>();

    // Menambahkan tanaman ke dalam inventory
    public void tambah(String tanaman) {
        data.add(tanaman.toLowerCase()); // Menyimpan nama tanaman dalam huruf kecil untuk konsistensi
    }

    // Memilih tanaman dari inventory
    public String pilihTanaman(String nama) {
        // Menghapus tanaman yang dipilih dari inventory
        data.remove(nama.toLowerCase());
        return nama;
    }

    // Menukar posisi tanaman dalam inventory
    public void tukarPosisi(int index1, int index2) {
        if (index1 >= 0 && index1 < data.size() && index2 >= 0 && index2 < data.size() && index1 != index2) {
            String temp = data.get(index1);
            data.set(index1, data.get(index2));
            data.set(index2, temp);
        }
    }

    // Menghapus tanaman dari inventory
    public void hapusTanaman(int index) {
        if (index >= 0 && index < data.size()) {
            data.remove(index);
        }
    }

    // Menampilkan semua tanaman dalam inventory
    public void tampilkanInventory() {
        System.out.println("Inventory:");
        for (int i = 0; i < data.size(); i++) {
            System.out.println((i + 1) + ". " + data.get(i));
        }
    }
}
