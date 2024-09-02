interface Action_Tumbuhan {
    void displayInfo(); // abstract
    // void produce_sun();
    // void attack();
}

interface Action_Zombie {
    void displayInfo(); // abstract
    // void attack();
    // void jumpable();
}

class Tumbuhan implements Action_Tumbuhan {
    private String name; // encapsulation
    private int cost;
    private int health;
    private int attackDamage;
    private int attackSpeed;
    private int range;
    private int cooldown;

    public Tumbuhan(String name, int cost, int health, int attackDamage, int attackSpeed, int range, int cooldown) {
        this.name = name;
        this.cost = cost;
        this.health = health;
        this.attackDamage = attackDamage;
        this.attackSpeed = attackSpeed;
        this.range = range;
        this.cooldown = cooldown;
    }

    @Override
    public void displayInfo() { // polymorphism override
        System.out.println("Name: " + name + ", Cost: " + cost + ", Health: " + health + ", Attack Damage: " + attackDamage + ", Attack Speed: " + attackSpeed + ", Range: " + range + ", Cooldown: " + cooldown);
    }

    public String getName(){ // encapsulation getters
        return name;
    }
}

class Zombie implements Action_Zombie {
    private String name; // encapsulation
    private int health;
    private int attackDamage;
    private int attackSpeed;
    private boolean isAquatic;

    public Zombie(String name, int health, int attackDamage, int attackSpeed, boolean isAquatic) {
        this.name = name;
        this.health = health;
        this.attackDamage = attackDamage;
        this.attackSpeed = attackSpeed;
        this.isAquatic = isAquatic;
    }

    @Override
    public void displayInfo() { // polymorphism override
        System.out.println("Name: " + name + ", Health: " + health + ", Attack Damage: " + attackDamage + ", Attack Speed: " + attackSpeed + ", isAquatic: " + isAquatic);
    }

    public String getName(){ // encapsulation getters
        return name;
    }
}

// Factory untuk menciptakan tumbuhan
class PlantFactory {
    public static Tumbuhan createPlant(String plantType) {
        if (plantType.toLowerCase().equals("sunflower")) {
            return new Tumbuhan("Sunflower", 50, 100, 0, 0, 0, 0);
        }
        else if (plantType.toLowerCase().equals("peashooter")) {
            return new Tumbuhan("Peashooter", 100, 100, 25, 4, -1, 10);
        }
        return null;
    }
}

// Factory untuk menciptakan objek zombie
class ZombieFactory {
    public static Zombie createZombie(String type) {
        if (type.toLowerCase().equals("normal zombie")) {
            return new Zombie("Normal Zombie", 125, 100, 1, false);
        }
        return null;
    }
}

public class character{
    public static void main(String[] args) {}
}
