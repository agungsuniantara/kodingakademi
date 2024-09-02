import java.util.*;

public class arraylist_iterator {
    public static void main(String[] args) {

        // arraylist next

        ArrayList<String> arraylist = new ArrayList<>();
        arraylist.add("Agus");
        arraylist.add("Made");

        Iterator<String> iterator = arraylist.iterator();
        System.out.println("Next : " + iterator.next());
        System.out.println("Next : " + iterator.next());

        // arraylist hasnext

        ArrayList<String> arraylist1 = new ArrayList<>();
        arraylist1.add("Bryan");

        Iterator<String> iterator1 = arraylist1.iterator();
        System.out.println("Cek elemen 1 : " + iterator1.hasNext());
        System.out.println("Next : " + iterator1.next());
        System.out.println("Cek elemen 2 : " + iterator1.hasNext());

        // arraylist remove

        ArrayList<String> arraylist2 = new ArrayList<>();
        arraylist2.add("Made");
        arraylist2.add("Agus");

        System.out.println("Data sebelum dihapus : " + arraylist2);

        Iterator<String> iterator2 = arraylist2.iterator();
        iterator2.next();
        iterator2.next();
        iterator2.remove();

        System.out.println("Data setelah dihapus : " + arraylist2);

        // arraylist hashmap

        HashMap<String, String> map = new HashMap<>();
        map.put("Nama", "Bryan");
        map.put("Umur", "20");

        System.out.println("Data sebelum dihapus : " + map);

        Set<String> key = map.keySet();
        Iterator<String> iterator3 = key.iterator();

        iterator3.next();
        iterator3.next();
        iterator3.remove();

        System.out.println("Data setelah dihapus : " + map);

        // Loop arraylist

        ArrayList<Integer> numbers = new ArrayList<>();

        numbers.add(3);
        numbers.add(4);

        Iterator<Integer> iterator4 = numbers.iterator();

        while (iterator4.hasNext()) {
            int number = iterator4.next();
            System.out.println("Data : " + number);
        }

    }
}
