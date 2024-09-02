public class overloading_encapsulation
{
	// enkapsulasi
	private String name;
	
	// constructor dengan parameter
	public overloading_encapsulation(String nama){
		this.name = nama;
	}
	
	// overloading dapat menggunakan nama method yang sama
	
	// Metode untuk menambahkan dua angka int
    public int add(int a, int b) {
        return a + b;
    }

    // Metode untuk menambahkan tiga angka int
    public int add(int a, int b, int c) {
        return a + b + c;
    }

    // Metode untuk menambahkan dua angka double
    public double add(double a, double b) {
        return a + b;
    }
	
	
	// enkapsulasi berhubungan dengan getter dan setter
	
	// Metode getter untuk name (ambil)
    public String getName() {
        return name;
    }

    // Metode setter untuk name (masuk)
    public void setName(String name) {
        this.name = name;
    }
	
	public static void main(String[] args)
	{
		overloading_encapsulation contoh = new overloading_encapsulation("agung");
		
		// overloading
		int hasil1 = contoh.add(10,20);
		int hasil2 = contoh.add(20,30,40);
		double hasil3 = contoh.add(0.1, 10.50);
		
		System.out.println("Hasil Overloading:");
        System.out.println("Hasil1: " + hasil1);
        System.out.println("Hasil2: " + hasil2);
        System.out.println("Hasil3: " + hasil3);
		
		
		// enkapsulasi getter setter
		String nama = contoh.getName();
		System.out.println("Sebelum dirubah : " + nama);
		contoh.setName("wayan");
		System.out.println("Setelah dirubah : " + contoh.name);
	}
}