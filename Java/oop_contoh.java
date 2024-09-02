public class oop_contoh
{
	String nama;
	int umur;
	String alamat;
	int nomer_rumah;
	
	// construct
	public oop_contoh(String a, int b, String c, int d){
		this.nama = a;
		this.umur = b;
		this.alamat = c;
		this.nomer_rumah = d;
	}
	
	public String getNama(){
		return nama;
	}
	
	public void getUmur(){
		System.out.println(umur);
	}
	
	public static void main(String[] args)
	{
		oop_contoh akses = new oop_contoh("agung",100,"denpasar", 30);
		oop_contoh akses2 = new oop_contoh("wayan",50,"badung", 20);
		
		// akses
		System.out.println("Data 1 : ");
		System.out.println("nama = " + akses.nama);
		System.out.println("umur = " + akses.umur);
		System.out.println("alamat = " + akses.alamat);
		System.out.println("nomer rumah = " + akses.nomer_rumah);
		
		// akses 2
		System.out.println("Data 2 : ");
		System.out.println("nama = " + akses2.nama);
		System.out.println("umur = " + akses2.umur);
		System.out.println("alamat = " + akses2.alamat);
		System.out.println("nomer rumah = " + akses2.nomer_rumah);
		
		//getNama
		String nama_akses = akses.getNama();
		String nama_akses2 = akses2.getNama();
		System.out.println(nama_akses);
		System.out.println(nama_akses2);
		
		//getUmur
		akses.getUmur();
		akses2.getUmur();
	}
}