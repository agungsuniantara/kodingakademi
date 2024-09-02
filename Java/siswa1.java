public class siswa1 extends akademik
{
	int cash;
	
	public siswa1(int a, String b, String c, int d, int e, int f){
		super(a,b,c,d,e);
		this.cash = f;
	}
	
	@Override
	
	public void bayar(){
		int kembalian = cash - bayar;
		System.out.println("kembalian = " + kembalian);
	}
	
	public static void main(String[] args)
	{
		siswa1 data = new siswa1(1, "agung", "denpasar", 20, 10000, 20000);
		
		data.tampil_data();
		data.bayar();
	}
}