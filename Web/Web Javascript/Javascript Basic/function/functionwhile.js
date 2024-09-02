function cek(kalimat){
    var count = 0;

    while(kalimat != "agung"){
        if(kalimat != "agung"){
            var kalimat = prompt("masih kesempatan 2 kali");
            count += 1;
            if(kalimat != "agung"){
                var kalimat = prompt("masih kesempatan 1 kali");
                count += 1;
            }
            if(kalimat != "agung"){
                alert("silahkan ke point coffe");
                count += 1;
            }
        }
        if (count == 3){
            break;
        }
    }
    if(kalimat == "agung"){
        alert("jawaban benar");
    }
    else{
        alert("silahkan ulangi lagi");
    }
}

function hitung(a,b){
    var hasil = a + b;
    return hasil;
}

function tampil(){
    document.write("<br> hello world");
}

function hitung(nomer1, nomer2){
    var angka1 = parseFloat(nomer1);
    var angka2 = parseFloat(nomer2);
    var jumlah = angka1 + angka2;
    
    alert("jawaban = " + jumlah);
}