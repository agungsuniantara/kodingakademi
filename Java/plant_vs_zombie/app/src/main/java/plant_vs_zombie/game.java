package plant_vs_zombie;

import plant_vs_zombie.model.Tumbuhan;
import plant_vs_zombie.model.Zombie;
import plant_vs_zombie.model.Inventory;
import java.util.Timer;
import java.util.TimerTask;

public class game {
   static int sun_player = 0;

    public static void main(String[] args) {
        // Membuat objek tanaman
        Tumbuhan sunflower = Tumbuhan.createPlant("sunflower");
        Tumbuhan peashooter = Tumbuhan.createPlant("peashooter");
        
        // Membuat objek zombie
        Zombie normal_zombie = Zombie.createZombie("normal zombie");
        
        // Membuat objek inventory
        Inventory inventory = new Inventory();
        
        // Menambahkan tanaman dan zombie ke inventory
        inventory.tambah(sunflower.getName());
        inventory.tambah(peashooter.getName());
        inventory.tambah(normal_zombie.getName());
        
        // Menampilkan isi inventory
        inventory.tampilkanInventory();

        // Timer untuk menjalankan ProduceSun setiap 10 detik
        Timer timer = new Timer();
        timer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {
                sun_player += sunflower.produceSun();
                System.out.println("Sun player: " + sun_player);
            }
        }, 0, 10000); // Menjalankan task setiap 10 detik (dalam milidetik)

    }
}
