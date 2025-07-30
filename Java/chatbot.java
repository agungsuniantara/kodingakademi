import java.util.Scanner;

public class chatbot {
    public static void tambah(int a, int b){
        int hasil = a + b;
        System.out.println("hasil = " + hasil);
    }

    public static void kurang(int a, int b){
        int hasil = a - b;
        System.out.println("hasil = " + hasil);
    }

    public static void main(String[] args) {
        while (true) { 
            Scanner scan = new Scanner(System.in);
            System.out.println("Welcome in chatbot my name is oracle");
            System.out.println("Please write your name : ");
            String nama = scan.nextLine();
            System.out.println("Halo " + nama + " menu yang tersedia : ");
            System.out.println("1. Tambah");
            System.out.println("2. Kali");
            System.out.println("3. Kurang");
            System.out.println("4. Bagi");

            System.out.println("Pilih menu : ");
            int pilih = scan.nextInt();

            System.out.println("Masukan angka1 : ");
            int angka1 = scan.nextInt();

            System.out.println("Masukan angka2 : ");
            int angka2 = scan.nextInt();

            if (pilih == 1){
                tambah(angka1, angka2);
            }
            else if(pilih == 2){
                kurang(angka1, angka2);
            }
        }
    }
}
