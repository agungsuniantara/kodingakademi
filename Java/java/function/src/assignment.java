import java.util.*;

public class assignment {
    public static void data_diri(String nama, String alamat, String umur){
        System.out.println("Nama : " + nama);
        System.out.println("Alamat : " + alamat);
        System.out.println("Umur : " + umur);
    }

    public static double kalkulator(double angka1, double angka2, String operator){
        double hasil = 0;

        if (operator.equals("+")){
            hasil += angka1 + angka2;
        }
        else if(operator.equals("-")){
            hasil += angka1 - angka2;
        }
        else if(operator.equals("/")){
            hasil += angka1 / angka2;
        }
        else if(operator.equals("*")){
            hasil += angka1 * angka2;
        }

        return hasil;
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Masukan nama : ");
        String nama = scan.next();
        System.out.print("Masukan alamat : ");
        String alamat = scan.next();
        System.out.print("Masukan umur : ");
        String umur = scan.next();

        scan.next();

        System.out.print("Masukan angka 1 : ");
        double angka1 = scan.nextDouble();
        System.out.print("Masukan angka 2 : ");
        double angka2 = scan.nextDouble();
        System.out.print("Masukan operator : ");
        String operator = scan.next();

        data_diri(nama, alamat, umur);

        System.out.println("Angka 1 : " + angka1);
        System.out.println("Angka 2 : " + angka2);
        System.out.println("Operator : " + operator);
        double simpan = kalkulator(angka1, angka2, operator);
        System.out.println("Hasil = " + simpan);

        scan.close();
    }
}
