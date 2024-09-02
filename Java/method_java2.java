public class method_java2
{
	public void tampil(){
		System.out.println("agung");
	}
	
	public void tampil2(String nama){
		System.out.println(nama);
	}
	
	public int rumus(int angka1, int angka2){
		int hasil = angka1 * angka2;
		return hasil;
	}
	
	public static void tampil3(){
		System.out.println("ini method statis");
	}
	
	public static int hitung(int angka1, int angka2){
		int hasil = angka1 * angka2;
		return hasil;
	}
	
	public static void main(String[] args)
	{
		method_java2 baru = new method_java2();
		
		// tidak statis
		baru.tampil();
		baru.tampil2("dyland");
		int ambil = baru.rumus(10,20);
		System.out.println(ambil);
		
		// statis
		tampil3();
		int tampil = hitung(10,20);
		System.out.println(tampil);
	}
}