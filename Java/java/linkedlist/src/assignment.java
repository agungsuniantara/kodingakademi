import java.util.*;

public class assignment {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Tipe data linkedlist : ");
        System.out.println("1. Linkedlist string");
        System.out.println("2. Linkedlist int");
        System.out.println("3. Linkedlist double");
        System.out.println("4. Linkedlist boolean");

        System.out.print("Pilih tipe data linkedlist : ");
        int pilih = scan.nextInt();

        if (pilih == 1){
            LinkedList<String> str = new LinkedList<>();

            System.out.print("Banyak data : ");
            int data = scan.nextInt();

            for (int i = 1; i <= data; i++){
                System.out.print("data ke-" + i + " : ");
                String masuk = scan.next();
                str.add(masuk);
            }

            System.out.println("linkedlist string : " + str);
        }
        else if(pilih == 2){
            LinkedList<Integer> integer = new LinkedList<>();

            System.out.print("Banyak data : ");
            int data = scan.nextInt();

            for (int i = 1; i <= data; i++){
                System.out.print("data ke-" + i + " : ");
                int masuk = scan.nextInt();
                integer.add(masuk);
            }

            System.out.println("linkedlist int : " + integer);
        }
        else if(pilih == 3){
            LinkedList<Double> doub = new LinkedList<>();

            System.out.print("Banyak data : ");
            int data = scan.nextInt();

            for (int i = 1; i <= data; i++){
                System.out.print("data ke-" + i + " : ");
                Double masuk = scan.nextDouble();
                doub.add(masuk);
            }

            System.out.println("linkedlist double : " + doub);
        }
        else if(pilih == 4){
            LinkedList<Boolean> bool = new LinkedList<>();

            System.out.print("Banyak data : ");
            int data = scan.nextInt();

            for (int i = 1; i <= data; i++){
                System.out.print("data ke-" + i + " : ");
                boolean masuk = scan.nextBoolean();
                bool.add(masuk);
            }

            System.out.println("linkedlist boolean : " + bool);
        }
        else{
            System.out.println("Tipe data tidak sesuai");
        }

        scan.close();
    }
}
