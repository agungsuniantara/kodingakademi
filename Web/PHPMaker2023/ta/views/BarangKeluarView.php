<?php

namespace PHPMaker2023\ta;

// Page object
$BarangKeluarView = &$Page;
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
<form name="fbarang_keluarview" id="fbarang_keluarview" class="ew-form ew-view-form overlay-wrapper" action="<?= CurrentPageUrl(false) ?>" method="post" novalidate autocomplete="off">
<?php if (!$Page->isExport()) { ?>
<script>
var currentTable = <?= JsonEncode($Page->toClientVar()) ?>;
ew.deepAssign(ew.vars, { tables: { barang_keluar: currentTable } });
var currentPageID = ew.PAGE_ID = "view";
var currentForm;
var fbarang_keluarview;
loadjs.ready(["wrapper", "head"], function () {
    let $ = jQuery;
    let fields = currentTable.fields;

    // Form object
    let form = new ew.FormBuilder()
        .setId("fbarang_keluarview")
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
<input type="hidden" name="t" value="barang_keluar">
<input type="hidden" name="modal" value="<?= (int)$Page->IsModal ?>">
<table class="<?= $Page->TableClass ?>">
<?php if ($Page->id_brgkel->Visible) { // id_brgkel ?>
    <tr id="r_id_brgkel"<?= $Page->id_brgkel->rowAttributes() ?>>
        <td class="<?= $Page->TableLeftColumnClass ?>"><span id="elh_barang_keluar_id_brgkel"><?= $Page->id_brgkel->caption() ?></span></td>
        <td data-name="id_brgkel"<?= $Page->id_brgkel->cellAttributes() ?>>
<span id="el_barang_keluar_id_brgkel">
<span<?= $Page->id_brgkel->viewAttributes() ?>>
<?= $Page->id_brgkel->getViewValue() ?></span>
</span>
</td>
    </tr>
<?php } ?>
<?php if ($Page->kode_barang->Visible) { // kode_barang ?>
    <tr id="r_kode_barang"<?= $Page->kode_barang->rowAttributes() ?>>
        <td class="<?= $Page->TableLeftColumnClass ?>"><span id="elh_barang_keluar_kode_barang"><?= $Page->kode_barang->caption() ?></span></td>
        <td data-name="kode_barang"<?= $Page->kode_barang->cellAttributes() ?>>
<span id="el_barang_keluar_kode_barang">
<span<?= $Page->kode_barang->viewAttributes() ?>>
<?= $Page->kode_barang->getViewValue() ?></span>
</span>
</td>
    </tr>
<?php } ?>
<?php if ($Page->nama_barang->Visible) { // nama_barang ?>
    <tr id="r_nama_barang"<?= $Page->nama_barang->rowAttributes() ?>>
        <td class="<?= $Page->TableLeftColumnClass ?>"><span id="elh_barang_keluar_nama_barang"><?= $Page->nama_barang->caption() ?></span></td>
        <td data-name="nama_barang"<?= $Page->nama_barang->cellAttributes() ?>>
<span id="el_barang_keluar_nama_barang">
<span<?= $Page->nama_barang->viewAttributes() ?>>
<?= $Page->nama_barang->getViewValue() ?></span>
</span>
</td>
    </tr>
<?php } ?>
<?php if ($Page->jumlah_stok->Visible) { // jumlah_stok ?>
    <tr id="r_jumlah_stok"<?= $Page->jumlah_stok->rowAttributes() ?>>
        <td class="<?= $Page->TableLeftColumnClass ?>"><span id="elh_barang_keluar_jumlah_stok"><?= $Page->jumlah_stok->caption() ?></span></td>
        <td data-name="jumlah_stok"<?= $Page->jumlah_stok->cellAttributes() ?>>
<span id="el_barang_keluar_jumlah_stok">
<span<?= $Page->jumlah_stok->viewAttributes() ?>>
<?= $Page->jumlah_stok->getViewValue() ?></span>
</span>
</td>
    </tr>
<?php } ?>
<?php if ($Page->tgl_keluar->Visible) { // tgl_keluar ?>
    <tr id="r_tgl_keluar"<?= $Page->tgl_keluar->rowAttributes() ?>>
        <td class="<?= $Page->TableLeftColumnClass ?>"><span id="elh_barang_keluar_tgl_keluar"><?= $Page->tgl_keluar->caption() ?></span></td>
        <td data-name="tgl_keluar"<?= $Page->tgl_keluar->cellAttributes() ?>>
<span id="el_barang_keluar_tgl_keluar">
<span<?= $Page->tgl_keluar->viewAttributes() ?>>
<?= $Page->tgl_keluar->getViewValue() ?></span>
</span>
</td>
    </tr>
<?php } ?>
<?php if ($Page->keterangan->Visible) { // keterangan ?>
    <tr id="r_keterangan"<?= $Page->keterangan->rowAttributes() ?>>
        <td class="<?= $Page->TableLeftColumnClass ?>"><span id="elh_barang_keluar_keterangan"><?= $Page->keterangan->caption() ?></span></td>
        <td data-name="keterangan"<?= $Page->keterangan->cellAttributes() ?>>
<span id="el_barang_keluar_keterangan">
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
