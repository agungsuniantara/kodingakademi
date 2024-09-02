public class employee
{
	String name;
	int salary;
	
	// construct
	public employee(String a, int b){
		this.name = a;
		this.salary = b;
	}
	
	public String getNama(){
		return name;
	}
	
	public int getSalary(){
		return salary;
	}
	
	public double raiseSalary(double persen){
		return salary * persen;
	}
	
	public void swap(String nama){
		name = nama;
	}
	
	public static void main(String[] args)
	{
		employee akses = new employee("agung", 10000);
		employee akses2 = new employee("wayan", 20000);
		
		double hasil = akses.raiseSalary(0.1);
		System.out.println(hasil);
		
		String nama_akses = akses.name;
		String nama_akses2 = akses2.name;
		
		akses.swap(nama_akses2);
		akses2.swap(nama_akses);
		
		System.out.println(akses.name);
		System.out.println(akses2.name);
	}
}