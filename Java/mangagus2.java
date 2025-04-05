class orgil{
    String nama = "wahasta";
    int umur = 20;
    String alamat = "denpasar";
    String tingkat;

    public orgil(String a){
        this.tingkat = a;
    }

    public void tampil_nama(){
        System.out.println("Nama = " + nama);
        System.out.println("Alamat = " + alamat);
        System.out.println("umur = " + umur);
        System.out.println("tingkat = " + tingkat);
    }
}

public class mangagus2 {
    public static void main(String[] args) {
        orgil data = new orgil("sudah gila");
        System.out.println(data.nama);
        data.tampil_nama();
    }
}
