abstract public class inheritance
{
	String nama;
	int umur;
	int id;
	
	public inheritance(String x, int c, int d){
		this.nama = x;
		this.umur = c;
		this.id = d;
	}
	
	public void tampil(){
		System.out.println("nama = " + nama);
		System.out.println("umur = " + umur);
	}
	
	public void tampil2(){
		System.out.println("function public");
	}
	
	public abstract void tampil3();
	
	public static void main(String[] args)
	{
		
	}
}