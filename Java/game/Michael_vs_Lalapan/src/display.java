public class display {
    public static void main(String[] args) {
        character.main(args);
        Inventory inventory = new Inventory();

        // Membuat objek sunflower dan normal_zombie
        Tumbuhan sunflower = PlantFactory.createPlant("sunflower");
        Tumbuhan peashooter = PlantFactory.createPlant("peashooter");
        Zombie normal_zombie = ZombieFactory.createZombie("normal zombie");

        // System.out.println(sunflower.getName());
        // System.out.println(peashooter.getName());
        // System.out.println(normal_zombie.getName());
        
        sunflower.displayInfo();
        peashooter.displayInfo();
        normal_zombie.displayInfo();

        inventory.tambah(sunflower.getName());
        inventory.tambah(normal_zombie.getName());
        inventory.tampilkanInventory();
    }
}
