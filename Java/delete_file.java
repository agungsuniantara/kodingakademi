import java.io.File;
import java.io.IOException;

public class delete_file
{
	public static void main(String[] args){
		try{
			File berkas = new File("hasil.txt");
			if (berkas.delete()){
				System.out.println("berkas berhasil di delete");
			}
			else{
				System.out.println("gagal di hapus");
			}
		}
		catch (Exception e){
			System.out.println("ada kesalahan");
		}
	}
}