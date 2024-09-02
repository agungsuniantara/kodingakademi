import java.util.Scanner;
import java.io.Console;

public class stringadvanceassignment
{
   public static void main(String[] args)
   {
	  // note jalankan program pada cmd
	  
	  Scanner in = new Scanner(System.in);
	  Console cons = System.console();

      // scanner (bisa di IDE dan cmd)
      System.out.print("What is your name? ");
      String name = in.nextLine();

      System.out.print("How old are you? ");
      int age = in.nextInt();
	  
      System.out.println("Hello, " + name + ". Next year, you'll be " + (age + 1));
	  
	  
	  // console (hanya bisa di console / cmd)
	  String username = cons.readLine("User name: ");
	  
	  String umur = cons.readLine("umur : "); // console hanya menerima string, jika angka harus dirubah ke int
	  int ubah_umur = Integer.parseInt(umur);
	  
	  char[] passwd = cons.readPassword("Password: ");
	  String tampil_password = new String(passwd); // tampil password dalam array passwd
	  
	  System.out.println("Hello, " + username + ". Alamat = "+ubah_umur+". password anda = " + tampil_password);
   
   
	  // formatting output
	  
	  double x = 10000.0 / 3.0;
	  String contoh = "agung";
	  int angka2 = 50;
	  
	  System.out.printf("%f \n", x);
      System.out.printf("%.3f \n", x);
	  System.out.printf("nama = %s, umur = %d \n", contoh, angka2);
	  
	  // assignment
	  
	  // no 1
	  
	  String tampilan = cons.readLine("masukan nama : ");
	  
	  if (tampilan.equals("agung")){
		  System.out.println("nama sama");
	  }
	  else{
		  System.out.println("nama tidak sama");
	  }
	  
	  // no 2
	  
	  System.out.println("masukan angka : ");
	  int angka10 = in.nextInt();
	  
	  if (angka10 < 11){
		  System.out.println("kanak-kanak");
	  }
	  else if(angka10 > 12 && angka10 < 25){
		  System.out.println("remaja");
	  }
	  else if(angka10 > 26 && angka10 < 45){
		  System.out.println("dewasa");
	  }
	  else{
		  System.out.println("lansia");
	  }
   }
}