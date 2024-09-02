<?php

namespace PHPMaker2023\ta;

// Page object
$OrderBarangView = &$Page;
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
<form name="forder_barangview" id="forder_barangview" class="ew-form ew-view-form overlay-wrapper" action="<?= CurrentPageUrl(false) ?>" method="post" novalidate autocomplete="off">
<?php if (!$Page->isExport()) { ?>
<script>
var currentTable = <?= JsonEncode($Page->toClientVar()) ?>;
ew.deepAssign(ew.vars, { tables: { order_barang: currentTable } });
var currentPageID = ew.PAGE_ID = "view";
var currentForm;
var forder_barangview;
loadjs.ready(["wrapper", "head"], function () {
    let $ = jQuery;
    let fields = currentTable.fields;

    // Form object
    let form = new ew.FormBuilder()
        .setId("forder_barangview")
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
<input type="hidden" name="t" value="order_barang">
<input type="hidden" name="modal" value="<?= (int)$Page->IsModal ?>">
<table class="<?= $Page->TableClass ?>">
<?php if ($Page->id_receipt->Visible) { // id_receipt ?>
    <tr id="r_id_receipt"<?= $Page->id_receipt->rowAttributes() ?>>
        <td class="<?= $Page->TableLeftColumnClass ?>"><span id="elh_order_barang_id_receipt"><?= $Page->id_receipt->caption() ?></span></td>
        <td data-name="id_receipt"<?= $Page->id_receipt->cellAttributes() ?>>
<span id="el_order_barang_id_receipt">
<span<?= $Page->id_receipt->viewAttributes() ?>>
<?= $Page->id_receipt->getViewValue() ?></span>
</span>
</td>
    </tr>
<?php } ?>
<?php if ($Page->no_order->Visible) { // no_order ?>
    <tr id="r_no_order"<?= $Page->no_order->rowAttributes() ?>>
        <td class="<?= $Page->TableLeftColumnClass ?>"><span id="elh_order_barang_no_order"><?= $Page->no_order->caption() ?></span></td>
        <td data-name="no_order"<?= $Page->no_order->cellAttributes() ?>>
<span id="el_order_barang_no_order">
<span<?= $Page->no_order->viewAttributes() ?>>
<?= $Page->no_order->getViewValue() ?></span>
</span>
</td>
    </tr>
<?php } ?>
<?php if ($Page->kode_barang->Visible) { // kode_barang ?>
    <tr id="r_kode_barang"<?= $Page->kode_barang->rowAttributes() ?>>
        <td class="<?= $Page->TableLeftColumnClass ?>"><span id="elh_order_barang_kode_barang"><?= $Page->kode_barang->caption() ?></span></td>
        <td data-name="kode_barang"<?= $Page->kode_barang->cellAttributes() ?>>
<span id="el_order_barang_kode_barang">
<span<?= $Page->kode_barang->viewAttributes() ?>>
<?= $Page->kode_barang->getViewValue() ?></span>
</span>
</td>
    </tr>
<?php } ?>
<?php if ($Page->nama_barang->Visible) { // nama_barang ?>
    <tr id="r_nama_barang"<?= $Page->nama_barang->rowAttributes() ?>>
        <td class="<?= $Page->TableLeftColumnClass ?>"><span id="elh_order_barang_nama_barang"><?= $Page->nama_barang->caption() ?></span></td>
        <td data-name="nama_barang"<?= $Page->nama_barang->cellAttributes() ?>>
<span id="el_order_barang_nama_barang">
<span<?= $Page->nama_barang->viewAttributes() ?>>
<?= $Page->nama_barang->getViewValue() ?></span>
</span>
</td>
    </tr>
<?php } ?>
<?php if ($Page->jumlah_barang->Visible) { // jumlah_barang ?>
    <tr id="r_jumlah_barang"<?= $Page->jumlah_barang->rowAttributes() ?>>
        <td class="<?= $Page->TableLeftColumnClass ?>"><span id="elh_order_barang_jumlah_barang"><?= $Page->jumlah_barang->caption() ?></span></td>
        <td data-name="jumlah_barang"<?= $Page->jumlah_barang->cellAttributes() ?>>
<span id="el_order_barang_jumlah_barang">
<span<?= $Page->jumlah_barang->viewAttributes() ?>>
<?= $Page->jumlah_barang->getViewValue() ?></span>
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
