<?php

namespace PHPMaker2023\ta;

// Page object
$AdminDelete = &$Page;
?>
<script>
var currentTable = <?= JsonEncode($Page->toClientVar()) ?>;
ew.deepAssign(ew.vars, { tables: { admin: currentTable } });
var currentPageID = ew.PAGE_ID = "delete";
var currentForm;
var fadmindelete;
loadjs.ready(["wrapper", "head"], function () {
    let $ = jQuery;
    let fields = currentTable.fields;

    // Form object
    let form = new ew.FormBuilder()
        .setId("fadmindelete")
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
<form name="fadmindelete" id="fadmindelete" class="ew-form ew-delete-form" action="<?= CurrentPageUrl(false) ?>" method="post" novalidate autocomplete="off">
<?php if (Config("CHECK_TOKEN")) { ?>
<input type="hidden" name="<?= $TokenNameKey ?>" value="<?= $TokenName ?>"><!-- CSRF token name -->
<input type="hidden" name="<?= $TokenValueKey ?>" value="<?= $TokenValue ?>"><!-- CSRF token value -->
<?php } ?>
<input type="hidden" name="t" value="admin">
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
<?php if ($Page->id_admin->Visible) { // id_admin ?>
        <th class="<?= $Page->id_admin->headerCellClass() ?>"><span id="elh_admin_id_admin" class="admin_id_admin"><?= $Page->id_admin->caption() ?></span></th>
<?php } ?>
<?php if ($Page->nama_admin->Visible) { // nama_admin ?>
        <th class="<?= $Page->nama_admin->headerCellClass() ?>"><span id="elh_admin_nama_admin" class="admin_nama_admin"><?= $Page->nama_admin->caption() ?></span></th>
<?php } ?>
<?php if ($Page->_email->Visible) { // email ?>
        <th class="<?= $Page->_email->headerCellClass() ?>"><span id="elh_admin__email" class="admin__email"><?= $Page->_email->caption() ?></span></th>
<?php } ?>
<?php if ($Page->no_telp->Visible) { // no_telp ?>
        <th class="<?= $Page->no_telp->headerCellClass() ?>"><span id="elh_admin_no_telp" class="admin_no_telp"><?= $Page->no_telp->caption() ?></span></th>
<?php } ?>
<?php if ($Page->_password->Visible) { // password ?>
        <th class="<?= $Page->_password->headerCellClass() ?>"><span id="elh_admin__password" class="admin__password"><?= $Page->_password->caption() ?></span></th>
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
<?php if ($Page->id_admin->Visible) { // id_admin ?>
        <td<?= $Page->id_admin->cellAttributes() ?>>
<span id="">
<span<?= $Page->id_admin->viewAttributes() ?>>
<?= $Page->id_admin->getViewValue() ?></span>
</span>
</td>
<?php } ?>
<?php if ($Page->nama_admin->Visible) { // nama_admin ?>
        <td<?= $Page->nama_admin->cellAttributes() ?>>
<span id="">
<span<?= $Page->nama_admin->viewAttributes() ?>>
<?= $Page->nama_admin->getViewValue() ?></span>
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
