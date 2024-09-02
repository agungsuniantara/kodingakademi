import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class read_file
{
	public static void main(String[] args){
		try{
			File berkas = new File("hasil.txt");
			Scanner baca = new Scanner(berkas);
			while(baca.hasNextLine()){
				String data = baca.nextLine();
				System.out.println(data);
			}
			baca.close();
		}
		catch (Exception e){
			System.out.println("ada kesalahan");
		}
	}
}