import java.util.Scanner;

public class coba
{
   public static void main(String[] args)
   {
      Scanner in = new Scanner(System.in);
	  
	  System.out.print("masukan operator : ");
	  String operator = in.nextLine();
	  
	  System.out.print("masukan angka1 : ");
	  int angka1 = in.nextInt();
	  
	  System.out.print("masukan angka2 : ");
	  int angka2 = in.nextInt();
	  
	  if (operator.equals("+")){
		  int hasil = angka1 + angka2;
		  System.out.println("hasil = " + hasil);
	  }
	  else if(operator.equals("-")){
		  int hasil = angka1 - angka2;
		  System.out.println("hasil = " + hasil);
	  }
	  else{
		  System.out.println("terjadi kesalahan !");
	  }
   }
}