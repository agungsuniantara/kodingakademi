import java.io.File;
import java.io.IOException;
import java.io.FileWriter;
import java.util.Scanner;
import java.util.Arrays;


public class assignment_read_write_file
{
	public static void main(String[] args){
        try {
			File berkas = new File("mynumbers.txt");
			berkas.createNewFile();
			
			File directoryPath = new File("mydata/2019");
			String contents[] = directoryPath.list();
			System.out.println(Arrays.toString(contents));
			
			FileWriter tulis = new FileWriter("mynumbers.txt");
			tulis.write(Arrays.toString(contents));
			tulis.close();
			
        } catch (Exception e) {
            System.out.println("ada kesalahan");
        }
	}
}