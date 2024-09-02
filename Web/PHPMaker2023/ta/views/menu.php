<?php

namespace PHPMaker2023\ta;

// Menu Language
if ($Language && function_exists(PROJECT_NAMESPACE . "Config") && $Language->LanguageFolder == Config("LANGUAGE_FOLDER")) {
    $MenuRelativePath = "";
    $MenuLanguage = &$Language;
} else { // Compat reports
    $LANGUAGE_FOLDER = "../lang/";
    $MenuRelativePath = "../";
    $MenuLanguage = Container("language");
}

// Navbar menu
$topMenu = new Menu("navbar", true, true);
echo $topMenu->toScript();

// Sidebar menu
$sideMenu = new Menu("menu", true, false);
$sideMenu->addMenuItem(4, "mi_staf_gudang", $MenuLanguage->MenuPhrase("4", "MenuText"), $MenuRelativePath . "StafGudangList", -1, "", IsLoggedIn() || AllowListMenu('{43BEB47F-FF54-4D63-A551-FAF44CEB7970}staf gudang'), false, false, "", "", false, true);
$sideMenu->addMenuItem(5, "mi_stok_barang", $MenuLanguage->MenuPhrase("5", "MenuText"), $MenuRelativePath . "StokBarangList", -1, "", IsLoggedIn() || AllowListMenu('{43BEB47F-FF54-4D63-A551-FAF44CEB7970}stok barang'), false, false, "", "", false, true);
$sideMenu->addMenuItem(3, "mi_barang_masuk", $MenuLanguage->MenuPhrase("3", "MenuText"), $MenuRelativePath . "BarangMasukList", -1, "", IsLoggedIn() || AllowListMenu('{43BEB47F-FF54-4D63-A551-FAF44CEB7970}barang masuk'), false, false, "", "", false, true);
$sideMenu->addMenuItem(2, "mi_barang_keluar", $MenuLanguage->MenuPhrase("2", "MenuText"), $MenuRelativePath . "BarangKeluarList", -1, "", IsLoggedIn() || AllowListMenu('{43BEB47F-FF54-4D63-A551-FAF44CEB7970}barang keluar'), false, false, "", "", false, true);
$sideMenu->addMenuItem(6, "mi_order_barang", $MenuLanguage->MenuPhrase("6", "MenuText"), $MenuRelativePath . "OrderBarangList", -1, "", IsLoggedIn() || AllowListMenu('{43BEB47F-FF54-4D63-A551-FAF44CEB7970}order barang'), false, false, "", "", false, true);
$sideMenu->addMenuItem(11, "mci_Laporan_Stok_Gudang", $MenuLanguage->MenuPhrase("11", "MenuText"), $MenuRelativePath . "loncat_01.php", -1, "", IsLoggedIn(), false, true, "", "", false, true);
echo $sideMenu->toScript();
