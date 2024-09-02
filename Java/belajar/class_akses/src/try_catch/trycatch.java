package try_catch;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class trycatch {
    public static void main(String[] args) {
        // Contoh NullPointerException
        String str = null;
        try {
            int length = str.length(); // Akan menimbulkan NullPointerException
        } catch (NullPointerException e) {
            System.out.println("NullPointerException: " + e.getMessage());
        }
        
        // Contoh ArrayIndexOutOfBoundsException
        int[] arr = {1, 2, 3};
        try {
            int value = arr[3]; // Akan menimbulkan ArrayIndexOutOfBoundsException
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("ArrayIndexOutOfBoundsException: " + e.getMessage());
        }
        
        // Contoh FileNotFoundException & IOException
        try {
            BufferedReader reader = new BufferedReader(new FileReader("nonexistentfile.txt"));
            String line = reader.readLine();
            System.out.println(line); // Akan menimbulkan FileNotFoundException & IOException
        } catch (IOException e) {
            System.out.println("IOException: " + e.getMessage());
        }
        
        // Contoh NumberFormatException
        String strNumber = "abc";
        try {
            int number = Integer.parseInt(strNumber); // Akan menimbulkan NumberFormatException
        } catch (NumberFormatException e) {
            System.out.println("NumberFormatException: " + e.getMessage());
        }

        int angka = 10;
        try {
            int result = angka - 10; 
            System.out.println(result);
        } catch (ArithmeticException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
