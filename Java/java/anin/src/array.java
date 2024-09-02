public class array {
    public static void main(String[] args) {
        // cara 1
        int[] angka = new int[3];
        angka[0] = 1;
        angka[1] = 2;
        angka[2] = 3;

        for (int i = 0; i < angka.length; i++){
            System.out.println("Data : " + angka[i]);
        }

        String[] data = new String[3];
        data[0] = "a";
        data[1] = "b";
        data[2] = "c";

        // cara 2
        int [] angka2 = {10, 20, 30};
        String[] data2 = {"anin", "burung", "cicak"};
    }
}
