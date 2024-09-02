package plant_vs_zombie.model;

import java.util.Timer;
import java.util.TimerTask;

public class Zombie{
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
        if (type.toLowerCase().equals("normal zombie")) {
            return new Zombie("Normal Zombie", 125, 100, 1, false);
        }
        else if (type.toLowerCase().equals("Conehead Zombie")) {
            return new Zombie("Normal Zombie", 250, 100, 1, false);
        }
        else if (type.toLowerCase().equals("Pole Vaulting Zombie")) {
            return new Zombie("Pole Vaulting Zombie", 175, 100, 1, false);
        }
        else if (type.toLowerCase().equals("Buckethead Zombie")) {
            return new Zombie("Buckethead Zombie", 300, 100, 1, false);
        }
        else if (type.toLowerCase().equals("Ducky Tube Zombie")) {
            return new Zombie("Ducky Tube Zombiee", 100, 100, 1, false);
        }
        else if (type.toLowerCase().equals("Dolphin Rider Zombie")) {
            return new Zombie("Dolphin Rider Zombie", 175, 100, 1, true);
        }
        return null;
    }

    public void move() {
        // Gerakkan zombie ke depan sesuai dengan kecepatannya
        Timer timer = new Timer();
        timer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {
                // Jika zombie masih hidup, maju ke depan
                if (health > 0) {
                    System.out.println("Zombie bergerak ke depan");
                } else {
                    // Jika zombie sudah mati, batalkan thread
                    timer.cancel();
                }
            }
        }, 0, attackSpeed * 1000); // Konversi ke milidetik
    }

    public void attackPlant(Tumbuhan plant) {
        Timer timer = new Timer();
        timer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {
                // Serang tanaman sesuai dengan attack damage dan attack speed zombie
                plant.setHealth(plant.getHealth() - attackDamage);
            }
        }, 0, attackSpeed * 1000); // Konversi ke milidetik
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
