package harry.model;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Timer;
import java.util.TimerTask;

public class Deck {
    public List<String> card = new ArrayList<>();
    private HashMap<String, Boolean> isPlantOnCooldown = new HashMap<>();

    // Method untuk menambahkan kartu tanaman ke dalam deck
    public void addCard(String plant) {
        try {
            card.add(plant);
            isPlantOnCooldown.put(plant, false); // Awalnya, tanaman tidak dalam cooldown
        } catch (Exception e) {
            System.out.println("Gagal menambahkan kartu: " + e.getMessage());
        }
    }

    // Menampilkan semua tanaman dalam card
    public void tampilkanCard() {
        try {
            for (int i = 0; i < card.size(); i++) {
                System.out.println((i + 1) + ". " + card.get(i));
            }
        } catch (Exception e) {
            System.out.println("Gagal menampilkan kartu: " + e.getMessage());
        }
    }

    public boolean menanamTumbuhan(int x, int y, Tumbuhan tumbuhan, Map map, Sun sun){
        try {
            if (!card.contains(tumbuhan.getName())) {
                System.out.println("Tanaman " + tumbuhan.getName() + " tidak ada dalam deck.");
                return false;
            }

            if (isPlantOnCooldown.getOrDefault(tumbuhan.getName(), true)) {
                System.out.println("Tanaman " + tumbuhan.getName() + " masih dalam cooldown dan tidak dapat ditanam.");
                return false;
            }

            if (map.grid[x][y] instanceof List && !((List)map.grid[x][y]).contains("L")) {
                System.out.println("Tidak dapat menanam tanaman di tempat ini.");
                return false;
            }

            if (sun.sun_player < tumbuhan.getCost()) {
                System.out.println("Sun tidak cukup untuk menanam " + tumbuhan.getName());
                return false;
            }
            else{
                sun.sun_player -= tumbuhan.getCost();
            }

            switch (tumbuhan.getName()) {
                case "sunflower":
                case "peashooter":
                case "wallnut":
                case "snowpea":
                case "squash":
                    if((x == 0 || x == 1 || x == 4 || x == 5) && (y >= 1 && y <= 9)){ // area umum
                        map.grid[x][y] = new ArrayList<>(List.of(tumbuhan.getName().substring(1, 2).toUpperCase()));
                    }
                    else if (map.grid[x][y] instanceof List && ((List)map.grid[x][y]).contains("L")) { // jika ada lilypad, tanaman dapat ditanam di atasnya
                        Tumbuhan lilypad = Tumbuhan.createPlant("lilypad");
                        int totalHealth = lilypad.getHealth() + tumbuhan.getHealth();
                        tumbuhan.setHealth(totalHealth);
                        ((List)map.grid[x][y]).add(tumbuhan.getName().substring(1, 2).toUpperCase());
                    }
                    else{
                        System.out.println(tumbuhan.getName() + " hanya dapat ditanam di area umum atau di atas lilypad.");
                        return false;
                    }
                    break;
                case "lilypad":
                    if((x == 2 || x == 3) && (y >= 1 && y <= 9)){ // area pool
                        map.grid[x][y] = new ArrayList<>(List.of("L"));
                    }
                    else{
                        System.out.println("Lilypad hanya dapat ditanam di area pool.");
                        return false;
                    }
                    break;
                default:
                    System.out.println("Tanaman tidak dikenal.");
                    return false;
            }
            startCooldownTimer(tumbuhan); // Memulai timer cooldown setelah tanaman berhasil ditanam

            if (map.grid[x][y] instanceof List && ((List)map.grid[x][y]).contains("U")) {
                sun.sun_sunflower(); // Memulai penghasilan Sun dari Sunflower
                System.out.println("sun di dapat dari sunflower");
            }
            return true;
        } catch (Exception e) {
            System.out.println("Terjadi kesalahan saat menanam tanaman: " + e.getMessage());
            return false;
        }
    }

    public void menggaliTumbuhan(int x, int y,Tumbuhan tumbuhan, Map map){
        try {
            if (map.grid[x][y] instanceof List) {
                List<String> plants = (List<String>) map.grid[x][y];
                for (String plantName : plants) {
                    switch (plantName) { // mengembalikan health tumbuhan
                            case "U":
                                tumbuhan.setHealth(100);
                                break;
                            case "E":
                                tumbuhan.setHealth(100);
                                break;
                            case "A":
                                tumbuhan.setHealth(1000);
                                break;
                            case "N":
                                tumbuhan.setHealth(100);
                                break;
                            case "Q":
                                tumbuhan.setHealth(100);
                                break;
                            default:
                                break;
                        }
                }
                map.grid[x][y] = null; // Menghapus list tanaman di koordinat tersebut
                System.out.println("Tanaman di koordinat " + x + ", " + y + " telah digali dan dihapus.");
            } else {
                System.out.println("Tidak ada tanaman di koordinat " + x + ", " + y + " untuk digali.");
            }
        } catch (Exception e) {
            System.out.println("Gagal menggali tanaman: " + e.getMessage());
        }
    }

    private void startCooldownTimer(Tumbuhan tumbuhan) {
        try {
            isPlantOnCooldown.put(tumbuhan.getName(), true); // Set tanaman ke status cooldown
            Timer timer = new Timer();
            timer.schedule(new TimerTask() {
                @Override
                public void run() {
                    isPlantOnCooldown.put(tumbuhan.getName(), false); // Setelah timer selesai, tanaman tidak lagi dalam cooldown
                }
            }, tumbuhan.getCooldown() * 1000);
        } catch (Exception e) {
            System.out.println("Gagal memulai timer cooldown: " + e.getMessage());
        }
    }
}
