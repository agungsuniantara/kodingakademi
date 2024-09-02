package harry.model;

import java.util.TimerTask;
import java.util.Timer;
import java.util.Random;

public class Sun {
    public int sun_player = 25; // Pemain mulai dengan 25 Sun
    final int MORNING_DURATION = 100; // Durasi pagi hari dalam detik
    final int NIGHT_DURATION = 100; // Durasi malam hari dalam detik
    Timer dayTimer = new Timer();
    Random random = new Random();

    public void sun_sunflower(){
        try {
            Timer sunflowerSunTimer = new Timer();
            sunflowerSunTimer.scheduleAtFixedRate(new TimerTask() {
                @Override
                public void run() {
                    sun_player += 25;
                }
            }, 0, 3000); // menjalankan task setiap 3 detik
        } catch (Exception e) {
            System.out.println("Error saat menjalankan sun_sunflower: " + e.getMessage());
        }
    }

    public void sun_random(){
        try {
            dayTimer.scheduleAtFixedRate(new TimerTask() {
                @Override
                public void run() {
                    sun_player += 25;
                }
            }, 0, 5000 + random.nextInt(5000)); // Menjalankan task ini antara 5 sampai 10 detik
        } catch (Exception e) {
            System.out.println("Error saat menjalankan sun_random: " + e.getMessage());
        }
    }

    public void sun_morning(){
        try {
            dayTimer.scheduleAtFixedRate(new TimerTask() {
                @Override
                public void run() {
                    sun_random();
                }
            }, 0, MORNING_DURATION * 1000); // Menjalankan task ini setiap 100 detik

            dayTimer.schedule(new TimerTask() {
                @Override
                public void run() {
                    sun_night();
                }
            }, MORNING_DURATION * 1000); // Memulai malam setelah 100 detik
        } catch (Exception e) {
            System.out.println("Error saat menjalankan sun_morning: " + e.getMessage());
        }
    }

    public void sun_night(){
        try {
            dayTimer.schedule(new TimerTask() {
                @Override
                public void run() {
                    sun_morning();
                }
            }, NIGHT_DURATION * 1000); // Memulai pagi setelah 100 detik malam
        } catch (Exception e) {
            System.out.println("Error saat menjalankan sun_night: " + e.getMessage());
        }
    }
}



