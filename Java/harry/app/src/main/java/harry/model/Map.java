package harry.model;

import java.util.Random;
import java.util.Timer;
import java.util.TimerTask;
import java.util.ArrayList;
import java.util.List;

public class Map {
    public Object[][] grid;
    private Random random = new Random();
    private Timer timer = new Timer();
    private int zombieCount = 0; // Menambahkan penghitung zombie

    public Map(){
        try {
            this.grid = new Object[6][20];
        } catch (Exception e) {
            System.out.println("Error saat membuat grid: " + e.getMessage());
        }
    }

    public void show_map(){
        try {
            for (int i = 0; i < grid.length; i++) {
                System.out.print("|");
                for (int j = 0; j < grid[i].length; j++) {
                    if (grid[i][j] == null){
                        System.out.print(" ");
                    }
                    else{
                        System.out.print(grid[i][j]);
                    }
                }
                System.out.println("");
            }
        } catch (Exception e) {
            System.out.println("Error saat menampilkan peta: " + e.getMessage());
        }
    }

    public void spawnZombie(){
        timer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {
                if (zombieCount <= 9) { // Memastikan jumlah zombie tidak lebih dari 10
                    for (int i = 0; i < grid.length; i++) {
                        if (random.nextDouble() < 0.3) { // Probabilitas 0.3 untuk munculnya zombie
                            if (grid[i][grid[i].length - 1] == null) {
                                Zombie zombie = Zombie.createZombie(randomZombie());
                                // Cek apakah koordinat x adalah pool dan zombie bukan aquatic
                                if ((i == 2 || i == 3) && !zombie.getisAquaticn()) {
                                    continue; // Jika iya, skip iterasi ini
                                }
                                // Cek apakah koordinat x bukan pool dan zombie adalah aquatic
                                if ((i != 2 && i != 3) && zombie.getisAquaticn()) {
                                    continue; // Jika iya, skip iterasi ini
                                }
                                grid[i][grid[i].length - 1] = new ArrayList<>();
                                ((List)grid[i][grid[i].length - 1]).add("Z" + zombie.getName().substring(0, 1).toUpperCase()); // Menempatkan zombie di akhir kolom
                                moveZombie(i, grid[i].length - 1, "Z" + zombie.getName().substring(0, 1).toUpperCase());
                                zombieCount++; // Menambahkan penghitung zombie
                            }
                        }
                    }
                }
            }
        }, 0, 20000 + random.nextInt(140001)); // Timer berjalan antara 20 detik sampai 160 detik
    }

    private void moveZombie(int x, int y, String zombie) {
        timer.schedule(new TimerTask() {
            @Override
            public void run() {
                if (y > 0 && grid[x][y - 1] == null) {
                    grid[x][y - 1] = new ArrayList<>();
                    ((List)grid[x][y - 1]).add(zombie);
                    grid[x][y] = null;
                    moveZombie(x, y - 1, zombie); // Memindahkan zombie ke petak selanjutnya
                }
                else if (y > 0 && grid[x][y - 1] instanceof List) {
                    grid[x][y - 1] = new ArrayList<>();
                    ((List)grid[x][y - 1]).add(zombie); 
                    grid[x][y] = null;
                    moveZombie(x, y - 1, zombie); // Memindahkan zombie ke petak selanjutnya
                }
                else if (y == 0) {
                    System.out.println("");
                    System.out.println("");
                    System.out.println("Zombie telah mencapai ujung peta. Game berakhir.");
                    System.exit(0); // Menghentikan program jika zombie mencapai y = 0
                }
            }
        }, 5000); // Zombie bergerak setiap 5 detik per petak
    }

    private String randomZombie(){
        String[] data = {"normal zombie", "conehead Zombie", "pole zombie", "buckethead zombie", "ducky tube zombie", "rider zombie"};
        return data[random.nextInt(data.length)];
    }
}
