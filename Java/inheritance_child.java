public class inheritance_child extends inheritance
{
	int angka;
	
	public inheritance_child(String x, int c, int d, int z){
		super(x, c, d);
		this.angka = z;
	}
	
	public void get_angka(){
		System.out.println(this.angka);
	}
	
	@Override
	
	public void tampil3(){
		System.out.println("nama = " + nama);
		System.out.println("umur = " + umur);
		System.out.println("angka = " + angka);
	}
	
	public static void main(String[] args)
	{
		inheritance_child data1 = new inheritance_child("dyland", 20, 10, 50);
		
		data1.tampil();
		
		data1.get_angka();
		
		data1.tampil2();
		
		data1.tampil3();
		
	}
}