import java.util.Scanner;

public class conditionalstatement
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		String tampil = "hello world";
		
		System.out.println("for dengan i++ : ");
		for (int i = 0; i < 5; i++){
			System.out.println(tampil + " ada pada index ke-" + i);
		}
		
		System.out.println("for dengan i-- : ");
		for (int i = 5; i > 0; i--){
			System.out.println(tampil + " ada pada index ke-" + i);
		}
		
		System.out.println("for didalam for : ");
		for (int i = 0; i < 5; i++){
			System.out.println("for luar");
			for (int c = 0; c < 3; c++){
				System.out.print("for dalam, ");
			}
			System.out.println("\n");
		}
		
		System.out.println("perulangan while : ");
		while(true){
			System.out.print("masukan nama : ");
			String nama = in.nextLine();
			
			if (nama.equals("agung")){
				System.out.println("benar");
			}
			else{
				System.out.println("Salah");
			}
			
			System.out.print("keluar sistem ? ");
			String kondisi = in.nextLine();
			
			if (kondisi.equals("ya")){
				break;
			}
		}
		
		System.out.println("switch : ");
		
		System.out.print("masukan angka : ");
		int angka = in.nextInt();
		
		switch(angka){
			case 1:
				System.out.println("pick 1");
				break;
			case 2:
				System.out.println("pick 2");
				break;
			case 3:
				System.out.println("pick 3");
				break;
			case 4:
				System.out.println("pick 4");
				break;
			default:
				System.out.println("case tidak ada !");
				break;
		}
	}
}