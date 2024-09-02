import java.io.*;
import java.util.*;

public class tugas {
    public static void main(String[] args) throws IOException {
        BufferedWriter test = new BufferedWriter(new FileWriter("anin/src/hai.txt"));

        test.write("hai nama saya anin");
        test.close();

        BufferedReader test2 = new BufferedReader(new FileReader("anin/src/hai.txt"));
        String bet;
        while ((bet = test2.readLine()) != null) {
            System.out.println(bet);
        }
        test2.close();

        String filename = "anin/src/hai.txt";
        String kalimat1 = "harry potter";
        String kalimat2 = "bleach";
        String kalimat3 = "beauty and the beast";

        BufferedWriter mat = new BufferedWriter(new FileWriter(filename, true));

        mat.newLine();
        mat.write(kalimat1);
        mat.newLine();
        mat.write(kalimat2);
        mat.newLine();
        mat.write(kalimat3);
        mat.close();

        BufferedReader testt = new BufferedReader(new FileReader("anin/src/hai.txt"));
        ArrayList<String> simpan = new ArrayList<>();
        String kata; 
        while ((kata = testt.readLine()) != null) {
            simpan.add(kata);
        }
        testt.close();

        // Mencari dan menampilkan kata dengan jumlah karakter terpanjang
        String kataTerpanjang = "";
        for (String str : simpan) {
            if (str.length() > kataTerpanjang.length()) {
                kataTerpanjang = str;
            }
        }
        System.out.println("Kata dengan jumlah karakter terpanjang: " + kataTerpanjang);
    }
}