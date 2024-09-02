import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        // perulangan for
        System.out.println("for increment + : ");

        for (int a = 0; a < 3; a++){ // a = 0, a = 1, a = 2, a = 3
            System.out.println("angka : " + a);
        }

        System.out.println("for increment - : ");

        for (int a = 10; a > 6; a--){ // a = 10, a = 9
            System.out.println("angka : " + a);
        }

        // perulangan for di dalam for
        System.out.println("for di dalam for : ");

        for (int c = 0; c < 3; c++){ // c = 0
            System.out.println("for di luar : " + c); 
            for (int a = 0; a < 3; a++){ // a = 0, a = 1, a = 2
                System.out.println("for di dalam : " + a);
            }
        }

        // perulangan while
        System.out.println("while loop : ");

        // contoh 1
        while(true){
            System.out.println("test");
            break;
        }

        //contoh 2
        int angka = 0;
        while(angka < 3){
            System.out.println("angka : " + angka);
            angka += 1;
        }

        // perulangan do while 

        int number = 0;
        System.out.println("do while loop : ");
        
        do {
            System.out.println("test");
            number += 1;
        }
        while(number > 3); // false

        // challange
        // 1. gunakan for untuk menampilkan bintang dimana kolom = 3, baris = 4.
        // 2. gunakan while untuk menanyakan pertanyaan, jika tidak maka while akan berhenti.

        // challange 1
        System.out.println("challange 1 : ");
        
        int baris = 4;
        int kolom = 3;

        for (int i = 0; i < baris; i++){
            // System.out.println("baris : " + i);
            for (int a = 0; a < kolom; a++){
                System.out.print("*");
            }
            System.out.println("");
        }

        // challange 2

        System.out.println("challange 2 : ");
        Scanner scan = new Scanner(System.in);

        while(true){
            System.out.println("Apakah ingin mengulangi ? ");
            String kondisi = scan.nextLine();
            
            if (kondisi.equals("tidak")){
                break;
            }
        }

        scan.close();
    }
}
