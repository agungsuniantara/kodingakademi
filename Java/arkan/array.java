public class array {
    public static void main(String[] args) {
        int [][] angka = {{1,2,3}, {4,5,6}};
        int [][] genap = new int[angka.length][angka[0].length];
        int jumlah_genap = 0;

        for (int i = 0; i < angka.length; ++i) {
            for (int j = 0; j < angka[i].length; ++j) {
                if (angka[i][j] % 2 == 0){
                    genap[i][j] = angka[i][j];
                }
            }
        }
        for (int i = 0; i < angka.length; ++i) {
            for (int j = 0; j < angka[i].length; ++j) {
                if (genap[i][j] != 0){
                    jumlah_genap += 1;
                }
            }
        }
        System.out.println("Jumlah genap = " + jumlah_genap);

        int [] angka10 = {1,2,3,4};
        int total = 0; 

        for (int i = 3; i < 4; i++){
            if (angka10[i] % 2 == 0){
                total += angka10[i];
            }
        }
        System.out.println("total angka genap = " + total);

    }
}
