import java.io.FileWriter;
import java.io.IOException;

public class write_file
{
	public static void main(String[] args){
		try{
			FileWriter berkas = new FileWriter("hasil.txt");
			berkas.write("tulisan 2");
			berkas.close();
			System.out.println("berhasil membuat tulisan");
		}
		catch (Exception e){
			System.out.println("ada kesalahan");
		}
	}
}