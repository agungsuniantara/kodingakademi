import java.util.Scanner;

class Rental {
    String namaPenyewa;
    double durasi;
	double harga = 5000;
	double total;
	double temp;

    Rental(String a, double b) {
        this.namaPenyewa = a;
        this.durasi = b;
    }

    void total() {
		if (this.temp != this.total){
			System.out.println("Total bayar: " + this.temp);
		}
		else{
			this.total = this.harga * this.durasi;
			System.out.println("Total bayar: " + this.total);
		}
    }
	
	void tambah_durasi(double a){
		this.durasi += a;
		System.out.println("total durasi : " + this.durasi);
	}
	
	double pembayaran(double a){
		double harga_awal = this.total;
		this.total -= a;
		this.temp = harga_awal - a;
		if (this.total != 0){
			System.out.println("belum lunas");
			return this.total;
		}
		else{
			System.out.println("sudah lunas");
			return this.total;
		}
	}
}

public class ProgramRentalPS {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Masukkan nama penyewa: ");
        String nama = scanner.nextLine();

        System.out.print("Masukkan durasi sewa: ");
        double durasi = scanner.nextDouble();

        Rental akun = new Rental(nama, durasi);

        int pilihan;
        do {
            System.out.println("\nMenu:");
            System.out.println("1. Total harga");
			System.out.println("2. Data Penyewa");
			System.out.println("3. Tambah durasi");
			System.out.println("4. Pembayaran");
            System.out.println("0. Keluar");
            System.out.print("Pilih menu : ");
            pilihan = scanner.nextInt();

            switch (pilihan) {
                case 1:
                    akun.total();
                    break;
				case 2:
					System.out.println("Nama akun : " + akun.namaPenyewa);
					break;
				case 3:
					System.out.print("Masukkan tambah durasi : ");
					double tambah = scanner.nextDouble();
					akun.tambah_durasi(tambah);
					break;
				case 4:
					System.out.print("Masukkan duit : ");
					double bayar = scanner.nextDouble();
					double simpan = akun.pembayaran(bayar);
					if (simpan != 0){
						break;
					}
                case 0:
                    System.out.println("Terima kasih. Program berakhir.");
                    break;
                default:
                    System.out.println("Pilihan tidak valid. Silakan coba lagi.");
            }

        } while (pilihan != 0);

        scanner.close();
    }
}
