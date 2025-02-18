import java.util.*;

class struktur_data {
    public void list(){
        // Membuat list
        List<String> fruits = new ArrayList<>();

        // Menambahkan elemen
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Orange");

        // Menambahkan elemen di indeks tertentu
        fruits.add(1, "Grapes");

        // Mengakses elemen berdasarkan indeks
        System.out.println("Buah pertama: " + fruits.get(0));

        // Menghapus elemen berdasarkan nilai
        fruits.remove("Banana");

        // Menghapus elemen berdasarkan indeks
        fruits.remove(2);

        // Menampilkan semua elemen
        System.out.println("Daftar buah: ");

        for (String fruit : fruits) {
            System.out.println(fruit);
        }

        // Mengecek keberadaan elemen
        System.out.println("Apakah ada Orange? " + fruits.contains("Orange"));

        // Ukuran list
        System.out.println("Jumlah elemen: " + fruits.size());

        // Menghapus semua elemen
        fruits.clear();

        // Mengecek apakah list kosong
        System.out.println("Apakah list kosong? " + fruits.isEmpty());
    }
    public void map(){
        // Membuat map
        Map<String, Integer> productPrices = new HashMap<>();

        // Menambahkan pasangan key-value
        productPrices.put("Apple", 50);
        productPrices.put("Banana", 30);
        productPrices.put("Orange", 20);

        // Mengakses value berdasarkan key
        System.out.println("Harga Apple: " + productPrices.get("Apple"));

        // Menampilkan semua pasangan key-value
        for (Map.Entry<String, Integer> entry : productPrices.entrySet()) {
            System.out.println(entry.getKey() + " - " + entry.getValue());
        }

        // Menghapus elemen berdasarkan key
        productPrices.remove("Banana");

        // Mengecek keberadaan key
        System.out.println("Apakah ada Orange? " + productPrices.containsKey("Orange"));

        // Mengecek keberadaan value
        System.out.println("Apakah ada harga 50? " + productPrices.containsValue(50));

        // Menampilkan semua key
        System.out.println("Produk: " + productPrices.keySet());

        // Menampilkan semua value
        System.out.println("Harga: " + productPrices.values());

        // Menghapus semua elemen
        productPrices.clear();

        // Mengecek apakah Map kosong
        System.out.println("Apakah map kosong? " + productPrices.isEmpty());
    }
    public void list_map(){
        // Membuat Map untuk menyimpan nama mahasiswa dan daftar nilainya
        Map<String, List<Integer>> studentGrades = new HashMap<>();

        // Menambahkan data mahasiswa
        studentGrades.put("Alice", new ArrayList<>(Arrays.asList(90, 85, 88)));
        studentGrades.put("Bob", new ArrayList<>(Arrays.asList(75, 80, 70)));

        // Menampilkan semua data mahasiswa
        System.out.println("Data mahasiswa:");
        for (Map.Entry<String, List<Integer>> entry : studentGrades.entrySet()) {
            System.out.println("Nama: " + entry.getKey() + ", Nilai: " + entry.getValue());
        }

        // Menambahkan nilai baru untuk Alice
        studentGrades.get("Alice").add(95);

        // Menampilkan nilai terbaru Alice
        System.out.println("Nilai terbaru Alice: " + studentGrades.get("Alice"));

        // Menambahkan mahasiswa baru
        studentGrades.put("Charlie", new ArrayList<>(Arrays.asList(88, 92)));

        // Menampilkan semua data mahasiswa setelah perubahan
        System.out.println("Data mahasiswa setelah perubahan:");
        for (Map.Entry<String, List<Integer>> entry : studentGrades.entrySet()) {
            System.out.println("Nama: " + entry.getKey() + ", Nilai: " + entry.getValue());
        }
    }
    public void tambahan(){
        String input = "id1:2, id2:3";
        String[] pairs = input.split(",");
        // Cara 1: Menggunakan Arrays.toString()
        System.out.println("Menggunakan Arrays.toString(): " + Arrays.toString(pairs));

        // Cara 2: Menggunakan loop untuk mencetak elemen array
        System.out.println("Menggunakan loop:");
        for (String pair : pairs) {
            System.out.println(pair);
        }

        String id = " id1 ".trim();
        System.out.println(id);

        String input2 = "ID1 : 2 ";
        input2 = input2.replaceAll("D", "U");
        System.out.println(input2);
    }
}

public class latihan {
    public static void main(String[] args) {
        struktur_data test = new struktur_data();
        test.tambahan();
    }
}
