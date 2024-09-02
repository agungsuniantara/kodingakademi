package polymorphism;

class Calculator {
    // Metode overloading untuk penjumlahan dengan dua parameter int
    public int add(int a, int b) {
        return a + b;
    }
    
    // Metode overloading untuk penjumlahan dengan tiga parameter int
    public int add(int a, int b, int c) {
        return a + b + c;
    }

    // Metode overloading untuk penjumlahan dengan dua parameter double
    public double add(double a, double b) {
        return a + b;
    }
}

public class overloadin_java {
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        
        // Memanggil metode add() dengan dua parameter int
        int sum1 = calc.add(5, 10);
        System.out.println("Addition of 5 and 10: " + sum1);
        
        // Memanggil metode add() dengan tiga parameter int
        int sum2 = calc.add(5, 10, 15);
        System.out.println("Addition of 5, 10, and 15: " + sum2);
        
        // Memanggil metode add() dengan dua parameter double
        double sum3 = calc.add(3.5, 2.5);
        System.out.println("Addition of 3.5 and 2.5: " + sum3);
    }
}
