package plant_vs_zombie.model;

import java.util.Timer;
import java.util.TimerTask;

public class Tumbuhan{
    private String name; 
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

    public static Tumbuhan createPlant(String plantType) {
        if (plantType.toLowerCase().equals("sunflower")) {
            return new Tumbuhan("Sunflower", 50, 100, 0, 0, 0, 0);
        }
        else if (plantType.toLowerCase().equals("peashooter")) {
            return new Tumbuhan("Peashooter", 100, 100, 25, 4, -1, 10);
        }
        else if (plantType.toLowerCase().equals("Wall nut")) {
            return new Tumbuhan("Wall nut", 50, 1000, 0, 0, 0, 20);
        }
        else if (plantType.toLowerCase().equals("Snow pea")) {
            return new Tumbuhan("Snow pea", 175, 100, 25, 4, -1, 10);
        }
        else if (plantType.toLowerCase().equals("Squash")) {
            return new Tumbuhan("Squash", 50, 100, 5000, 0, 1, 20);
        }
        else if (plantType.toLowerCase().equals("Lilypad")) {
            return new Tumbuhan("Lilypad", 25, 100, 0, 0, 0, 10);
        }
        else{
            return null;
        }
    }

   // Metode untuk menghasilkan sun
    public int produceSun() {
        if (this.name.equalsIgnoreCase("Sunflower")) {
            return 25; // Menghasilkan 25 sun
        } else {
            return 0; // Jika bukan Sunflower, tidak menghasilkan sun
        }
    }

    // Metode untuk mengurangi kecepatan zombie
    public void slow(Zombie zombie) {
        if (this.name.equalsIgnoreCase("Snow-pea")) {
            // Set kecepatan zombie menjadi setengah dari sebelumnya
            zombie.setattackSpeed(zombie.getAttack_Spped() * 2);
            // Set timer untuk mengembalikan kecepatan zombie menjadi semula setelah 3 detik
            Timer timer = new Timer();
            timer.schedule(new TimerTask() {
                @Override
                public void run() {
                    // Set kecepatan zombie kembali ke semula
                    zombie.setattackSpeed(zombie.getAttack_Spped() / 2);
                }
            }, 3000); // 3000 milidetik (3 detik)
        }
    }

    // Metode untuk melakukan instant-kill pada zombie
    public void instantKill(Zombie zombie) {
        if (this.name.equalsIgnoreCase("Squash")) {
            // Set health zombie menjadi 0 (membunuh zombie)
            zombie.setHealth(0);
        }
    } 
    
    // Metode untuk mengecek apakah tanaman dapat ditanam di air
    public boolean isAquatic() {
        return this.name.equalsIgnoreCase("Lilypad");
    }

    public void setName(String name){
        this.name = name;
    }

    public void setCost(int cost){
        this.cost = cost;
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

    public void setrange(int range){
        this.range = range;
    }

    public void setcooldown(int cooldown){
        this.cooldown = cooldown;
    }


    public String getName(){ 
        return name;
    }

    public int getCost(){ 
        return cost;
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

    public int getRange(){ 
        return range;
    }

    public int getCooldown(){ 
        return cooldown;
    }
}
