<?php

namespace PHPMaker2023\ta;

// Page object
$StafGudangDelete = &$Page;
?>
<script>
var currentTable = <?= JsonEncode($Page->toClientVar()) ?>;
ew.deepAssign(ew.vars, { tables: { staf_gudang: currentTable } });
var currentPageID = ew.PAGE_ID = "delete";
var currentForm;
var fstaf_gudangdelete;
loadjs.ready(["wrapper", "head"], function () {
    let $ = jQuery;
    let fields = currentTable.fields;

    // Form object
    let form = new ew.FormBuilder()
        .setId("fstaf_gudangdelete")
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
<form name="fstaf_gudangdelete" id="fstaf_gudangdelete" class="ew-form ew-delete-form" action="<?= CurrentPageUrl(false) ?>" method="post" novalidate autocomplete="off">
<?php if (Config("CHECK_TOKEN")) { ?>
<input type="hidden" name="<?= $TokenNameKey ?>" value="<?= $TokenName ?>"><!-- CSRF token name -->
<input type="hidden" name="<?= $TokenValueKey ?>" value="<?= $TokenValue ?>"><!-- CSRF token value -->
<?php } ?>
<input type="hidden" name="t" value="staf_gudang">
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
<?php if ($Page->id_staf->Visible) { // id_staf ?>
        <th class="<?= $Page->id_staf->headerCellClass() ?>"><span id="elh_staf_gudang_id_staf" class="staf_gudang_id_staf"><?= $Page->id_staf->caption() ?></span></th>
<?php } ?>
<?php if ($Page->nama_staf->Visible) { // nama_staf ?>
        <th class="<?= $Page->nama_staf->headerCellClass() ?>"><span id="elh_staf_gudang_nama_staf" class="staf_gudang_nama_staf"><?= $Page->nama_staf->caption() ?></span></th>
<?php } ?>
<?php if ($Page->_email->Visible) { // email ?>
        <th class="<?= $Page->_email->headerCellClass() ?>"><span id="elh_staf_gudang__email" class="staf_gudang__email"><?= $Page->_email->caption() ?></span></th>
<?php } ?>
<?php if ($Page->no_telp->Visible) { // no_telp ?>
        <th class="<?= $Page->no_telp->headerCellClass() ?>"><span id="elh_staf_gudang_no_telp" class="staf_gudang_no_telp"><?= $Page->no_telp->caption() ?></span></th>
<?php } ?>
<?php if ($Page->_password->Visible) { // password ?>
        <th class="<?= $Page->_password->headerCellClass() ?>"><span id="elh_staf_gudang__password" class="staf_gudang__password"><?= $Page->_password->caption() ?></span></th>
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
<?php if ($Page->id_staf->Visible) { // id_staf ?>
        <td<?= $Page->id_staf->cellAttributes() ?>>
<span id="">
<span<?= $Page->id_staf->viewAttributes() ?>>
<?= $Page->id_staf->getViewValue() ?></span>
</span>
</td>
<?php } ?>
<?php if ($Page->nama_staf->Visible) { // nama_staf ?>
        <td<?= $Page->nama_staf->cellAttributes() ?>>
<span id="">
<span<?= $Page->nama_staf->viewAttributes() ?>>
<?= $Page->nama_staf->getViewValue() ?></span>
</span>
</td>
<?php } ?>
<?php if ($Page->_email->Visible) { // email ?>
        <td<?= $Page->_email->cellAttributes() ?>>
<span id="">
<span<?= $Page->_email->viewAttributes() ?>>
<?= $Page->_email->getViewValue() ?></span>
</span>
</td>
<?php } ?>
<?php if ($Page->no_telp->Visible) { // no_telp ?>
        <td<?= $Page->no_telp->cellAttributes() ?>>
<span id="">
<span<?= $Page->no_telp->viewAttributes() ?>>
<?= $Page->no_telp->getViewValue() ?></span>
</span>
</td>
<?php } ?>
<?php if ($Page->_password->Visible) { // password ?>
        <td<?= $Page->_password->cellAttributes() ?>>
<span id="">
<span<?= $Page->_password->viewAttributes() ?>>
<?= $Page->_password->getViewValue() ?></span>
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
