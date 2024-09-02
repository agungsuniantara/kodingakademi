import java.util.*;

public class assignment {
    public static void main(String[] args) {
        ArrayList<String> data = new ArrayList<>();
        Scanner scan = new Scanner(System.in);

        System.out.print("Banyak data : ");
        int angka = scan.nextInt();

        for (int i = 0; i < angka; i++){
            System.out.print("index " + i + ": ");
            String temp = scan.next();

            data.add(temp);
        }

        System.out.println("data = " + data);

        for (int i = 0; i < angka; i++){
            if (i % 2 != 0){
                data.set(i, "Hewan");
            }
        }

        System.out.println("ganti data index ganjil : ");
        System.out.println("data = " + data);

        scan.close();
    }
}
