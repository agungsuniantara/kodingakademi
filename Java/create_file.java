import java.io.File;
import java.io.IOException;

public class create_file
{
	public static void main(String[] args){
		try{
			File berkas = new File("hasil.txt");
			if (berkas.createNewFile()){
				System.out.println("nama file : " + berkas.getName());
			}
			else{
				System.out.println("file sudah ada");
			}
		}
		catch (Exception e){
			System.out.println("ada kesalahan");
		}
	}
}