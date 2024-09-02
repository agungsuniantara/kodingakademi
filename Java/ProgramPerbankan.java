import java.util.Scanner;

class AkunBank {
    String namaPemilik;
    double saldo;

    AkunBank(String namaPemilik, double saldoAwal) {
        this.namaPemilik = namaPemilik;
        this.saldo = saldoAwal;
    }

    void setor(double jumlah) {
        saldo += jumlah;
        System.out.println("Setoran berhasil. Saldo sekarang: " + saldo);
    }

    void tarik(double jumlah) {
        if (jumlah <= saldo) {
            saldo -= jumlah;
            System.out.println("Penarikan berhasil. Saldo sekarang: " + saldo);
        } else {
            System.out.println("Saldo tidak mencukupi.");
        }
    }

    void cekSaldo() {
        System.out.println("Saldo saat ini: " + saldo);
    }
}

public class ProgramPerbankan {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Masukkan nama pemilik akun: ");
        String namaPemilik = scanner.nextLine();

        System.out.print("Masukkan saldo awal: ");
        double saldoAwal = scanner.nextDouble();

        AkunBank akun = new AkunBank(namaPemilik, saldoAwal);

        int pilihan;
        do {
            System.out.println("\nMenu:");
            System.out.println("1. Setor");
            System.out.println("2. Tarik");
            System.out.println("3. Cek Saldo");
			System.out.println("4. Tampil akun");
            System.out.println("0. Keluar");
            System.out.print("Pilih menu (0-4): ");
            pilihan = scanner.nextInt();

            switch (pilihan) {
                case 1:
                    System.out.print("Masukkan jumlah setoran: ");
                    double jumlahSetoran = scanner.nextDouble();
                    akun.setor(jumlahSetoran);
                    break;
                case 2:
                    System.out.print("Masukkan jumlah penarikan: ");
                    double jumlahPenarikan = scanner.nextDouble();
                    akun.tarik(jumlahPenarikan);
                    break;
                case 3:
                    akun.cekSaldo();
                    break;
				case 4:
					System.out.println("Nama akun : " + akun.namaPemilik);
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
