public class oop5
{
	String nama;
	int umur;
	
	// enkapsulasi
	private int id;
	
	// constructor
	public oop5(String x, int c, int d){
		this.nama = x;
		this.umur = c;
		this.id = d;
	}
	
	public void tampil(){
		System.out.println("nama = " + nama);
		System.out.println("umur = " + umur);
	}
	
	public static void main(String[] args)
	{
		oop6 data2 = new oop6("wahyu", 30, 10);
		
		data2.tampil();
	}
}