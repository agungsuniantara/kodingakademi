// Peminjaman.java
import java.util.Date;
public class Peminjaman {
    private int id;
    private int idBuku;
    private int idAnggota;
    private Date tanggalPinjam;
    private Date tanggalKembali;
    private String status;

    public Peminjaman(int id, int idBuku, int idAnggota, Date tanggalPinjam, Date tanggalKembali, String status) {
        this.id = id;
        this.idBuku = idBuku;
        this.idAnggota = idAnggota;
        this.tanggalPinjam = tanggalPinjam;
        this.tanggalKembali = tanggalKembali;
        this.status = status;
    }

    // Getter dan Setter
    public int getId() { return id; }
    public int getIdBuku() { return idBuku; }
    public int getIdAnggota() { return idAnggota; }
    public Date getTanggalPinjam() { return tanggalPinjam; }
    public Date getTanggalKembali() { return tanggalKembali; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
}
