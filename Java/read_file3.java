import java.io.File;
import java.util.ArrayList;
import java.util.Scanner;

public class read_file3 {
    public static void main(String[] args) {
        ArrayList<String> lines = new ArrayList<>(); 
        int maxLength = 0; // 7

        try {
            File berkas = new File("readfile2.txt");
            Scanner baca = new Scanner(berkas);

            while(baca.hasNextLine()) {
                String data = baca.nextLine();
                lines.add(data);
                if (data.length() > maxLength) {
                    maxLength = data.length();
                }
            }

            for (String line : lines) {
                int letterCount = 0;

                if (line.length() == maxLength) {
                    System.out.println("kata terbesar : " + line);
                }
                
                // Hitung jumlah yang huruf bukan angka atau simbol
                for (int i = 0; i < line.length(); i++) {
                    char c = line.charAt(i);
                    if (Character.isLetter(c)) { 
                        letterCount++;
                    }
                }
                System.out.println("Kalimat: \"" + line + "\"");
                System.out.println("Jumlah huruf: " + letterCount);
            }

			baca.close();
		}
		catch (Exception e){
			System.out.println("ada kesalahan");
		}
    }
}
