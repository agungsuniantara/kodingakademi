import java.io.FileWriter;
import java.io.IOException;
import java.io.BufferedWriter;

public class write_append_file
{
	public static void main(String[] args){
		try{
			FileWriter berkas = new FileWriter("hasil.txt");
			BufferedWriter br = new BufferedWriter(berkas);
			br.write("ini teks tambahan 2");
			
			br.close();
			
			System.out.println("berhasil membuat tulisan");
		}
		catch (Exception e){
			System.out.println("ada kesalahan");
		}
	}
}