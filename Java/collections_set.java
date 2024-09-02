import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;
import java.util.Iterator;

public class collections_set
{
	public static void main(String[] args){
		
		// Set interface : Tidak menyimpan elemen duplikat serta data tidak berurutan.
		
		// metode add
		
		Set<String> mySet = new HashSet<>();
		mySet.add("Apple");
		mySet.add("Banana");
		mySet.add("Orange");
		mySet.add("Banana"); // Tidak akan ditambahkan karena "Banana" sudah ada
		
		System.out.println(mySet);
		
		// metode remove
		
		mySet.remove("Banana"); // Menghapus "Banana" dari set
		
		System.out.println(mySet);
		
		// metode size
		
		int size = mySet.size(); // Mendapatkan jumlah elemen dalam set
		
		System.out.println(size);
		
		// metode contains
		
		boolean containsOrange = mySet.contains("Orange"); // true
		
		System.out.println(containsOrange);
		
		// metode isEmpty
		
		boolean isEmpty = mySet.isEmpty(); // false karena set tidak kosong
		
		System.out.println(isEmpty);
		
		// metode clear
		
		mySet.clear(); // Menghapus semua elemen dari set
		
		System.out.println(mySet);
		
		// metode toAray
		
		Set<String> mySet2 = new HashSet<>();
        mySet2.add("Apple");
        mySet2.add("Banana");
        mySet2.add("Orange");

        // Mengonversi elemen-elemen dari myList ke dalam array dengan tipe String
        String[] stringArray = mySet2.toArray(new String[0]);

        // Mencetak elemen-elemen array
        for (int i = 0; i < stringArray.length; i++) {
            System.out.println(stringArray[i]);
        }
		
		// metode iterator
		
		Iterator<String> iterator = mySet2.iterator();
		while (iterator.hasNext()) {
			String element = iterator.next();
			System.out.println(element);
		}
		
		// metode addAll
		
		Set<String> anotherSet = new HashSet<>();
		anotherSet.add("Grapes");
		anotherSet.add("Banana");

		mySet2.addAll(anotherSet); // Menambahkan semua elemen dari anotherSet ke mySet
		
		System.out.println(mySet2);
		
		// metode retainAll
		
		Set<String> intersectionSet = new HashSet<>();
		intersectionSet.add("Apple");
		intersectionSet.add("Banana");

		mySet2.retainAll(intersectionSet); // Menyimpan hanya elemen yang ada dalam kedua set
		System.out.println(mySet2);
		
		// metode removeAll
		
		Set<String> toRemoveSet = new HashSet<>();
		toRemoveSet.add("Apple");
		toRemoveSet.add("Grapes");

		mySet2.removeAll(toRemoveSet); // Menghapus semua elemen yang ada dalam toRemoveSet dari mySet

		System.out.println(mySet2);









		
		
	}
}