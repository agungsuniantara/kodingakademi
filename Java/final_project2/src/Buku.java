// Buku.java
public class Buku {
    private int id;
    private String judul;
    private String pengarang;
    private int tahunTerbit;
    private String genre;
    private int stok;

    public Buku(int id, String judul, String pengarang, int tahunTerbit, String genre, int stok) {
        this.id = id;
        this.judul = judul;
        this.pengarang = pengarang;
        this.tahunTerbit = tahunTerbit;
        this.genre = genre;
        this.stok = stok;
    }

    // Getter dan Setter
    public int getId() { return id; }
    public String getJudul() { return judul; }
    public String getPengarang() { return pengarang; }
    public int getTahunTerbit() { return tahunTerbit; }
    public String getGenre() { return genre; }
    public int getStok() { return stok; }
    public void setStok(int stok) { this.stok = stok; }
}
