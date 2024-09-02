import java.io.File;
import java.io.IOException;
import java.io.FileWriter;
import java.util.Scanner;

public class read_write_file
{
	public static void main(String[] args){
        try {
			// create file
			File berkas = new File("baru.txt");
			berkas.createNewFile();
			
			// write file
			FileWriter tulis = new FileWriter("baru.txt");
			tulis.write("tulisan di text");
			tulis.close();
			
			// read file
			File baca = new File("baru.txt");
			Scanner r = new Scanner(baca);
			String data = r.nextLine();
			System.out.println(data);
			
        } catch (Exception e) {
            System.out.println("ada kesalahan");
        }
	}
}