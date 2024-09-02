package aksesbilitas_java;

// class hanya dapat menggunakan aksesibilitas : 
// 1. Default
// 2. final
// 3. public

// Default (Tanpa Kata Kunci): Kelas dapat diakses hanya oleh kelas-kelas dalam paket yang sama
class Test{
    String nama = "class default";
}

// Final: Kelas tidak dapat diwariskan oleh kelas lain
final class final_class {
    public void print(){
        System.out.println("final class");
    }
}

// pewarisan
class pewaris_test extends Test{
    public void print(){
        System.out.println(this.nama);
    }
}

// class pewaris_MyClass extends MyClass{
//     public void print(){
//         System.out.println(this.nama);
//     }
// } // error MyClass tidak bisa diwariskan karena menggunakan final


// setiap file hanya memiliki public class 1
public class aksesbilitas {

    // default
    String test_default;

    // Public: bisa diakses class sendiri, bisa diakses class lain, bisa diakses file lain.
    public String test_public;

    // Protected: bisa diakses class sendiri, bisa diakses class lain, tidak bisa diakses file lain. 
    protected String test_protected;

    // Private: bisa diakses class sendiri, tidak bisa diakses class lain, tidak bisa diakses file lain.
    private String test_private;

    // Final : variabel tidak dapat diubah nilainya, kalau dalam bentuk class tidak dapat diwariskan
    final String test_final = "final";

    // Static : variabel atau method dapat dipanggil tanpa deklarasi objek hanya memanggil class nya saja
    static String test_static;

    public aksesbilitas(String a, String b, String c, String d, String e){
        this.test_default = a;
        this.test_private = b;
        this.test_protected = c;
        // this.test_final = d; error final tidak dapat diinisialisasi
        test_static = d; // ketika atribut memakai static maka tidak perlu memakai this karena this itu objek
        this.test_public = e;
    }

    public void manggil_attribut(){
        System.out.println(this.test_default);
        System.out.println(this.test_public);
        System.out.println(this.test_protected);
        System.out.println(this.test_private);
        System.out.println(test_static); // static tidak perlu objek
    }

    public String fungsi_return(){ // fungsi return
        String nama = "fungsi return";
        return nama;
    }

    public void tanpa_static(){ // fungsi void
        System.out.println("fungsi tanpa static");
    }

    public static void pakai_static(){
        System.out.println("fungsi pakai static");
    }

    protected static void pakai_protected(){
        System.out.println("fungsi pakai protected");
    }

    private void pakai_private(){
        System.out.println("fungsi pakai private");
    }

    void test(){
        System.out.println("test");
    }
    
    public static void main(String[] args) {
        aksesbilitas data = new aksesbilitas("test_default", "test_private", "test_protected", "test_static", "test_public");
        System.out.println("Test Atribut : ");
        System.out.println(data.test_default);
        System.out.println(data.test_private);
        System.out.println(data.test_protected);
        System.out.println(test_static); // atribut static
        System.out.println(data.test_public);

        System.out.println("Test fungsi : ");
        data.manggil_attribut();
        String var_return = data.fungsi_return();
        System.out.println(var_return);
        data.tanpa_static();
        pakai_static(); // fungsi static
        data.pakai_private();
        pakai_protected(); // fungsi static
        data.test();
    }
}
