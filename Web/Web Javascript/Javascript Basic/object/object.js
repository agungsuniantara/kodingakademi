function hitung(angka1,angka2){
    var bangundatar = {
        nama : "persegi panjang",
        panjang : angka1,
        lebar : angka2,

        panggilnama: function(){
            var panggil = this.nama;
            return panggil;
        },
        luas: function(){
            var hasil = this.panjang * this.lebar;
            return hasil;
        },
        keliling: function(){
            var hasil = 2 * (this.panjang * this.lebar);
            return hasil;
        }
    };
    alert("Nama : " + bangundatar.panggilnama() + "\nPanjang : " + bangundatar.panjang + "\nLebar : " + bangundatar.lebar + "\nLuas : " + bangundatar.luas() + "\nKeliling : " + bangundatar.keliling());
}
