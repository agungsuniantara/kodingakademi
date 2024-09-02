package abstraction;

// Abstract class
abstract class Shape {
    // Variabel instance
    protected String color;
    
    // Constructor
    public Shape(String color) {
        this.color = color;
    }
    
    // Abstract method
    public abstract double calculateArea();
    
    // Concrete method
    public void displayColor() {
        System.out.println("Color: " + color);
    }
}

// Subclass Rectangle
class Rectangle extends Shape {
    private double width;
    private double height;
    
    // Constructor
    public Rectangle(String color, double width, double height) {
        super(color);
        this.width = width;
        this.height = height;
    }
    
    // Implementasi metode calculateArea dari Shape
    @Override
    public double calculateArea() {
        return width * height;
    }
}

public class abstraction_java {
    public static void main(String[] args) {
        // Membuat objek Rectangle
        Rectangle rectangle = new Rectangle("red", 5, 3);
        
        // Memanggil metode displayColor dan calculateArea
        rectangle.displayColor(); // Output: Color: red
        System.out.println("Area of rectangle: " + rectangle.calculateArea()); // Output: Area of rectangle: 15.0
    }
}
