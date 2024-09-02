package harry.model;

import java.util.Timer;
import java.util.TimerTask;
import java.util.*;

interface ZombieAction{
    void displayInfo();
}

public class Zombie implements ZombieAction{
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

    public static Zombie createZombie(String type) {
        try {
            if (type.equalsIgnoreCase("normal zombie")) {
                return new Zombie("normal zombie", 125, 100, 1, false);
            } else if (type.equalsIgnoreCase("conehead Zombie")) {
                return new Zombie("conehead zombie", 250, 100, 1, false);
            } else if (type.equalsIgnoreCase("pole zombie")) {
                return new Zombie("pole vaulting zombie", 175, 100, 1, false);
            } else if (type.equalsIgnoreCase("buckethead zombie")) {
                return new Zombie("buckethead zombie", 300, 100, 1, false);
            } else if (type.equalsIgnoreCase("ducky tube zombie")) {
                return new Zombie("ducky tube zombie", 100, 100, 1, true);
            }else if (type.equalsIgnoreCase("rider zombie")) {
                return new Zombie("rider zombie", 175, 100, 1, true);
            }
            else{
                return null;
            }
        } catch (Exception e) {
            System.out.println("Error saat membuat zombie: " + e.getMessage());
            return null;
        }
    }

    @Override
    public void displayInfo() {
        try {
            System.out.println(name + " (health: " + health + " attackDamage: " + attackDamage + " attackSpeed: " + attackSpeed + " isAquatic: " + isAquatic + ")");
        } catch (Exception e) {
            System.out.println("Error saat menampilkan informasi zombie: " + e.getMessage());
        }
    }

    public void setName(String name){
        this.name = name;
    }

    public void setHealth(int health){
        this.health = health;
    }

    public void setattackDamage(int attackDamage){
        this.attackDamage = attackDamage;
    }

    public void setattackSpeed(int attackSpeed){
        this.attackSpeed = attackSpeed;
    }

    public String getName(){ 
        return name;
    }

    public int getHealth(){ 
        return health;
    }

    public int getAttack_Damage(){ 
        return attackDamage;
    }

    public int getAttack_Spped(){ 
        return attackSpeed;
    }

    public boolean getisAquaticn(){ 
        return isAquatic;
    }
}
