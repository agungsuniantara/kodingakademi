public class oop3
{
	String merek;
	String warna;
	int tahunProduksi;
	
	// constructor dengan parameter
	
	public oop3(String merek, String warna, int tahunProduksi){
		this.merek = merek;
		this.warna = warna;
		this.tahunProduksi = tahunProduksi;
	}
	
	public void tampilkanInfo(){
		System.out.println("Merek : " + merek);
		System.out.println("Warna : " + warna);
		System.out.println("Tahun produksi : " + tahunProduksi);
	}
	
	public static void main(String[] args)
	{
		oop3 mobil = new oop3("honda", "merah", 2020);
		System.out.println("Informasi mobil 2 : ");
		mobil.tampilkanInfo();
	}
}