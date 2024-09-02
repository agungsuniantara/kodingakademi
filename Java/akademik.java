abstract public class akademik
{	
	int id;
	String nama;
	String alamat;
	int umur;
	int bayar;
	
	public akademik(int a, String b, String c, int d, int e){
		this.id = a;
		this.nama = b;
		this.alamat = c;
		this.umur = d;
		this.bayar = e;
	}
	
	public void tampil_data(){
		System.out.println("id = " + id);
		System.out.println("nama = " + nama);
		System.out.println("alamat = " + alamat);
		System.out.println("umur = " + umur);
		System.out.println("bayar = " + bayar);
	}
	
	public abstract void bayar();
	
	public static void main(String[] args)
	{
		
	}
}