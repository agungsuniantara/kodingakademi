import java.util.*;

public class App {
    public static void main(String[] args) throws Exception {
        // linkedlist next

        LinkedList<String> linkedlist = new LinkedList<>();
        linkedlist.add("John");
        linkedlist.add("Steven");

        Iterator<String> iterator = linkedlist.iterator();
        System.out.println("Next : " + iterator.next());
        System.out.println("Next : " + iterator.next());

        // linkedlist hasnext

        LinkedList<String> linkedlist1 = new LinkedList<>();
        linkedlist1.add("John");

        Iterator<String> iterator1 = linkedlist1.iterator();
        System.out.println("Cek elemen 1 : " + iterator1.hasNext());
        System.out.println("Next : " + iterator1.next());
        System.out.println("Cek elemen 2 : " + iterator1.hasNext());

        // linkedlist remove

        LinkedList<String> linkedlist2 = new LinkedList<>();
        linkedlist2.add("John");
        linkedlist2.add("Bryan");

        System.out.println("Data sebelum dihapus : " + linkedlist2);

        Iterator<String> iterator2 = linkedlist2.iterator();
        iterator2.next();
        iterator2.next();
        iterator2.remove();

        System.out.println("Data setelah dihapus : " + linkedlist2);

        // Loop LinkedList

        LinkedList<Integer> numbers = new LinkedList<>();

        numbers.add(1);
        numbers.add(2);

        Iterator<Integer> iterator3 = numbers.iterator();

        while (iterator3.hasNext()) {
            int number = iterator3.next();
            System.out.println("Data : " + number);
        }
        




        // assignment

        LinkedList <String> key_hash = new LinkedList<>();
        ArrayList <String> value_hash = new ArrayList<>();
        LinkedHashMap <String, String> hashmap = new LinkedHashMap<>();

        hashmap.put("Nama", "John");
        hashmap.put("Alamat", "Denpasar");
        hashmap.put("Umur", "18 Tahun");
        hashmap.put("Pekerjaan", "Siswa");
        hashmap.put("Status", "Single");
        
        Set<String> key = hashmap.keySet();
        Iterator<String> iterator_hash = key.iterator();
        
        System.out.println("Data hashmap sebelum dihapus : ");
        while (iterator_hash.hasNext()) {
            String data_key = iterator_hash.next();
            System.out.println(data_key + " : " + hashmap.get(data_key));
            key_hash.add(data_key);
            value_hash.add(hashmap.get(data_key));
            iterator_hash.remove();
        }

        System.out.println("Data hashmap setelah dihapus : " + hashmap);
        System.out.println("Data linkedlist : " + key_hash);
        System.out.println("Data arraylist : " + value_hash);
    }
}
