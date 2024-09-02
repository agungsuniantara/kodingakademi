public class oop4
{
	String nama;
	int umur;
	
	// enkapsulasi
	private int id;
	
	// constructor
	public oop4(String x, int c, int d){
		this.nama = x;
		this.umur = c;
		this.id = d;
	}
	
	public void tampil(){
		System.out.println("nama = " + nama);
		System.out.println("umur = " + umur);
	}
	
	public int angka(int x){
		return x;
	}
	
	// overloading 
	
	public int angka(int x, int c){
		return x + c;
	}
	
	public int angka(int x, int c, int b){
		return x + c + b;
	}
	
	// getter
	
	public int tampil_id(){
		return this.id;
	}
	
	// setter
	
	public void masuk_data(int angka){
		this.umur = angka;
	}
	
	public static void main(String[] args)
	{
		oop4 data1 = new oop4("agung", 20, 2);
		
		data1.tampil();
		
		//overloading
		int angka1 = data1.angka(10);
		int angka2 = data1.angka(10,20);
		int angka3 = data1.angka(10,20,30);
		
		System.out.println(angka1);
		System.out.println(angka2);
		System.out.println(angka3);
		
		//getter
		int id = data1.tampil_id();
		System.out.println(id);
		
		//setter
		data1.masuk_data(100);
		System.out.println(data1.umur);
	}
}