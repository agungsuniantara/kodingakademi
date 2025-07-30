<?php
    $value = "jaguar";

    switch ($value) {
        case "jaguar":
            echo "jaguar";
            break;
        case "bmw":
            echo "bmw";
            break;
        case "mercedes":
            echo "mercedes";
            break;
        default:
            echo "unknown";
            break;
    }

    $hari_kerja = "senin";

    switch ($hari_kerja) {
        case "senin":
        case "selasa":
        case "rabu":
        case "kamis":
        case "jumat":
            echo "Hari kerja";
            break;
        case "sabtu":
        case "minggu":
            echo "Hari libur";
            break;
        default:
            echo "Hari tidak dikenal";
            break;
    }
?>