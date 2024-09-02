import java.util.*;

public class App {
    public static void main(String[] args) throws Exception {

        HashMap<String, String> map = new HashMap<>();
        LinkedHashMap<String, String> map_hashlink = new LinkedHashMap<>();

        // put hashmap

        map.put("Nama", "John");
        map.put("Umur", "20");

        System.out.println("Map : " + map);

        // get hashmap

        map.put("Nama", "John");
        map.put("Umur", "20");

        System.out.println("Nama : " + map.get("Nama"));
        System.out.println("Umur : " + map.get("Umur"));

        // keyset hashmap

        map.put("Nama", "John");
        map.put("Umur", "20");

        System.out.println("Key : " + map.keySet());

        // values hashmap

        map.put("Nama", "John");
        map.put("Umur", "20");

        System.out.println("Value : " + map.values());

        // entryset hashmap

        map.put("Nama", "John");
        map.put("Umur", "20");

        System.out.println("Data : " + map.entrySet());

        // foreach hashmap

        map.put("Nama", "John");
        map.put("Umur", "20");

        System.out.println("Data key");
        for (String nama : map.keySet()){
            System.out.println("Key : " + nama);
        }

        System.out.println("Data value");
        for (String umur : map.values()){
            System.out.println("Value : " + umur);
        }

        System.out.println("Data key dan value");
        for (Map.Entry<String, String> data : map.entrySet()){
            String key = data.getKey();
            String value = data.getValue();
            System.out.println("Key : " + key + ", Value : " + value);
        }

        // remove hashmaps

        map.put("Nama", "John");
        map.put("Umur", "20");

        map.remove("Nama");
        System.out.println("Map : " + map);

        // clear hashmaps

        map.put("Nama", "John");
        map.put("Umur", "20");

        map.clear();
        System.out.println("Map : " + map);

        // replace values

        map.put("Nama", "John");
        map.put("Umur", "20");
        
        map.replace("Nama", "Bryan");
        System.out.println("Map : " + map);

        // size hashmap

        map.put("Nama", "John");
        map.put("Umur", "20");
        
        System.out.println("Size map : " + map.size());

        // isempty hashmap

        map.put("Nama", "John");
        map.put("Umur", "20");
        
        System.out.println("Apakah data kosong ? " + map.isEmpty());

        // contains key hashmap

        map.put("Nama", "John");
        map.put("Umur", "20");
        
        System.out.println("Key nama tersedia ? " + map.containsKey("Nama"));

        System.out.println("Value john tersedia ? " + map.containsValue("John"));
    }
}
