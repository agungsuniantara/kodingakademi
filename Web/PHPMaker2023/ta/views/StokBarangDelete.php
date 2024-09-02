<?php

namespace PHPMaker2023\ta;

// Page object
$StokBarangDelete = &$Page;
?>
<script>
var currentTable = <?= JsonEncode($Page->toClientVar()) ?>;
ew.deepAssign(ew.vars, { tables: { stok_barang: currentTable } });
var currentPageID = ew.PAGE_ID = "delete";
var currentForm;
var fstok_barangdelete;
loadjs.ready(["wrapper", "head"], function () {
    let $ = jQuery;
    let fields = currentTable.fields;

    // Form object
    let form = new ew.FormBuilder()
        .setId("fstok_barangdelete")
        .setPageId("delete")
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
<?php $Page->showPageHeader(); ?>
<?php
$Page->showMessage();
?>
<form name="fstok_barangdelete" id="fstok_barangdelete" class="ew-form ew-delete-form" action="<?= CurrentPageUrl(false) ?>" method="post" novalidate autocomplete="off">
<?php if (Config("CHECK_TOKEN")) { ?>
<input type="hidden" name="<?= $TokenNameKey ?>" value="<?= $TokenName ?>"><!-- CSRF token name -->
<input type="hidden" name="<?= $TokenValueKey ?>" value="<?= $TokenValue ?>"><!-- CSRF token value -->
<?php } ?>
<input type="hidden" name="t" value="stok_barang">
<input type="hidden" name="action" id="action" value="delete">
<?php foreach ($Page->RecKeys as $key) { ?>
<?php $keyvalue = is_array($key) ? implode(Config("COMPOSITE_KEY_SEPARATOR"), $key) : $key; ?>
<input type="hidden" name="key_m[]" value="<?= HtmlEncode($keyvalue) ?>">
<?php } ?>
<div class="card ew-card ew-grid <?= $Page->TableGridClass ?>">
<div class="card-body ew-grid-middle-panel <?= $Page->TableContainerClass ?>" style="<?= $Page->TableContainerStyle ?>">
<table class="<?= $Page->TableClass ?>">
    <thead>
    <tr class="ew-table-header">
<?php if ($Page->id_barang->Visible) { // id_barang ?>
        <th class="<?= $Page->id_barang->headerCellClass() ?>"><span id="elh_stok_barang_id_barang" class="stok_barang_id_barang"><?= $Page->id_barang->caption() ?></span></th>
<?php } ?>
<?php if ($Page->kode_barang->Visible) { // kode_barang ?>
        <th class="<?= $Page->kode_barang->headerCellClass() ?>"><span id="elh_stok_barang_kode_barang" class="stok_barang_kode_barang"><?= $Page->kode_barang->caption() ?></span></th>
<?php } ?>
<?php if ($Page->nama_barang->Visible) { // nama_barang ?>
        <th class="<?= $Page->nama_barang->headerCellClass() ?>"><span id="elh_stok_barang_nama_barang" class="stok_barang_nama_barang"><?= $Page->nama_barang->caption() ?></span></th>
<?php } ?>
<?php if ($Page->jumlah_stok->Visible) { // jumlah_stok ?>
        <th class="<?= $Page->jumlah_stok->headerCellClass() ?>"><span id="elh_stok_barang_jumlah_stok" class="stok_barang_jumlah_stok"><?= $Page->jumlah_stok->caption() ?></span></th>
<?php } ?>
    </tr>
    </thead>
    <tbody>
<?php
$Page->RecordCount = 0;
$i = 0;
while (!$Page->Recordset->EOF) {
    $Page->RecordCount++;
    $Page->RowCount++;

    // Set row properties
    $Page->resetAttributes();
    $Page->RowType = ROWTYPE_VIEW; // View

    // Get the field contents
    $Page->loadRowValues($Page->Recordset);

    // Render row
    $Page->renderRow();
?>
    <tr <?= $Page->rowAttributes() ?>>
<?php if ($Page->id_barang->Visible) { // id_barang ?>
        <td<?= $Page->id_barang->cellAttributes() ?>>
<span id="">
<span<?= $Page->id_barang->viewAttributes() ?>>
<?= $Page->id_barang->getViewValue() ?></span>
</span>
</td>
<?php } ?>
<?php if ($Page->kode_barang->Visible) { // kode_barang ?>
        <td<?= $Page->kode_barang->cellAttributes() ?>>
<span id="">
<span<?= $Page->kode_barang->viewAttributes() ?>>
<?= $Page->kode_barang->getViewValue() ?></span>
</span>
</td>
<?php } ?>
<?php if ($Page->nama_barang->Visible) { // nama_barang ?>
        <td<?= $Page->nama_barang->cellAttributes() ?>>
<span id="">
<span<?= $Page->nama_barang->viewAttributes() ?>>
<?= $Page->nama_barang->getViewValue() ?></span>
</span>
</td>
<?php } ?>
<?php if ($Page->jumlah_stok->Visible) { // jumlah_stok ?>
        <td<?= $Page->jumlah_stok->cellAttributes() ?>>
<span id="">
<span<?= $Page->jumlah_stok->viewAttributes() ?>>
<?= $Page->jumlah_stok->getViewValue() ?></span>
</span>
</td>
<?php } ?>
    </tr>
<?php
    $Page->Recordset->moveNext();
}
$Page->Recordset->close();
?>
</tbody>
</table>
</div>
</div>
<div class="ew-buttons ew-desktop-buttons">
<button class="btn btn-primary ew-btn" name="btn-action" id="btn-action" type="submit"><?= $Language->phrase("DeleteBtn") ?></button>
<button class="btn btn-default ew-btn" name="btn-cancel" id="btn-cancel" type="button" data-href="<?= HtmlEncode(GetUrl($Page->getReturnUrl())) ?>"><?= $Language->phrase("CancelBtn") ?></button>
</div>
</form>
<?php
$Page->showPageFooter();
echo GetDebugMessage();
?>
<script>
loadjs.ready("load", function () {
    // Write your table-specific startup script here, no need to add script tags.
});
</script>
