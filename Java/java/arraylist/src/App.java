import java.util.*;

public class App {
    public static void main(String[] args) {
        // Membuat ArrayList
        ArrayList<String> arraylist_str = new ArrayList<>();

        // Menambahkan elemen ke ArrayList
        arraylist_str.add("Apple");
        arraylist_str.add("Banana");
        arraylist_str.add("Orange");

        System.out.println("ArrayList : " + arraylist_str);

        // Menambahkan elemen di awal ArrayList

        arraylist_str.add(0, "Grapes");
        System.out.println("ArrayList : " + arraylist_str);

        // for arraylist

        for (int i = 0; i < arraylist_str.size(); i++){
            System.out.println("index " + i + ": " + arraylist_str.get(i));
        }

        // foreach arraylist

        for (String data : arraylist_str){
            System.out.println(data);
        }

        // get arraylist

        String fruit = arraylist_str.get(2);
        System.out.println("Elemen pada indeks 2 : " + fruit);

        // Menghapus elemen berdasarkan nilai
        
        arraylist_str.remove("Apple");
        arraylist_str.remove(0);
        System.out.println("ArrayList : " + arraylist_str);

        // Menghapus elemen berdasarkan nilai

        arraylist_str.set(1, "Grape");
        System.out.println("ArrayList : " + arraylist_str);

        // Mendapatkan ukuran ArrayList

        int size = arraylist_str.size();
        System.out.println("Ukuran ArrayList : " + size);

        // Mengecek apakah ArrayList kosong

        boolean isEmpty = arraylist_str.isEmpty();
        System.out.println("Apakah ArrayList kosong? " + isEmpty);

        // Mengecek apakah ArrayList mengandung suatu elemen tertentu

        boolean containsBanana = arraylist_str.contains("Apple");
        System.out.println("Apakah ArrayList mengandung 'Apple'? " + containsBanana);
    }
}
