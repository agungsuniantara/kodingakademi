public class assignment_oop
{
	String nama;
	int salary;
	
	public assignment_oop(String nama, int salary){
		this.nama = nama;
		this.salary = salary;
	}
	
	public String getNama(){
		return nama;
	}
	
	public int getSalary(){
		return salary;
	}
	
	public int raiseSalary(int angka){
		return salary * angka;
	}
	
	// metode static merupakan metode diluar class
	// metode static tidak dapat mengambil variabel class maka dapat menggunakan parameter untuk ngambil nilai dari variabel
	// contoh :
	
	public static void tripleSalary1(int x) {
		// int angka = salary (error)
        int angka = x * 3;
        System.out.println(angka);
    }
	
	public static void main(String[] args)
	{
		assignment_oop data1 = new assignment_oop("agung", 20);
		
		System.out.println(data1.getNama());
		
		// panggil metode static tanpa class
		tripleSalary1(data1.salary);

	}
}