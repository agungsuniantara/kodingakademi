import java.util.*;

public class App {
    public static void main(String[] args) {

        // Membuat LinkedList
        LinkedList<String> linkedList_str = new LinkedList<>();
        LinkedList<Integer> linkedList_int = new LinkedList<>();
        LinkedList<Double> linkedList_double = new LinkedList<>();
        LinkedList<Boolean> linkedList_boolean = new LinkedList<>();

        // Menambahkan elemen ke LinkedList
        linkedList_str.add("Apple");
        linkedList_str.add("Banana");
        linkedList_str.add("Orange");

        System.out.println("LinkedList : " + linkedList_str);

        // Menambahkan elemen di awal LinkedList
        linkedList_str.addFirst("Grape");
        System.out.println("LinkedList : " + linkedList_str);

        // Menambahkan elemen di akhir LinkedList
        linkedList_str.addLast("Banana");
        System.out.println("LinkedList : " + linkedList_str);

        // Menampilkan elemen-elemen LinkedList for

        for (int i = 0; i < linkedList_str.size(); i++){
            System.out.println("index " + i + ": " + linkedList_str.get(i));
        }

        // Menampilkan elemen-elemen LinkedList

        for (String fruit : linkedList_str) {
            System.out.println(fruit);
        }

        // Mendapatkan dan mengatur elemen di indeks tertentu

        String data = linkedList_str.get(1);
        System.out.println(data);

        // Menghapus elemen berdasarkan nilai

        linkedList_str.remove("Banana");
        linkedList_str.remove(0);
        System.out.println("LinkedList : " + linkedList_str);

        // Menghapus elemen pertama

        linkedList_str.removeFirst();
        System.out.println("LinkedList : " + linkedList_str);

        // Menghapus elemen terakhir

        linkedList_str.removeLast();
        System.out.println("LinkedList : " + linkedList_str);

        // Menghapus semua elemen dari LinkedList

        linkedList_str.clear();
        System.out.println("LinkedList : " + linkedList_str);

        // Mendapatkan dan mengatur elemen di indeks tertentu

        linkedList_str.add("Apple");
        linkedList_str.add("Banana");
        linkedList_str.add("Orange");

        linkedList_str.set(1, "Mango");
        System.out.println("LinkedList : " + linkedList_str);

        // Mendapatkan ukuran LinkedList

        int size = linkedList_str.size();
        System.out.println("Size: " + size);

        // Mengecek apakah linkedlist kosong

        boolean isEmpty = linkedList_str.isEmpty();
        System.out.println("Apakah LinkedList kosong? " + isEmpty);

        // Mengecek apakah LinkedList mengandung suatu elemen tertentu

        boolean containsBanana = linkedList_str.contains("Banana");
        System.out.println("Apakah LinkedList mengandung 'Banana'? " + containsBanana);
        
    }
}
