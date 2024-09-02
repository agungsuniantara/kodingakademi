package inheritance_java;

class user{
    private String nama;
    private String alamat;

    public user(String a, String b){
        this.nama = a;
        this.alamat = b;
    }

    public void tampil_nama(){
        System.out.println("Nama : " + this.nama);
    }

    public void tampil_alamat(){
        System.out.println("Alamat : " + this.alamat);
    }
}

class mahasiswa extends user{
    private static String nim; // atribut memakai private static

    public mahasiswa(String a, String b, String c){
        super(a, b);
        nim = c; // ketika atribut memakai static maka tidak perlu memakai this karena this itu objek
    }

    public void tampil_nim(){
        System.out.println("Nim : " + nim); // ketika atribut memakai static maka tidak perlu memakai this karena this itu objek
    }
}

public class inheritance1 {
    public static void main(String[] args) {
        mahasiswa data1 = new mahasiswa("john", "denpasar", "20202020");
        data1.tampil_nim();
        data1.tampil_nama();
        data1.tampil_alamat();
        // System.out.println(data1.nama); error atribut
    }
}
