import java.util.*;

public class hashmap_iterator {
    public static void main(String[] args) {
        // Hashmap next 1

        HashMap<String, String> map = new HashMap<>();
        map.put("Nama", "John");
        map.put("Umur", "20");

        Set<String> key = map.keySet();
        Collection<String> value = map.values();

        Iterator<String> iterator_key = key.iterator();
        Iterator<String> iterator_value = value.iterator();

        String key1 = iterator_key.next();
        String value1 = iterator_value.next();
        System.out.println("Key: " + key1 + ", Value: " + value1);

        String key2 = iterator_key.next();
        String value2 = iterator_value.next();
        System.out.println("Key: " + key2 + ", Value: " + value2);

        // Hashmap next 2

        HashMap<String, String> map1 = new HashMap<>();
        map1.put("Nama", "John");
        map1.put("Umur", "20");

        Set<String> key3 = map.keySet(); // set = data unik / tidak duplikat

        Iterator<String> iterator = key3.iterator();

        String key4 = iterator.next();
        System.out.println("Key: " + key4 + ", Value: " + map.get(key4));

        String key5 = iterator.next();
        System.out.println("Key: " + key5 + ", Value: " + map.get(key5));

        // hashmap hasnext

        HashMap<String, String> map2 = new HashMap<>();
        map2.put("Nama", "Bryan");

        Set<String> key6 = map2.keySet();
        Iterator<String> iterator2 = key6.iterator();
        
        System.out.println("Cek elemen 1 : " + iterator2.hasNext());
        String key7 = iterator2.next();
        System.out.println("Key: " + key7 + ", Value: " + map.get(key7));
        System.out.println("Cek elemen 2 : " + iterator2.hasNext());

        // Loop hashmap

        HashMap<String, String> map3 = new HashMap<>();
        map3.put("Nama", "Bryan");
        map3.put("Umur", "20");

        Set<String> key8 = map3.keySet();
        Iterator<String> iterator3 = key8.iterator();

        while (iterator3.hasNext()) {
            String data_key = iterator3.next();
            System.out.println("Key : " + data_key + ", Value : " + map3.get(data_key));
        }
    }
}
