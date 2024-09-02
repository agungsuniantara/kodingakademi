package plant_vs_zombie.model;

import java.util.Random;
import java.util.Timer;
import java.util.TimerTask;

public class Sun {
    private int sunCount; // Jumlah Sun yang dimiliki pemain
    private static final int INITIAL_SUN = 25; // Jumlah Sun awal

    public Sun() {
        this.sunCount = INITIAL_SUN; // Set jumlah Sun awal
    }

    // Getter untuk mendapatkan jumlah Sun yang dimiliki pemain
    public int getSunCount() {
        return sunCount;
    }

    // Method untuk menambah jumlah Sun
    public void addSun(int amount) {
        sunCount += amount;
    }

    // Method untuk mengurangi jumlah Sun
    public void spendSun(int amount) {
        if (sunCount >= amount) {
            sunCount -= amount;
        } else {
            System.out.println("Not enough Sun!");
        }
    }

    // Method untuk mendapatkan Sun dari tanaman Sunflower
    public void obtainSunFromSunflower() {
        // Misalnya, setiap kali mendapatkan Sun dari Sunflower, tambahkan 25 ke jumlah Sun
        addSun(25);
    }

    // Method untuk mendapatkan Sun pada pagi hari
    public void obtainSunAtMorning() {
        Timer timer = new Timer();
        timer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {
                // Mendapatkan jumlah Sun antara 5 - 10 setiap interval waktu
                int randomSun = new Random().nextInt(6) + 5;
                addSun(randomSun);
                System.out.println("Mendapatkan " + randomSun + " Sun!");
            }
        }, 0, getRandomInterval()); // Waktu interval antara 5 - 10 detik
    }

    // Method untuk mendapatkan interval waktu antara 5 - 10 detik
    private int getRandomInterval() {
        return (new Random().nextInt(6) + 5) * 1000; // Konversi ke milidetik
    }
}
