public class App {
    public static void nama(){
        System.out.println("Nama = john");
    }

    public static int hitung(){
        int angka = 10;
        return angka;
    }

    public void tampil_nama(){
        System.out.println("ini fungsi tanpa static");
    }

    public String tampil_alamat(){
        return "denpasar";
    }

    public static void tambah(int a, int b){
        int hasil = a + b;
        System.out.println(hasil);
    }

    public static void main(String[] args) {
        nama();
        int hasil = hitung();
        System.out.println(hasil);

        App tampil = new App();
        tampil.tampil_nama();
        String alamat = tampil.tampil_alamat();
        System.out.println(alamat);

        tambah(100, 200);
    }
}
