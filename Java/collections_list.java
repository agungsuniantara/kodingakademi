import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class collections_list
{
	public static void main(String[] args){
		
		// List interface : Menyimpan elemen berurutan.
		
		// metode add
		
		List<String> myList = new ArrayList<>();
		myList.add("Apple");
		myList.add("Banana");
		myList.add("Orange");
		
		System.out.println(myList);
		
		// metode add index
		
		myList.add(1, "Grapes"); // Menambahkan "Grapes" pada indeks 1
		
		System.out.println(myList);
		
		// metode get
		
		String fruit = myList.get(2); // Mengambil elemen pada indeks 2 (Orange)
		
		System.out.println(fruit);
		
		// metode size
		
		int size = myList.size(); // Mendapatkan jumlah elemen dalam daftar
		System.out.println(size);
		
		// metode remove
		
		myList.remove(1); // Menghapus elemen pada indeks 1 (Banana)
		System.out.println(myList);
		
		// metode contains
		
		boolean containsBanana = myList.contains("Banana"); // true
		System.out.println(containsBanana);
		
		// metode isEmpty
		
		boolean isEmpty = myList.isEmpty(); // false karena daftar tidak kosong
		System.out.println(isEmpty);
		
		// metode indexOf
		
		int index = myList.indexOf("Orange"); // 2
		System.out.println(index);
		
		// metode clear
		
		myList.clear(); // Menghapus semua elemen dari daftar
		System.out.println(myList);
		
		// metode toAray
		
		List<String> myList2 = new ArrayList<>();
        myList2.add("Apple");
        myList2.add("Banana");
        myList2.add("Orange");

        // Mengonversi elemen-elemen dari myList ke dalam array dengan tipe String
        String[] stringArray = myList2.toArray(new String[0]);

        // Mencetak elemen-elemen array
        for (int i = 0; i < stringArray.length; i++) {
            System.out.println(stringArray[i]);
        }
		
		// Iterasi menggunakan for-each loop
		 
        System.out.println("Iterating using for-each loop:");
        for (String tampil : myList2) {
            System.out.println(tampil);
        }
	}
}