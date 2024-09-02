package plant_vs_zombie.model;

import java.util.ArrayList;
import java.util.List;

public class Deck {
    private List<Tumbuhan> plantCards;

    public Deck() {
        plantCards = new ArrayList<>();
    }

    // Method untuk menambahkan kartu tanaman ke dalam deck
    public void addPlantCard(Tumbuhan plant) {
        plantCards.add(plant);
    }

    // Method untuk menghapus kartu tanaman dari deck
    public void removePlantCard(Tumbuhan plant) {
        plantCards.remove(plant);
    }

    // Method untuk mendapatkan semua kartu tanaman dalam deck
    public List<Tumbuhan> getAllPlantCards() {
        return plantCards;
    }

    // Method untuk mendapatkan jumlah kartu tanaman dalam deck
    public int getPlantCardCount() {
        return plantCards.size();
    }

    // Method untuk mendapatkan kartu tanaman berdasarkan indeks
    public Tumbuhan getPlantCard(int index) {
        if (index >= 0 && index < plantCards.size()) {
            return plantCards.get(index);
        }
        return null;
    }

    // Method untuk mengecek apakah deck kosong
    public boolean isEmpty() {
        return plantCards.isEmpty();
    }
}
