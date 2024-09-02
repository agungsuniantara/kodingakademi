public class arrayassignment2
{
	public static void main(String[] args)
	{
		int[] angka = {1,2,3,4,5,6};
		int[] ganjil = new int[3];
		int[] genap = new int[3];
		
		int index_genap = 0;
		int index_ganjil = 0;
		
		for (int i = 0; i < angka.length; i++){
			if (angka[i] % 2 == 0){
				genap[index_genap] = angka[i];
				index_genap += 1;
			}
			else{
				ganjil[index_ganjil] = angka[i];
				index_ganjil += 1;
			}
			
		}
		
		System.out.println("genap : ");
		for (int i = 0; i < genap.length; i++){
			System.out.println(genap[i]);
		}
		
		System.out.println("ganjil : ");
		for (int i = 0; i < ganjil.length; i++){
			System.out.println(ganjil[i]);
		}
	}
}