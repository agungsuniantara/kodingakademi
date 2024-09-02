public class oop6
{
	String nama;
	int umur;
	
	// enkapsulasi
	private int id;
	
	// constructor
	public oop6(String x, int c, int d){
		this.nama = x;
		this.umur = c;
		this.id = d;
	}
	
	private void tampil(){
		System.out.println("nama = " + nama);
		System.out.println("umur = " + umur);
	}
	
	public static void main(String[] args)
	{
		oop6 data2 = new oop6("wahyu", 30, 10);
		
		data2.tampil();
		
		double x = 3.4;
		int nx = (int) x;
		
		System.out.println(nx);
	}
}