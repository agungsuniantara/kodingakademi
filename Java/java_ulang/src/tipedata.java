public class tipedata {
    public static void main(String[] args) throws Exception {
        int umur  = 25;
        String nama_lengkap = "John";

        int angka1, angka2;
        String nama;

        float angka_float = 1.1234562f;
        double angka_double = 1.123456789123456;

        char huruf = 'a';

        boolean benar = true;
        boolean salah = false;

        angka1 = 10;
        angka2 = 20;
        nama = "john";

        System.out.println(angka_float);
        System.out.println(angka_double);

        float test1 = (float) angka1;
        double test2 = (double) angka2;
        
        System.out.println(test1);
        System.out.println(test2);

        System.out.println(((Object) angka2).getClass().getSimpleName());
    }
}
