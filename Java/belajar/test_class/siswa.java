class siswa {
    private String nama = "karen";
    private String alamat = "denpasar";
    private int angka1 = 10;
    private int angka2 = 20;

    public void tampil_data(){
        System.out.println(this.nama);
        System.out.println(this.alamat);
    }

    public void tambah(){
        int hasil = this.angka1 + this.angka2;
        System.out.println(hasil);
    }

    public int tambah_int(){
        int hasil = this.angka1 + this.angka2;
        return hasil;
    }

    public String to_String(){
        return "hasil = " + tambah_int(); // 30
    }
}

class menu{
    public static void main(String[] args) {
        siswa data1 = new siswa();
        data1.tampil_data();
        data1.tambah();
        int test = data1.tambah_int();
        System.out.println(test);
    }
}



