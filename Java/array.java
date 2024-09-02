public class array
{
	public static void main(String[] args)
	{
		// inisialisasi array 1D
		int[] angka = {1,2,3,4,5};
		String[] huruf = {"agung", "wahyu"};
		
		// ganti value array
		angka[0] = 100;
		huruf[0] = "kekeyi";
		
		// tampil value array
		System.out.println(angka[0]);
		System.out.println(angka[1]);
		System.out.println(angka.length);
		System.out.println(huruf[0]);
		System.out.println(huruf[1]);
		
		// for array
		for (int i = 0; i < angka.length; i++){
			System.out.println(angka[i]);
		}
		
		// inisialisasi array 2D
		
		int[][] myNumbers = { {1, 2, 3, 4}, {5, 6, 7} }; // baris dan kolom
		System.out.println(myNumbers[1][1]);
		
	}
}