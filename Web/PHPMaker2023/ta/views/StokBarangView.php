<?php

namespace PHPMaker2023\ta;

// Page object
$StokBarangView = &$Page;
?>
<?php if (!$Page->isExport()) { ?>
<div class="btn-toolbar ew-toolbar">
<?php $Page->ExportOptions->render("body") ?>
<?php $Page->OtherOptions->render("body") ?>
</div>
<?php } ?>
<?php $Page->showPageHeader(); ?>
<?php
$Page->showMessage();
?>
<main class="view">
<form name="fstok_barangview" id="fstok_barangview" class="ew-form ew-view-form overlay-wrapper" action="<?= CurrentPageUrl(false) ?>" method="post" novalidate autocomplete="off">
<?php if (!$Page->isExport()) { ?>
<script>
var currentTable = <?= JsonEncode($Page->toClientVar()) ?>;
ew.deepAssign(ew.vars, { tables: { stok_barang: currentTable } });
var currentPageID = ew.PAGE_ID = "view";
var currentForm;
var fstok_barangview;
loadjs.ready(["wrapper", "head"], function () {
    let $ = jQuery;
    let fields = currentTable.fields;

    // Form object
    let form = new ew.FormBuilder()
        .setId("fstok_barangview")
        .setPageId("view")
        .build();
    window[form.id] = form;
    currentForm = form;
    loadjs.done(form.id);
});
</script>
<script>
loadjs.ready("head", function () {
    // Write your table-specific client script here, no need to add script tags.
});
</script>
<?php } ?>
<?php if (Config("CHECK_TOKEN")) { ?>
<input type="hidden" name="<?= $TokenNameKey ?>" value="<?= $TokenName ?>"><!-- CSRF token name -->
<input type="hidden" name="<?= $TokenValueKey ?>" value="<?= $TokenValue ?>"><!-- CSRF token value -->
<?php } ?>
<input type="hidden" name="t" value="stok_barang">
<input type="hidden" name="modal" value="<?= (int)$Page->IsModal ?>">
<table class="<?= $Page->TableClass ?>">
<?php if ($Page->id_barang->Visible) { // id_barang ?>
    <tr id="r_id_barang"<?= $Page->id_barang->rowAttributes() ?>>
        <td class="<?= $Page->TableLeftColumnClass ?>"><span id="elh_stok_barang_id_barang"><?= $Page->id_barang->caption() ?></span></td>
        <td data-name="id_barang"<?= $Page->id_barang->cellAttributes() ?>>
<span id="el_stok_barang_id_barang">
<span<?= $Page->id_barang->viewAttributes() ?>>
<?= $Page->id_barang->getViewValue() ?></span>
</span>
</td>
    </tr>
<?php } ?>
<?php if ($Page->kode_barang->Visible) { // kode_barang ?>
    <tr id="r_kode_barang"<?= $Page->kode_barang->rowAttributes() ?>>
        <td class="<?= $Page->TableLeftColumnClass ?>"><span id="elh_stok_barang_kode_barang"><?= $Page->kode_barang->caption() ?></span></td>
        <td data-name="kode_barang"<?= $Page->kode_barang->cellAttributes() ?>>
<span id="el_stok_barang_kode_barang">
<span<?= $Page->kode_barang->viewAttributes() ?>>
<?= $Page->kode_barang->getViewValue() ?></span>
</span>
</td>
    </tr>
<?php } ?>
<?php if ($Page->nama_barang->Visible) { // nama_barang ?>
    <tr id="r_nama_barang"<?= $Page->nama_barang->rowAttributes() ?>>
        <td class="<?= $Page->TableLeftColumnClass ?>"><span id="elh_stok_barang_nama_barang"><?= $Page->nama_barang->caption() ?></span></td>
        <td data-name="nama_barang"<?= $Page->nama_barang->cellAttributes() ?>>
<span id="el_stok_barang_nama_barang">
<span<?= $Page->nama_barang->viewAttributes() ?>>
<?= $Page->nama_barang->getViewValue() ?></span>
</span>
</td>
    </tr>
<?php } ?>
<?php if ($Page->jumlah_stok->Visible) { // jumlah_stok ?>
    <tr id="r_jumlah_stok"<?= $Page->jumlah_stok->rowAttributes() ?>>
        <td class="<?= $Page->TableLeftColumnClass ?>"><span id="elh_stok_barang_jumlah_stok"><?= $Page->jumlah_stok->caption() ?></span></td>
        <td data-name="jumlah_stok"<?= $Page->jumlah_stok->cellAttributes() ?>>
<span id="el_stok_barang_jumlah_stok">
<span<?= $Page->jumlah_stok->viewAttributes() ?>>
<?= $Page->jumlah_stok->getViewValue() ?></span>
</span>
</td>
    </tr>
<?php } ?>
</table>
</form>
</main>
<?php
$Page->showPageFooter();
echo GetDebugMessage();
?>
<?php if (!$Page->isExport()) { ?>
<script>
loadjs.ready("load", function () {
    // Write your table-specific startup script here, no need to add script tags.
});
</script>
<?php } ?>
