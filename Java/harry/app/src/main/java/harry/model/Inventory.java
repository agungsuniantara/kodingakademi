package harry.model;

import java.util.ArrayList;
import java.util.List;

public class Inventory {
    public List<String> data = new ArrayList<>();

    // Menambahkan tanaman ke dalam inventory
    public void tambah(String plant) {
        try {
            data.add(plant.toLowerCase());
        } catch (Exception e) {
            System.out.println("Gagal menambahkan tanaman: " + e.getMessage());
        }
    }

    // Memilih tanaman dari inventory
    public String pilihTanaman(String nama) {
        try {
            data.remove(nama.toLowerCase());
        } catch (Exception e) {
            System.out.println("Gagal memilih tanaman: " + e.getMessage());
        }
        return nama;
    }

    // Menukar posisi tanaman dalam inventory
    public void tukarPosisi(int index1, int index2) {
        try {
            if (index1 >= 0 && index1 < data.size() && index2 >= 0 && index2 < data.size() && index1 != index2) {
                String temp = data.get(index1);
                data.set(index1, data.get(index2));
                data.set(index2, temp);
            }
        } catch (Exception e) {
            System.out.println("Gagal menukar posisi tanaman: " + e.getMessage());
        }
    }

    // Menghapus tanaman dari inventory
    public void hapusTanaman(String index) {
        try {
            for (String array : data){
                if (array.equalsIgnoreCase(index)){
                    data.remove(index);
                    break;
                }
            }
        } catch (Exception e) {
            System.out.println("Gagal menghapus tanaman: " + e.getMessage());
        }
    }

    // Menampilkan semua tanaman dalam inventory
    public void tampilkanInventory() {
        try {
            for (int i = 0; i < data.size(); i++) {
                System.out.println((i + 1) + ". " + data.get(i));
            }
        } catch (Exception e) {
            System.out.println("Gagal menampilkan inventory: " + e.getMessage());
        }
    }
}
