public class oop2
{
	String merek;
	String warna;
	int tahunProduksi;
	
	// constructor tanpa parameter
	
	public oop2(){
		merek = "Unknown";
		warna = "Putih";
		tahunProduksi = 2020;
	}
	
	public void tampilkanInfo(){
		System.out.println("Merek : " + merek);
		System.out.println("Warna : " + warna);
		System.out.println("Tahun produksi : " + tahunProduksi);
	}
	
	public static void main(String[] args)
	{
		oop2 mobil = new oop2();
		System.out.println("informasi mobil 1 : ");
		mobil.tampilkanInfo();
		System.out.println();
	}
}