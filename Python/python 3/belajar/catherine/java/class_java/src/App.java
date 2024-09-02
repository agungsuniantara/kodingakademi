public class App {
    String nama;
    static String alamat;
    int umur;

    public App(String a, String b, int c){
        this.nama = a; // this adalah object
        alamat = b;
        this.umur = c;
    }

    public void tampil_nama(){
        System.out.println(this.nama);
    }

    public String coba(){
        String nama = this.nama;
        return nama;
    }

    public static void tampil_alamat(){
        System.out.println(alamat);
    }

    public static void main(String[] args) {
        App data = new App("john", "denpasar", 20);
        System.out.println("Atribut : ");
        System.out.println(data.nama); // atribut tanpa static
        System.out.println(alamat); // atribut static
        System.out.println(data.coba());

        System.out.println("Function : ");
        data.tampil_nama(); // function tanpa static
        tampil_alamat(); // function static
    }  
}
