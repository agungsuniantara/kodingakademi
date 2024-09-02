package harry.model;

import java.util.Timer;
import java.util.TimerTask;
import java.util.*;

interface PlantAction{
    void displayInfo();
}

public class Tumbuhan implements PlantAction{
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
        try {
            if (plantType.toLowerCase().equals("sunflower")) {
                return new Tumbuhan("sunflower", 50, 100, 0, 0, 0, 10);
            }
            else if (plantType.toLowerCase().equals("peashooter")) {
                return new Tumbuhan("peashooter", 100, 100, 25, 4, -1, 10);
            }
            else if (plantType.toLowerCase().equals("wallnut")) {
                return new Tumbuhan("wallnut", 50, 1000, 0, 0, 0, 20);
            }
            else if (plantType.toLowerCase().equals("snowpea")) {
                return new Tumbuhan("snowpea", 175, 100, 25, 4, -1, 10);
            }
            else if (plantType.toLowerCase().equals("squash")) {
                return new Tumbuhan("squash", 50, 100, 5000, 0, 1, 20);
            }
            else if (plantType.toLowerCase().equals("lilypad")) {
                return new Tumbuhan("lilypad", 25, 100, 0, 0, 0, 10);
            }
            else{
                return null;
            }
        } catch (Exception e) {
            System.out.println("Error saat membuat tanaman: " + e.getMessage());
            return null;
        }
    }

    @Override
    public void displayInfo() {
        try {
            System.out.println(name + " (cost: " + cost + " health: " + health + " attackDamage: " + attackDamage + " attackSpeed: " + attackSpeed + " range: " + range + " cooldown: " + cooldown + ")");
        } catch (Exception e) {
            System.out.println("Error saat menampilkan informasi: " + e.getMessage());
        }
    }

    public void attack(Map map, int x, int y, Zombie normal, Zombie conehead, Zombie pole, Zombie buckethead, Zombie ducky, Zombie dolphin) {
        if (attackSpeed > 0 && attackDamage > 0) {
            Timer timer = new Timer();
            timer.scheduleAtFixedRate(new TimerTask() {
                @Override
                public void run() {
                    for (int j = 0; j < map.grid[x].length; j++) {
                        if (map.grid[x][j] instanceof List) {
                            List<String> zombies = (List<String>) map.grid[x][j];
                            Iterator<String> zombieIterator = zombies.iterator();
                            while (zombieIterator.hasNext()) {
                                String zombieType = zombieIterator.next();
                                boolean isDead = applyDamage(zombieType, normal, conehead, pole, buckethead, ducky, dolphin);
                                if (isDead) {
                                    zombieIterator.remove();
                                }
                            }
                            if (zombies.isEmpty()) {
                                map.grid[x][j] = null;
                            }
                        }
                    }
                }
            }, 0, attackSpeed * 1000);
        }
    }

    private boolean applyDamage(String zombieType, Zombie normal, Zombie conehead, Zombie pole, Zombie buckethead, Zombie ducky, Zombie dolphin) {
        Zombie targetZombie;
        switch (zombieType) {
            case "ZN":
                targetZombie = normal;
                break;
            case "ZC":
                targetZombie = conehead;
                break;
            case "ZP":
                targetZombie = pole;
                break;
            case "ZB":
                targetZombie = buckethead;
                break;
            case "ZD":
                targetZombie = ducky;
                break;
            case "ZR":
                targetZombie = dolphin;
                break;
            default:
                return false;
        }
        targetZombie.setHealth(targetZombie.getHealth() - attackDamage);
        return targetZombie.getHealth() <= 0;
    }
    
    // Metode untuk mengurangi kecepatan zombie
    public void slow(Zombie zombie) {
        try {
            if (this.name.equalsIgnoreCase("snowpea")) {
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
        } catch (Exception e) {
            System.out.println("Error saat memperlambat zombie: " + e.getMessage());
        }
    }

    // Metode untuk melakukan instant-kill pada zombie
    public void instantKill(Zombie zombie) {
        try {
            if (this.name.equalsIgnoreCase("squash")) {
                // Set health zombie menjadi 0 (membunuh zombie)
                zombie.setHealth(0);
            }
        } catch (Exception e) {
            System.out.println("Error saat membunuh zombie: " + e.getMessage());
        }
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
