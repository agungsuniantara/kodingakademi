import java.util.LinkedList;
import java.util.Iterator;

public class collection_linkedlist {
    public static void main(String[] args) {
        LinkedList<String> linkedList = new LinkedList<>();

        // 1. Menambahkan elemen ke akhir list
        linkedList.add("Apple");
        linkedList.add("Banana");
        linkedList.add("Orange");
		
		System.out.println(linkedList);

        // 2. Menambahkan elemen di awal list
        linkedList.addFirst("Grapes");
		
		System.out.println(linkedList);

        // 3. Menambahkan elemen di akhir list
        linkedList.addLast("Strawberry");
		
		System.out.println(linkedList);

        // 4. Menambahkan elemen pada indeks tertentu
        linkedList.add(2, "Mango");
		
		System.out.println(linkedList);

        // 5. Menghapus dan mengembalikan elemen pertama dari list
        String removedElement = linkedList.remove();
		
		System.out.println(linkedList);

        // 6. Menghapus dan mengembalikan elemen pertama dari list
        String removedFirst = linkedList.removeFirst();
		
		System.out.println(linkedList);

        // 7. Menghapus dan mengembalikan elemen terakhir dari list
        String removedLast = linkedList.removeLast();
		
		System.out.println(linkedList);

        // 8. Menghapus elemen tertentu dari list
        linkedList.remove("Orange");
		
		System.out.println(linkedList);
		
		// 9. Menghapus elemen pada indeks tertentu
        linkedList.remove(1);
		
		System.out.println(linkedList);
		
		// 10. Mengambil elemen pada indeks tertentu
        String element = linkedList.get(0);
		
		System.out.println(element);
		
		// 11. Mengganti elemen pada indeks tertentu dengan elemen baru
		linkedList.add("Pear");
        linkedList.set(0, "Cherry");
		
		System.out.println(linkedList);
		
		// 12. Mendapatkan jumlah elemen dalam list
        int size = linkedList.size();
		
		System.out.println(size);
		
		 // 13. Memeriksa apakah list kosong
        boolean isEmpty = linkedList.isEmpty();
		
		System.out.println(isEmpty);
		
		// 14. Menghapus semua elemen dari list
        linkedList.clear();
		
		System.out.println(linkedList);
		
		// 15. Mengembalikan indeks pertama dari elemen tertentu
		linkedList.add("Apple");
        linkedList.add("Banana");
        linkedList.add("Orange");
		
        int index = linkedList.indexOf("Apple");
		
		System.out.println(index);
		
		// 16. Menggunakan iterator untuk iterasi ke depan
        Iterator<String> iterator = linkedList.iterator();
        while (iterator.hasNext()) {
            String forwardElement = iterator.next();
            System.out.println("Forward Iteration: " + forwardElement);
        }
		
		// 17. Menggunakan iterator untuk iterasi ke belakang
        Iterator<String> descendingIterator = linkedList.descendingIterator();
        while (descendingIterator.hasNext()) {
            String backwardElement = descendingIterator.next();
            System.out.println("Backward Iteration: " + backwardElement);
        }
	}
}
