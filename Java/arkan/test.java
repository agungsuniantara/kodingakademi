public class test {
    public static void main(String[] args) {
        int angka = 1; // 2
        System.out.println("angka = " + angka);
        angka += 1; // angka = angka + 1
        System.out.println("angka = " + angka);
        angka -= 10;
        System.out.println("angka = " + angka);
        angka %= 2;
        System.out.println("angka = " + angka);

        int num1 = 10;
        int num2 = 20;

        boolean benar = num1 < num2;
        boolean salah = num1 > num2;
        boolean sama = num1 == num2;
        System.out.println(benar);
        System.out.println(salah);
        System.out.println(sama);
    }
}
