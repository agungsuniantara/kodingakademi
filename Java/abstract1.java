abstract public class abstract1
{
	String nama;
	int umur;
	
	// enkapsulasi
	private int id;
	
	// constructor
	public abstract1(String x, int c, int d){
		this.nama = x;
		this.umur = c;
		this.id = d;
	}
	
	public void tampil(){
		System.out.println("nama = " + nama);
		System.out.println("umur = " + umur);
	}
	
	public abstract void suara();
	
	public static void main(String[] args){
		
	}
}