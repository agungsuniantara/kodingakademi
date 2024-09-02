import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        // operator aritmatika

        int z = 10;
        int w = 50;

        int pertambahan = z + w;
        int pengurangan = z - w;
        int pembagian = z / w;
        int perkalian = z * w;
        int modulus = z % w;

        System.out.println("Operator aritmatika : ");
        System.out.println(pertambahan);
        System.out.println(pengurangan);
        System.out.println(pembagian);
        System.out.println(perkalian);
        System.out.println(modulus);

        // operator penugasan

        int a = 20; // 30 // 25 // 50 // 25 // 1

        a += 10;
        a -= 5;
        a *= 2;
        a /= 2;
        a %= 2;

        System.out.println("Operator aritmatika : ");
        System.out.println(a);

        // operator pembanding

        int b = 30;
        int c = 40;

        boolean samaDengan = b == c; // false
        boolean tidakSamaDengan = b != c; // true
        boolean lebihBesar = b > c; // false
        boolean lebihKecil = b < c; // true
        boolean lebihBesarSama = b >= c; // false
        boolean lebihKecilSama = b <= c; // true

        System.out.println("Operator pembanding : ");
        System.out.println(samaDengan);
        System.out.println(tidakSamaDengan);
        System.out.println(lebihBesar);
        System.out.println(lebihKecil);
        System.out.println(lebihBesarSama);
        System.out.println(lebihKecilSama);

        // operator logika

        int d = 50;
        int e = 80;
        int f = 30;

        boolean and = (d > f) && (e < f); // false
        boolean or = (d > f) || (e < f); // true
        boolean not = !(d > f); // false

        System.out.println("Operator logika : ");
        System.out.println(and);
        System.out.println(or);
        System.out.println(not);

        // operator bitwise

        int h = 20;
        int g = 30;

        int bitAnd = h & g;
        int bitOr = h | g;
        int bitXor = h ^ g;
        int bitNot = ~h;
        int bitLeftShift = h << 1;
        int bitRightShift = h >> 1;

        System.out.println("Operator bitwise : ");
        System.out.println(bitAnd);
        System.out.println(bitOr);
        System.out.println(bitXor);
        System.out.println(bitNot);
        System.out.println(bitLeftShift);
        System.out.println(bitRightShift);

        // operator ternary

        int k = 10;
        int l = 30;

        String hasil = (k > l) ? "benar" : "salah";
        int angka = (k < l) ? k : l;

        System.out.println("Operator ternary : ");
        System.out.println(hasil);
        System.out.println(angka);

        // Scanner

        System.out.println("Fungsi scanner : ");

        Scanner scan = new Scanner(System.in);

        System.out.print("masukan nama : ");
        String nama = scan.nextLine();

        System.out.print("masukan angka : ");
        Double angka2 = scan.nextDouble();

        System.out.print("masukan angka int : ");
        int angka3 = scan.nextInt();

        System.out.println("Nama = " + nama);
        System.out.println("Angka double = " + angka2);
        System.out.println("Angka int = " + angka3);

        scan.close();
    }
}
