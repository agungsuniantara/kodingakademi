import java.io.File;
import java.util.ArrayList;
import java.util.Scanner;

public class read_file2 {
    public static void main(String[] args) {
        int maxLength = 0; // 7
        ArrayList<String> lines = new ArrayList<>(); // Untuk menyimpan semua baris

        try {
            File berkas = new File("readfile2.txt");
            Scanner baca = new Scanner(berkas);

            // Baca semua baris dan cari panjang maksimum
            while(baca.hasNextLine()) {
                String data = baca.nextLine();
                lines.add(data);
                if (data.length() > maxLength) {
                    maxLength = data.length();
                }
            }

            // Cetak semua baris yang memiliki panjang maksimum
            System.out.println("Kalimat terpanjang (panjang: " + maxLength + ")");
            for (String line : lines) {
                if (line.length() == maxLength) {
                    System.out.println(line);
                }
            }
			baca.close();
		}
		catch (Exception e){
			System.out.println("ada kesalahan");
		}
    }
}
