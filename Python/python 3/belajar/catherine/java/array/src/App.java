public class App {
    public static void main(String[] args) throws Exception {
        // array
        int [] angka = new int[2];
        angka[0] = 1;
        angka[1] = 2;

        System.out.println("Array : ");
        System.out.println("angka index 0 : " + angka[0]);

        // for array
        System.out.println("Perulangan for array : ");

        for (int i = 0; i < angka.length; i++){
            System.out.println("angka : " + angka[i]);
        }

        // foreach
        System.out.println("Perulangan foreach array : ");

        for (int data : angka){
            System.out.println("foreach angka : " + data);
        }

        // array 2d
        System.out.println("array 2D : ");

        int [][] angka3 = {
            {1, 2, 3}, // 0
            {4, 5, 6}  // 1
        };

        System.out.println("angka : " + angka3[1][2]);

        for (int i = 0; i < angka3.length; i++){
            for (int z = 0; z < angka3[i].length; z++){
                System.out.print(angka3[i][z] + " ");
            }
            System.out.println("");
        }

        // array 3d
        System.out.println("array 3D : ");

        int [][][] angka4 = {
            { // 0
                {1, 2, 3}, // 0
                {4, 5, 6} // 1
            },
            { // 1
                {7, 8, 9}, // 0
                {10, 11, 12} // 1
            }
        };

        System.out.println("angka : " + angka4[1][0][1]);

        for (int i = 0; i < angka4.length; i++){
            for (int z = 0; z < angka4[i].length; z++){
                for (int a = 0; a < angka4[i][z].length; a++){
                    System.out.print(angka4[i][z][a] + " ");
                }
                System.out.println("");
            }
        }
    }
}
