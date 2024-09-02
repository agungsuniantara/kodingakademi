public class arrayassignment
{
	public static void main(String[] args)
	{
		// kecil ke besar
		
		System.out.println("Kecil ke besar : ");
		
		String[] nama = {"terima kasih","halo","saya"};
		
		for (int i = 0; i < 3 - 1; i++){
			int min = i;
			
			for (int j = i + 1; j < 3; j++){
				if (nama[j].length() < nama[min].length()){
					min = j;
				}
			}
			
			String temp = nama[min];
			nama[min] = nama[i];
			nama[i] = temp;
		}
		
		for (int i = 0; i < 3; i++) {
            System.out.println(nama[i]);
        }
		
		System.out.println("Besar ke kecil : ");
		
		// besar ke kecil
		
		String[] nama2 = {"halo","saya","terima kasih"};
		
		for (int i = 0; i < 3 - 1; i++){
			int min = i;
			
			for (int j = i + 1; j < 3; j++){
				if (nama2[j].length() > nama2[min].length()){
					min = j;
				}
			}
			
			String temp = nama2[min];
			nama2[min] = nama2[i];
			nama2[i] = temp;
		}
		
		for (int i = 0; i < 3; i++) {
            System.out.println(nama2[i]);
        }
	}
}