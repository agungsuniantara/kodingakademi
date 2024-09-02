package interface_javaa;

// Interface untuk bentuk geometris
interface Shape {
    // Metode untuk menghitung luas
    double calculateArea();
    
    // Metode untuk menghitung keliling
    double calculatePerimeter();
    
    // Metode untuk menggambar bentuk
    void draw();
}

// Kelas Lingkaran yang mengimplementasikan interface Shape
class Circle implements Shape {
    private double radius;
    
    // Constructor
    public Circle(double radius) {
        this.radius = radius;
    }
    
    // Implementasi metode calculateArea dari interface Shape
    @Override
    public double calculateArea() {
        return Math.PI * radius * radius;
    }
    
    // Implementasi metode calculatePerimeter dari interface Shape
    @Override
    public double calculatePerimeter() {
        return 2 * Math.PI * radius;
    }
    
    // Implementasi metode draw dari interface Shape
    @Override
    public void draw() {
        System.out.println("Drawing circle with radius " + radius);
    }
}

// Kelas Persegi yang mengimplementasikan interface Shape
class Square implements Shape {
    private double side;
    
    // Constructor
    public Square(double side) {
        this.side = side;
    }
    
    // Implementasi metode calculateArea dari interface Shape
    @Override
    public double calculateArea() {
        return side * side;
    }
    
    // Implementasi metode calculatePerimeter dari interface Shape
    @Override
    public double calculatePerimeter() {
        return 4 * side;
    }
    
    // Implementasi metode draw dari interface Shape
    @Override
    public void draw() {
        System.out.println("Drawing square with side " + side);
    }
}

public class interface_java {
    public static void main(String[] args) {
       // Membuat objek Lingkaran
        Circle circle = new Circle(5);
        
        // Memanggil metode calculateArea, calculatePerimeter, dan draw
        System.out.println("Area of circle: " + circle.calculateArea()); // Output: Area of circle: 78.53981633974483
        System.out.println("Perimeter of circle: " + circle.calculatePerimeter()); // Output: Perimeter of circle: 31.41592653589793
        circle.draw(); // Output: Drawing circle with radius 5
        
        // Membuat objek Persegi
        Square square = new Square(4);
        
        // Memanggil metode calculateArea, calculatePerimeter, dan draw
        System.out.println("Area of square: " + square.calculateArea()); // Output: Area of square: 16.0
        System.out.println("Perimeter of square: " + square.calculatePerimeter()); // Output: Perimeter of square: 16.0
        square.draw(); // Output: Drawing square with side 4
    }
}
