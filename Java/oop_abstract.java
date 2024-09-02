// Kelas abstract
abstract class oop_abstract {
    private String nama;

    // Konstruktor
    public oop_abstract(String nama) {
        this.nama = nama;
    }

    // Metode concrete
    public void bergerak() {
        System.out.println(nama + " bergerak");
    }

    // Metode abstract yang harus diimplementasi oleh kelas turunan
    public abstract void suara();
}

// Kelas turunan pertama
class Kucing extends oop_abstract {
    // Konstruktor
    public Kucing(String nama) {
        super(nama);
    }

    // Implementasi metode abstract
    @Override
    public void suara() {
        System.out.println("Meow!");
    }
}

// Kelas turunan kedua
class Anjing extends oop_abstract {
    // Konstruktor
    public Anjing(String nama) {
        super(nama);
    }

    // Implementasi metode abstract
    @Override
    public void suara() {
        System.out.println("Woof!");
    }
}

	public static void main(String[] args) {
        Kucing kucing = new Kucing("Tom");
        Anjing anjing = new Anjing("Buddy");

        kucing.bergerak();
        kucing.suara();

        anjing.bergerak();
        anjing.suara();
    }
