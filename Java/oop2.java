public class oop2
{
	String merek;
	String warna;
	int tahunProduksi;
	
	// constructor tanpa parameter
	
	public oop2(String a, String b, int c){
		merek = a;
		warna = b;
		tahunProduksi = c;
	}
	
	public void tampilkanInfo(){
		System.out.println("Merek : " + merek);
		System.out.println("Warna : " + warna);
		System.out.println("Tahun produksi : " + tahunProduksi);
	}

	public String get_merek(){
		return merek;
	}
	
	public static void main(String[] args)
	{
		oop2 mobil = new oop2("honda", "merah", 20);
		System.out.println("informasi mobil 1 : ");
		mobil.tampilkanInfo();

		String value = mobil.get_merek();
		System.out.println(value);
	}
}