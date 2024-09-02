import java.util.Scanner;
import java.io.Console;

public class coba3
{
   public static void main(String[] args)
   {
	   Scanner in = new Scanner(System.in);
	   Console con = System.console();
	   
	   // scanner
	   
	   System.out.print("masukan nama scanner : ");
	   String nama = in.nextLine();
	   
	   System.out.print("masukan umur scanner : ");
	   int umur = in.nextInt();
	   
	   System.out.println("nama = " + nama + ", umur = " + umur);
	   
	   // console
	   
	   String nama2 = con.readLine("Masukan nama console : ");
	   
	   String angka = con.readLine("Masukan angka console : ");
	   int ubah_angka = Integer.parseInt(angka);
	   
	   System.out.println("nama = " + nama2 + ", angka = " + ubah_angka);
	   
	   // formatting
	   
	   String nama3 = "soso";
	   double angka2 = 897.7878;
	   int angka3 = 10;
	   
	   System.out.printf("angka = %f \n", angka2);
	   System.out.printf("nama = %s, angka = %.2f \n", nama3, angka2);
	   System.out.printf("angka = %d \n", angka3);
	   
	   // assignment1
	   
	   String nama4 = con.readLine("masukan nama : ");
	   
	   if(nama4.equal("agung")){
		   System.out.printf("nama sama");
	   }
	   else{
		    System.out.printf("nama sama");
	   }
	   
	   // assignment2
	   
	   int angka5 = 15;
	   
	   if (angka5 > 10 && angka5 < 20){
		   System.out.println("angka diantara 10 dan 20");
	   }
	   else{
		   System.out.println("angka diluar 10 dan 20");
	   }
   }
}