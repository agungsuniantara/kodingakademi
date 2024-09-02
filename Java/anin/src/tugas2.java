import java.io.*;
import java.util.*;

public class tugas2 {
    public static void main(String[] args) throws IOException {
        ArrayList<String> simpan = new ArrayList<>();
        BufferedReader testt = new BufferedReader(new FileReader("anin/src/hai.txt"));
        String kata;
        while ((kata = testt.readLine()) != null) {
            simpan.add(kata);
        }
        testt.close();
        
        for (String str : simpan) {
            for (int i = 0; i < str.length(); i++) {
                if (str.charAt(i) == 'e') {
                    System.out.print("e");
                }
            }
            System.out.println("");
        }
    }
}
