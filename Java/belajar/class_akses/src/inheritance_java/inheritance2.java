package inheritance_java;

public class inheritance2 {
    public static void main(String[] args) {
        mahasiswa data1 = new mahasiswa("john", "denpasar", "20202020");
        data1.tampil_alamat();
        // System.out.println(data1.nama); error atribut private
    }
}
