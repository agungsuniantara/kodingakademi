public class inheritance_child2 extends inheritance
{
	int angka;
	
	public inheritance_child2(String x, int c, int d, int z){
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
		System.out.println("abstrak 3");
	}
	
	public static void main(String[] args)
	{
		inheritance_child2 data2 = new inheritance_child2("dyland", 20, 10, 50);
		
		data2.tampil();
		
		data2.get_angka();
		
		data2.tampil2();
		
		data2.tampil3();
	}
}