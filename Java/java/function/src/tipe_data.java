public class tipe_data {
    public static int hitung(int angka1, int angka2){
        int hasil = angka1 + angka2;
        return hasil;
    }
    public static void main(String[] args) {
        int simpan = hitung(10, 20);
        System.out.println("hasil method tipe data : " + simpan);
    }
}
