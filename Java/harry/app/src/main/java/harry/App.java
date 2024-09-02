package harry;

import harry.model.Tumbuhan;
import java.util.Scanner;
import harry.model.Zombie;
import harry.model.Inventory;
import harry.model.Deck;
import harry.model.Map;
import harry.model.Sun;
import java.util.List;

public class App {
    static Tumbuhan sunflower = Tumbuhan.createPlant("sunflower");
    static Tumbuhan peashooter = Tumbuhan.createPlant("peashooter");
    static Tumbuhan wallnut = Tumbuhan.createPlant("wallnut");
    static Tumbuhan snowpea = Tumbuhan.createPlant("snowpea");
    static Tumbuhan squash = Tumbuhan.createPlant("squash");
    static Tumbuhan lilypad = Tumbuhan.createPlant("lilypad");

    static Zombie normal = Zombie.createZombie("normal zombie");
    static Zombie conehead = Zombie.createZombie("conehead zombie");
    static Zombie pole = Zombie.createZombie("pole zombie");
    static Zombie buckethead = Zombie.createZombie("buckethead zombie");
    static Zombie ducky = Zombie.createZombie("ducky tube zombie");
    static Zombie dolphin = Zombie.createZombie("rider zombie");

    public static void menu(){
        System.out.println("1. Start");
        System.out.println("2. Help");
        System.out.println("3. Plant list");
        System.out.println("4. Zombies List");
        System.out.println("5. Exit");
    }

    public static void PlantList(){
        sunflower.displayInfo();
        peashooter.displayInfo();
        wallnut.displayInfo();
        snowpea.displayInfo();
        squash.displayInfo();
        lilypad.displayInfo();
    }

    public static void ZombieList(){
        normal.displayInfo();
        conehead.displayInfo();
        pole.displayInfo();
        buckethead.displayInfo();
        ducky.displayInfo();
    }

    public static int halaman_utama(Scanner scan){
        int angka = 0;
        while (true) {
            try {
                System.out.print("Pilih nomer menu : ");
                int nomer = scan.nextInt();
                if (nomer == 3) {
                    PlantList();
                } else if (nomer == 1) {
                    angka = 1;
                    break;
                } else if (nomer == 4) {
                    ZombieList();
                } else if (nomer == 5) {
                    System.out.println("Terima kasih sudah bermain game !!!");
                    break;
                } else {
                    throw new IllegalArgumentException("Menu tidak valid.");
                }
            } catch (Exception e) {
                System.out.println("Error: " + e.getMessage());
                scan.nextLine(); // Clear buffer
            }
        }
        return angka;
    }

    public static void card(Scanner scan, Inventory bag, Deck deck){
        try {
            bag.tambah(sunflower.getName());
            bag.tambah(peashooter.getName());
            bag.tambah(wallnut.getName());
            bag.tambah(snowpea.getName());
            bag.tambah(squash.getName());
            bag.tambah(lilypad.getName());  
        } catch (Exception e) {
            System.out.println("Error saat menambahkan tanaman ke inventory: " + e.getMessage());
        }

        while (true) {
            try {
                System.out.println("Inventory : ");
                bag.tampilkanInventory();
                System.out.print("Inventory action (pilih, hapus, tukar, start) : ");
                String kondisi = scan.next();
                if (kondisi.equalsIgnoreCase("pilih")) {
                    System.out.print("tanaman : ");
                    String tanaman = scan.next();
                    boolean contains = bag.data.contains(tanaman.toLowerCase());
                    String temp = bag.pilihTanaman(tanaman.toLowerCase());
                    if (contains) {
                        switch (tanaman.toLowerCase()) {
                            case "sunflower":
                                deck.addCard(temp);
                                break;
                            case "peashooter":
                                deck.addCard(temp);
                                break;
                            case "wallnut":
                                deck.addCard(temp);
                                break;
                            case "snowpea":
                                deck.addCard(temp);
                                break;
                            case "squash":
                                deck.addCard(temp);
                                break;
                            case "lilypad":
                                deck.addCard(temp);
                                break;
                            default:
                                throw new IllegalArgumentException("Tanaman tidak valid.");
                        }
                    } else {
                        throw new IllegalArgumentException("Tanaman tidak tersedia.");
                    }
                } 
                else if (kondisi.equalsIgnoreCase("hapus")) {
                    System.out.print("tanaman : ");
                    String tanaman = scan.next();
                    if (bag.data.contains(tanaman.toLowerCase())) {
                        bag.hapusTanaman(tanaman.toLowerCase());
                        System.out.println("Tanaman '" + tanaman + "' dihapus dari inventory.");
                    } else {
                        throw new IllegalArgumentException("Tanaman tidak tersedia.");
                    }   
                }
                else if (kondisi.equalsIgnoreCase("tukar")) {
                    System.out.print("tanaman 1 : ");
                    String tanaman1 = scan.next();
                    System.out.print("tanaman 2 : ");
                    String tanaman2 = scan.next();
                    if (bag.data.contains(tanaman1.toLowerCase()) && bag.data.contains(tanaman2.toLowerCase())) {
                        int index_tanaman1 = 0;
                        int index_tanaman2 = 0;
                        for (int i = 0; i < bag.data.size(); i++){
                            String temp = bag.data.get(i);
                            if (temp.equalsIgnoreCase(tanaman1)){
                                index_tanaman1 += i;
                            }
                        }
                        for (int i = 0; i < bag.data.size(); i++){
                            String temp = bag.data.get(i);
                            if (temp.equalsIgnoreCase(tanaman2)){
                                index_tanaman2 += i;
                            }
                        }
                        bag.tukarPosisi(index_tanaman1, index_tanaman2);
                    } else {
                        throw new IllegalArgumentException("Tanaman tidak tersedia.");
                    }   
                }
                else if (kondisi.equalsIgnoreCase("start")) {
                    if (deck.card.size() < 6) {
                        System.out.println("Deck harus memiliki minimal 6 kartu untuk memulai permainan.");
                        continue;
                    }
                    break; // Exit loop and start the game
                } else {
                    throw new IllegalArgumentException("Pilihan tidak valid.");
                }
                
            } catch (Exception e) {
                System.out.println("Error: " + e.getMessage());
                scan.nextLine(); // Clear buffer
            }
        }
    }
    
    public static void game(Scanner scan, Deck deck, Map map, Sun sun){
        try {
            sun.sun_morning(); // Memulai penghasilan Sun di pagi hari
        } catch (Exception e) {
            System.out.println("Error saat memulai penghasilan Sun di pagi hari: " + e.getMessage());
        }

        if (deck.card.size() < 6) {
            System.out.println("Deck tidak memenuhi syarat minimal 6 kartu. Tidak dapat memulai permainan.");
            return;
        }

        while (true) {
            System.out.println("Map : ");
            map.show_map();
            System.out.println("Sun : " + sun.sun_player);
            System.out.println("Deck card : ");
            deck.tampilkanCard();
            map.spawnZombie();
            System.out.print("Deck option (menanam, menggali) : ");
            String action = scan.next();
            if (action.equalsIgnoreCase("menanam")) {
                menanamTanaman(scan, deck, map, sun);
            } 
            else if (action.equalsIgnoreCase("menggali")) {
                menggaliTanaman(scan, map, deck);
            }
            else {
                System.out.println("Aksi tidak valid. Silakan pilih 'menanam', 'menggali'.");
            }
        }
    }

    private static void menanamTanaman(Scanner scan, Deck deck, Map map, Sun sun) {
        try {
            System.out.print("x : ");
            int x = scan.nextInt();
            System.out.print("y : ");
            int y = scan.nextInt();
            System.out.print("tanaman : ");
            String tanaman = scan.next();
            switch (tanaman.toLowerCase()) {
                case "sunflower":
                    deck.menanamTumbuhan(x, y, sunflower, map, sun);
                    sunflower.attack(map, x, y, normal, conehead, pole, buckethead, ducky, dolphin);
                    break;
                case "peashooter":
                    deck.menanamTumbuhan(x, y, peashooter, map, sun);
                    peashooter.attack(map, x, y, normal, conehead, pole, buckethead, ducky, dolphin);
                    break;
                case "wallnut":
                    deck.menanamTumbuhan(x, y, wallnut, map, sun);
                    wallnut.attack(map, x, y, normal, conehead, pole, buckethead, ducky, dolphin);
                    break;
                case "snowpea":
                    deck.menanamTumbuhan(x, y, snowpea, map, sun);
                    snowpea.attack(map, x, y, normal, conehead, pole, buckethead, ducky, dolphin);
                    break;
                case "squash":
                    deck.menanamTumbuhan(x, y, squash, map, sun);
                    squash.attack(map, x, y, normal, conehead, pole, buckethead, ducky, dolphin);
                    break;
                case "lilypad":
                    deck.menanamTumbuhan(x, y, lilypad, map, sun);
                    lilypad.attack(map, x, y, normal, conehead, pole, buckethead, ducky, dolphin);
                    break;
                default:
                    System.out.println("Tanaman tidak dikenal. Coba lagi.");
                    break;
            }
            tampilkanKesehatanKarakter(map);
        } catch (Exception e) {
            System.out.println("Error saat menanam: " + e.getMessage());
        }
    }

    private static void menggaliTanaman(Scanner scan, Map map, Deck deck) {
        System.out.print("x : ");
        int x = scan.nextInt();
        System.out.print("y : ");
        int y = scan.nextInt();
        if (map.grid[x][y] instanceof List) {
            List<String> tanamanDiPosisi = (List<String>) map.grid[x][y];
            for (String tanaman : tanamanDiPosisi) {
                switch (tanaman) {
                    case "U":
                        deck.menggaliTumbuhan(x, y, sunflower, map);
                        break;
                    case "E":
                        deck.menggaliTumbuhan(x, y, peashooter, map);
                        break;
                    case "A":
                        deck.menggaliTumbuhan(x, y, wallnut, map);
                        break;
                    case "N":
                        deck.menggaliTumbuhan(x, y, snowpea, map);
                        break;
                    case "Q":
                        deck.menggaliTumbuhan(x, y, squash, map);
                        break;
                    case "L":
                        deck.menggaliTumbuhan(x, y, lilypad, map);
                        break;
                    default:
                        System.out.println("Tidak ada tanaman yang dapat digali.");
                        break;
                }
            }
        } else {
            System.out.println("Tidak ada tanaman yang dapat digali.");
        }
    }

    private static void tampilkanKesehatanKarakter(Map map) {
        boolean data = false;
        System.out.println("Kesehatan karakter di peta:");
        for (int i = 0; i < map.grid.length; i++) {
            for (int j = 0; j < map.grid[i].length; j++) {
                if (map.grid[i][j] instanceof List) {
                    for (String karakter : (List<String>) map.grid[i][j]) {
                        data = true;
                        switch (karakter) {
                            case "U":
                                System.out.println("Health sunflower : " + sunflower.getHealth());
                                break;
                            case "E":
                                System.out.println("Health peashooter : " + peashooter.getHealth());
                                break;
                            case "A":
                                System.out.println("Health wallnut : " + wallnut.getHealth());
                                break;
                            case "N":
                                System.out.println("Health snowpea : " + snowpea.getHealth());
                                break;
                            case "Q":
                                System.out.println("Health squash : " + squash.getHealth());
                                break;
                            case "ZN":
                                System.out.println("Health normal zombie : " + normal.getHealth());
                                break;
                            case "ZC":
                                System.out.println("Health conehead zombie : " + conehead.getHealth());
                                break;
                            case "ZP":
                                System.out.println("Health pole zombie : " + pole.getHealth());
                                break;
                            case "ZB":
                                System.out.println("Health buckethead zombie : " + buckethead.getHealth());
                                break;
                            case "ZD":
                                System.out.println("Health ducky tube zombie : " + ducky.getHealth());
                                break;
                            case "ZR":
                                System.out.println("Health rider zombie : " + dolphin.getHealth());
                                break;
                            default:
                                break;
                        }
                    }
                }
            }
        }
        if (!data) {
            System.out.println("Tidak ada karakter pada map.");
        }
    }
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Inventory bag = new Inventory();
        Deck deck = new Deck();
        Map map = new Map();
        Sun sun = new Sun();

        menu();
        int start = halaman_utama(scan);
        if(start == 1){
            System.out.println("Start Game !!!");
            card(scan, bag, deck);
            game(scan, deck, map, sun);
        }
        scan.close();
    }
}


