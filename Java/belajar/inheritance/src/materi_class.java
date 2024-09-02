
// Default (Tanpa Kata Kunci): Kelas dapat diakses hanya oleh kelas-kelas dalam paket yang sama
class Test{
    String nama = "agung";
}

// Public: Kelas dapat diakses dari mana saja, baik dari kelas di dalam paket yang sama maupun dari paket lain

// public class test2{} error karena jika menggunakan "public" pada kelas harus memiliki file sendiri

// Final: Kelas tidak dapat diwariskan oleh kelas lain
final class MyClass {
    String nama = "agung";
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

public class materi_class {
    public static void main(String[] args) throws Exception {
        pewaris_test coba = new pewaris_test();
        coba.print();
    }
}


