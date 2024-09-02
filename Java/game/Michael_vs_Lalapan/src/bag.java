import java.util.ArrayList;

class Inventory {
    private ArrayList<String> data = new ArrayList<>();

    public void tambah(String tanaman) {
        data.add(tanaman);
    }

    // Memilih tanaman dalam Inventory
    // public boolean pilihTanaman(String nama) {
    //     return data.remove(nama.toLowerCase()); 
    // }

    // Menukar posisi tanaman dalam Inventory
    public void tukarPosisi(int index1, int index2) {
        String temp = data.get(index1);
        data.set(index1, data.get(index2));
        data.set(index2, temp);
    }

    // Menghapus tanaman dari Inventory
    public void hapusTanaman(int index) {
        data.remove(index);
    }

    // Menampilkan semua tanaman dalam Inventory
    public void tampilkanInventory() {
        System.out.println("Inventory:");
        for (int i = 0; i < data.size(); i++) {
            System.out.println((i + 1) + ". " + data.get(i));
        }
    }
}
