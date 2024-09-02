public class App {
    public static void main(String[] args) throws Exception {
        int pilihan = 1;
        int angka1 = 10;
        int angka2 = 20;
        int angka3 = 50;

        // statement conditional

        if (pilihan > 2){ // false
            System.out.println("lebih besar dari 2");
        }
        else if (pilihan == 2){ // false
            System.out.println("sama dengan 2");
        }
        else if (pilihan < 2){ // true
            System.out.println("lebih kecil dari 2");
        }
        else{
            System.out.println("nilai tidak dikenal");
        }

        // statement conditional with logic operation

        if (angka1 > 15 && angka2 < 30){ 
            System.out.println("kondisi if");
        }
        else if(angka1 > 5 && angka2 < 30){  // true & true = true
            System.out.println("kondisi else if");
        }

        if (angka1 > 5 && angka2 < 30 && angka3 > 40){  // true & true & true = false
            System.out.println("kondisi and lebih dari 1 benar");
        }

        // statement switch

        int pilih = 2;

        switch(pilih){
            case 1:
                System.out.println("ini case 1");
                break;
            case 2:
                System.out.println("ini case 2");
                break;
            default:
                System.out.println("case tidak tersedia");
        }

        String kondisi = "satu";

        switch(kondisi){
            case "satu":
                System.out.println("ini case 1");
                break;
            case "dua":
                System.out.println("ini case 2");
                break;
            default:
                System.out.println("case tidak tersedia");
        }

        // challange

        // buat variabel nilai
        // nilai >= 0 & nilai <= 50, tampil nilai D
        // nilai > 50 & nilai <= 70, tampil nilai C
        // nilai > 70 & nilai <= 90, tampil nilai B
        // nilai > 90 & nilai <= 100, tampil nilai A
        // else, tampil nilai tidak diketahui

        int nilai = 20;

        if (nilai >= 0 && nilai <= 50){
            System.out.println("nilai D");
        }
        else if(nilai > 50 && nilai <= 70){
            System.out.println("nilai C");
        }
        else if(nilai > 70 && nilai <= 90){
            System.out.println("nilai B");
        }
        else if(nilai > 90 && nilai <= 100){
            System.out.println("nilai A");
        }
        else{
            System.out.println("nilai tidak diketahui");
        }
    }
}
