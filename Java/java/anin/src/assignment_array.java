import java.util.Scanner;

public class assignment_array {
    public static void main(String[] args) {
        int[] ganjil = new int[4];
        int[] genap = new int[4];

        Scanner in = new Scanner(System.in);

        for (int i = 0; i < 4; i++){
            System.out.println("Masukan angka : ");
            int angka = in.nextInt();

            if (angka % 2 == 0){
                genap[i] = angka;
            }
            else{
                ganjil[i] = angka;
            }
        }

        for (int i = 0; i < genap.length; i++){
            System.out.println("Data genap : " + genap[i]);
        }

        for (int i = 0; i < ganjil.length; i++){
            System.out.println("Data ganjil : " + ganjil[i]);
        }

        in.close();
    }
}
