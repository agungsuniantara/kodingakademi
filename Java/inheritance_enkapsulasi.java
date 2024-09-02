public class inheritance_enkapsulasi
{
	public static void main(String[] args)
	{
		inheritance data = new inheritance("dylan", 20,10);
		
		// jika tampil2 private maka error
		// jika tampil2 public maka tidak error
		data.tampil2();
		
		data.tampil();
	}
}