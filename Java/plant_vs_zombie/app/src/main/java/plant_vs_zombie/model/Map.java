package plant_vs_zombie.model;

public class Map {
    private static final int ROWS = 9;
    private static final int COLS = 6;
    private static final int POOL_ROWS = 18;

    private Area[][] grid; // Grid untuk menyimpan petak-petak pada peta

    public Map() {
        this.grid = new Area[ROWS][COLS];
        initializeMap();
    }

    // Inisialisasi peta
    private void initializeMap() {
        // Setiap petak pada peta diinisialisasi sebagai area umum
        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                grid[i][j] = Area.COMMON_AREA;
            }
        }
        // Area pool ditandai sebagai area pool
        for (int i = 0; i < POOL_ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                grid[i][j] = Area.POOL_AREA;
            }
        }
        // Area muncul zombie ditandai sebagai area muncul zombie
        for (int i = 0; i < ROWS; i++) {
            for (int j = COLS - 1; j < COLS; j++) {
                grid[i][j] = Area.ZOMBIE_SPAWN_AREA;
            }
        }
        // Area yang harus dilindungi oleh pemain ditandai sebagai area yang harus dilindungi
        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < 1; j++) {
                grid[i][j] = Area.PROTECTED_AREA;
            }
        }
    }

    // Getter untuk mendapatkan petak pada koordinat tertentu pada peta
    public Area getArea(int row, int col) {
        return grid[row][col];
    }
}

    // Enum untuk merepresentasikan jenis area pada peta
enum Area {
    COMMON_AREA, // Area umum
    POOL_AREA, // Area pool
    ZOMBIE_SPAWN_AREA, // Area muncul zombie
    PROTECTED_AREA // Area yang harus dilindungi oleh pemain
}
