import java.util.*;

public class assignment {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        HashMap<String, String> nama = new HashMap<>();
        HashMap<String, Integer> umur = new HashMap<>();
        HashMap<String, String> alamat = new HashMap<>();

        System.out.print("Banyak data : ");
        int jumlah = scan.nextInt();

        for (int i = 1; i < jumlah + 1; i++){
            System.out.println("Data " + i + " : ");
            System.out.print("Masukan nama : ");
            String data_nama = scan.next();
            String key = "nama_" + i;
            nama.put(key, data_nama);

            System.out.print("Masukan umur : ");
            int data_umur = scan.nextInt();
            umur.put(data_nama, data_umur);

            System.out.print("Masukan alamat : ");
            String data_alamat = scan.next();
            alamat.put(data_nama, data_alamat);
        }

        System.out.println("Data hashmap nama : " + nama);
        System.out.println("Data hashmap umur : " + umur);
        System.out.println("Data hashmap alamat : " + alamat);

        System.out.println("Tampilkan data umur berdasarkan nama : ");

        for (Map.Entry<String, String> data_nama : nama.entrySet()){
            String value = data_nama.getValue();
            System.out.println("Nama : " + value);
            for(Map.Entry<String, Integer> data_umur : umur.entrySet()){
                String key = data_umur.getKey();
                int value_umur = data_umur.getValue();
                if (key.equals(value)){
                    System.out.println("Umur : " + value_umur + " Tahun");
                }
            }
        }

        scan.close();
    }
}
