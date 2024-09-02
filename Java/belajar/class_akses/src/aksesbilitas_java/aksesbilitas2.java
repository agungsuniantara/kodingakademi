package aksesbilitas_java;

public class aksesbilitas2 {
    public static void main(String[] args) {

        // atribut tidak static
        aksesbilitas data = new aksesbilitas("test_default", "test_private", "test_protected", "test_static", "test_public");
        System.out.println(data.test_default);
        // System.out.println(data.test_private); atribut private tidak bisa di akses file lain
        System.out.println(data.test_protected);
        System.out.println(data.test_public);


        // atribut static
        System.out.println(aksesbilitas.test_static); // atribut static pada file lain langsung panggil class nya


        // function tidak static
        data.manggil_attribut();
        String var = data.fungsi_return();
        System.out.println(var);
        data.tanpa_static();
        aksesbilitas.pakai_static(); // function static
        aksesbilitas.pakai_protected(); // function protected static
        // data.pakai_private(); function private tidak bisa di akses file lain
        data.test();


        // panggil void main class aksesbilitas
        // pakai static
        aksesbilitas.main(args);

        // tanpa static
        // data.main(args); error karena void main bersifat static
    }
}
