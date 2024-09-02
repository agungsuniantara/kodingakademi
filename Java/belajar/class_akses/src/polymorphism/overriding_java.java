package polymorphism;

// Superclass
class Animal {
    public void makeSound() {
        System.out.println("Animal makes a sound");
    }
}

// Subclass
class Dog extends Animal {
    // Overriding metode makeSound dari superclass Animal
    @Override
    public void makeSound() {
        System.out.println("Dog barks");
    }
}

// Subclass lain
class Cat extends Animal {
    // Overriding metode makeSound dari superclass Animal
    @Override
    public void makeSound() {
        System.out.println("Cat meows");
    }
}

public class overriding_java {
    public static void main(String[] args) {
        Animal animal1 = new Dog(); // Polymorphism
        Animal animal2 = new Cat(); // Polymorphism
        
        animal1.makeSound(); // Memanggil metode makeSound() dari objek Dog
        animal2.makeSound(); // Memanggil metode makeSound() dari objek Cat
    }
}
