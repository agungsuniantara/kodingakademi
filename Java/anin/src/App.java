public class App {
    String name;
    Double salary;

    public App (String nama, double b){
        name = nama;
        salary = b;
    }

    public void tukar(App kelas_lain){
        String temp = name;

        name = kelas_lain.name; // objek1.name = objek2.name
        kelas_lain.name = temp; // objek2.name = temp
    }


    public static void main(String[] args) throws Exception {
        App objek1 = new App("agung", 20000);
        App objek2 = new App("anin", 20000);

        System.out.println("Nama sebelum ditukar : " + objek1.name);

        objek1.tukar(objek2);

        System.out.println("Nama setelah ditukar : " + objek1.name);
    }
}
