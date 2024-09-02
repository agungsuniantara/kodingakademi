<?php

namespace PHPMaker2023\ta;

// Page object
$BarangMasukView = &$Page;
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
<form name="fbarang_masukview" id="fbarang_masukview" class="ew-form ew-view-form overlay-wrapper" action="<?= CurrentPageUrl(false) ?>" method="post" novalidate autocomplete="off">
<?php if (!$Page->isExport()) { ?>
<script>
var currentTable = <?= JsonEncode($Page->toClientVar()) ?>;
ew.deepAssign(ew.vars, { tables: { barang_masuk: currentTable } });
var currentPageID = ew.PAGE_ID = "view";
var currentForm;
var fbarang_masukview;
loadjs.ready(["wrapper", "head"], function () {
    let $ = jQuery;
    let fields = currentTable.fields;

    // Form object
    let form = new ew.FormBuilder()
        .setId("fbarang_masukview")
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
<input type="hidden" name="t" value="barang_masuk">
<input type="hidden" name="modal" value="<?= (int)$Page->IsModal ?>">
<table class="<?= $Page->TableClass ?>">
<?php if ($Page->id_brgmsk->Visible) { // id_brgmsk ?>
    <tr id="r_id_brgmsk"<?= $Page->id_brgmsk->rowAttributes() ?>>
        <td class="<?= $Page->TableLeftColumnClass ?>"><span id="elh_barang_masuk_id_brgmsk"><?= $Page->id_brgmsk->caption() ?></span></td>
        <td data-name="id_brgmsk"<?= $Page->id_brgmsk->cellAttributes() ?>>
<span id="el_barang_masuk_id_brgmsk">
<span<?= $Page->id_brgmsk->viewAttributes() ?>>
<?= $Page->id_brgmsk->getViewValue() ?></span>
</span>
</td>
    </tr>
<?php } ?>
<?php if ($Page->no_order->Visible) { // no_order ?>
    <tr id="r_no_order"<?= $Page->no_order->rowAttributes() ?>>
        <td class="<?= $Page->TableLeftColumnClass ?>"><span id="elh_barang_masuk_no_order"><?= $Page->no_order->caption() ?></span></td>
        <td data-name="no_order"<?= $Page->no_order->cellAttributes() ?>>
<span id="el_barang_masuk_no_order">
<span<?= $Page->no_order->viewAttributes() ?>>
<?= $Page->no_order->getViewValue() ?></span>
</span>
</td>
    </tr>
<?php } ?>
<?php if ($Page->kode_barang->Visible) { // kode_barang ?>
    <tr id="r_kode_barang"<?= $Page->kode_barang->rowAttributes() ?>>
        <td class="<?= $Page->TableLeftColumnClass ?>"><span id="elh_barang_masuk_kode_barang"><?= $Page->kode_barang->caption() ?></span></td>
        <td data-name="kode_barang"<?= $Page->kode_barang->cellAttributes() ?>>
<span id="el_barang_masuk_kode_barang">
<span<?= $Page->kode_barang->viewAttributes() ?>>
<?= $Page->kode_barang->getViewValue() ?></span>
</span>
</td>
    </tr>
<?php } ?>
<?php if ($Page->nama_barang->Visible) { // nama_barang ?>
    <tr id="r_nama_barang"<?= $Page->nama_barang->rowAttributes() ?>>
        <td class="<?= $Page->TableLeftColumnClass ?>"><span id="elh_barang_masuk_nama_barang"><?= $Page->nama_barang->caption() ?></span></td>
        <td data-name="nama_barang"<?= $Page->nama_barang->cellAttributes() ?>>
<span id="el_barang_masuk_nama_barang">
<span<?= $Page->nama_barang->viewAttributes() ?>>
<?= $Page->nama_barang->getViewValue() ?></span>
</span>
</td>
    </tr>
<?php } ?>
<?php if ($Page->jumlah_stok->Visible) { // jumlah_stok ?>
    <tr id="r_jumlah_stok"<?= $Page->jumlah_stok->rowAttributes() ?>>
        <td class="<?= $Page->TableLeftColumnClass ?>"><span id="elh_barang_masuk_jumlah_stok"><?= $Page->jumlah_stok->caption() ?></span></td>
        <td data-name="jumlah_stok"<?= $Page->jumlah_stok->cellAttributes() ?>>
<span id="el_barang_masuk_jumlah_stok">
<span<?= $Page->jumlah_stok->viewAttributes() ?>>
<?= $Page->jumlah_stok->getViewValue() ?></span>
</span>
</td>
    </tr>
<?php } ?>
<?php if ($Page->tgl_terima->Visible) { // tgl_terima ?>
    <tr id="r_tgl_terima"<?= $Page->tgl_terima->rowAttributes() ?>>
        <td class="<?= $Page->TableLeftColumnClass ?>"><span id="elh_barang_masuk_tgl_terima"><?= $Page->tgl_terima->caption() ?></span></td>
        <td data-name="tgl_terima"<?= $Page->tgl_terima->cellAttributes() ?>>
<span id="el_barang_masuk_tgl_terima">
<span<?= $Page->tgl_terima->viewAttributes() ?>>
<?= $Page->tgl_terima->getViewValue() ?></span>
</span>
</td>
    </tr>
<?php } ?>
<?php if ($Page->keterangan->Visible) { // keterangan ?>
    <tr id="r_keterangan"<?= $Page->keterangan->rowAttributes() ?>>
        <td class="<?= $Page->TableLeftColumnClass ?>"><span id="elh_barang_masuk_keterangan"><?= $Page->keterangan->caption() ?></span></td>
        <td data-name="keterangan"<?= $Page->keterangan->cellAttributes() ?>>
<span id="el_barang_masuk_keterangan">
<span<?= $Page->keterangan->viewAttributes() ?>>
<?= $Page->keterangan->getViewValue() ?></span>
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
