class Pasien {
    private String nama;
    private int umur;

    public Pasien(String nama, int umur) {
        this.nama = nama;
        this.umur = umur;
    }

    public String getNama() {
        return nama;
    }

    public int getUmur() {
        return umur;
    }

    @Override
    public String toString() {
        return "Pasien = {nama = " + nama + ", umur = " + umur + "}";
    }
}

class Dokter {
    private String nama;
    private String spesialisasi;

    public Dokter(String nama, String spesialisasi) {
        this.nama = nama;
        this.spesialisasi = spesialisasi;
    }

    public String getNama() {
        return nama;
    }

    public String getSpesialisasi() {
        return spesialisasi;
    }

    @Override
    public String toString() {
        return "Dokter = {nama = " + nama + ", spesialis = " + spesialisasi + "}";
    }
}

class Kunjungan {
    private Pasien pasien;
    private Dokter dokter;
    private String tanggal;
	// private int harga;

    public Kunjungan(Pasien pasien, Dokter dokter, String tanggal) {
        this.pasien = pasien;
        this.dokter = dokter;
        this.tanggal = tanggal;
    }

    public Pasien getPasien() {
        return pasien;
    }

    public Dokter getDokter() {
        return dokter;
    }

    public String getTanggal() {
        return tanggal;
    }
	
	public int harga(){
		int harga = 0;

        if (pasien.getUmur() < 20) {
            harga += 100000;
        } else if (pasien.getUmur() >= 20 && pasien.getUmur() < 30) {
            harga += 200000;
        } else if (pasien.getUmur() >= 30) {
            harga += 300000;
        }

        return harga;
	}

    @Override
    public String toString() {
        return "Kunjungan = { pasien = " + pasien.getNama() + ", dokter = " + dokter.getNama() + ", tanggal = " + tanggal + ", biaya = "+ harga() + "}";
    }
}

public class ProgramKlinik {
    public static void main(String[] args) {
        Pasien pasien1 = new Pasien("John Doe", 30);
        Dokter dokter1 = new Dokter("Dr. Smith", "Dokter Umum");

        Kunjungan kunjungan1 = new Kunjungan(pasien1, dokter1, "2024-01-31");

        System.out.println("Informasi Kunjungan:");
        System.out.println(kunjungan1.toString());
		System.out.println(pasien1.toString());
		System.out.println(dokter1.toString());
    }
}
