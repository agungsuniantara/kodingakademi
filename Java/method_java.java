public class method_java
{
	// Metode void
	public void tampil(){
		System.out.println("tampil");
	}
	
	// Metode void dengan Parameter
	public void tampil2(String nama){
		System.out.println(nama);
	}
	
	// Metode dengan nilai kembali (return)
	public int tambah(int a, int b){
		return a + b;
	}
	
	// Metode void statis
	public static void statis(){
		System.out.println("ini metode statis");
	}
	
	// Metode void statis parameter
	public static void statis_parameter(String coba){
		System.out.println(coba);
	}
	
	// Metode int statis return parameter
	public static int statis_return(int a, int b){
		return a + b;
	}
	
	public static void main(String[] args)
	{
		method_java contoh = new method_java();
		contoh.tampil();
		contoh.tampil2("agung");
		int hasil = contoh.tambah(10,20);
		System.out.println(hasil);
		
		// statis
		statis();
		statis_parameter("agung");
		int hasil2 = statis_return(10, 20);
		System.out.println(hasil2);
	}
}