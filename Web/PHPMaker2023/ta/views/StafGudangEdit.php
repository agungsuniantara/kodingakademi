<?php

namespace PHPMaker2023\ta;

// Page object
$StafGudangEdit = &$Page;
?>
<?php $Page->showPageHeader(); ?>
<?php
$Page->showMessage();
?>
<main class="edit">
<form name="fstaf_gudangedit" id="fstaf_gudangedit" class="<?= $Page->FormClassName ?>" action="<?= CurrentPageUrl(false) ?>" method="post" novalidate autocomplete="off">
<script>
var currentTable = <?= JsonEncode($Page->toClientVar()) ?>;
ew.deepAssign(ew.vars, { tables: { staf_gudang: currentTable } });
var currentPageID = ew.PAGE_ID = "edit";
var currentForm;
var fstaf_gudangedit;
loadjs.ready(["wrapper", "head"], function () {
    let $ = jQuery;
    let fields = currentTable.fields;

    // Form object
    let form = new ew.FormBuilder()
        .setId("fstaf_gudangedit")
        .setPageId("edit")

        // Add fields
        .setFields([
            ["id_staf", [fields.id_staf.visible && fields.id_staf.required ? ew.Validators.required(fields.id_staf.caption) : null], fields.id_staf.isInvalid],
            ["nama_staf", [fields.nama_staf.visible && fields.nama_staf.required ? ew.Validators.required(fields.nama_staf.caption) : null], fields.nama_staf.isInvalid],
            ["_email", [fields._email.visible && fields._email.required ? ew.Validators.required(fields._email.caption) : null], fields._email.isInvalid],
            ["no_telp", [fields.no_telp.visible && fields.no_telp.required ? ew.Validators.required(fields.no_telp.caption) : null], fields.no_telp.isInvalid],
            ["_password", [fields._password.visible && fields._password.required ? ew.Validators.required(fields._password.caption) : null], fields._password.isInvalid]
        ])

        // Form_CustomValidate
        .setCustomValidate(
            function (fobj) { // DO NOT CHANGE THIS LINE! (except for adding "async" keyword)!
                    // Your custom validation code here, return false if invalid.
                    return true;
                }
        )

        // Use JavaScript validation or not
        .setValidateRequired(ew.CLIENT_VALIDATE)

        // Dynamic selection lists
        .setLists({
        })
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
<?php if (Config("CHECK_TOKEN")) { ?>
<input type="hidden" name="<?= $TokenNameKey ?>" value="<?= $TokenName ?>"><!-- CSRF token name -->
<input type="hidden" name="<?= $TokenValueKey ?>" value="<?= $TokenValue ?>"><!-- CSRF token value -->
<?php } ?>
<input type="hidden" name="t" value="staf_gudang">
<input type="hidden" name="action" id="action" value="update">
<input type="hidden" name="modal" value="<?= (int)$Page->IsModal ?>">
<?php if (IsJsonResponse()) { ?>
<input type="hidden" name="json" value="1">
<?php } ?>
<input type="hidden" name="<?= $Page->OldKeyName ?>" value="<?= $Page->OldKey ?>">
<div class="ew-edit-div"><!-- page* -->
<?php if ($Page->id_staf->Visible) { // id_staf ?>
    <div id="r_id_staf"<?= $Page->id_staf->rowAttributes() ?>>
        <label id="elh_staf_gudang_id_staf" class="<?= $Page->LeftColumnClass ?>"><?= $Page->id_staf->caption() ?><?= $Page->id_staf->Required ? $Language->phrase("FieldRequiredIndicator") : "" ?></label>
        <div class="<?= $Page->RightColumnClass ?>"><div<?= $Page->id_staf->cellAttributes() ?>>
<span id="el_staf_gudang_id_staf">
<span<?= $Page->id_staf->viewAttributes() ?>>
<input type="text" readonly class="form-control-plaintext" value="<?= HtmlEncode(RemoveHtml($Page->id_staf->getDisplayValue($Page->id_staf->EditValue))) ?>"></span>
<input type="hidden" data-table="staf_gudang" data-field="x_id_staf" data-hidden="1" name="x_id_staf" id="x_id_staf" value="<?= HtmlEncode($Page->id_staf->CurrentValue) ?>">
</span>
</div></div>
    </div>
<?php } ?>
<?php if ($Page->nama_staf->Visible) { // nama_staf ?>
    <div id="r_nama_staf"<?= $Page->nama_staf->rowAttributes() ?>>
        <label id="elh_staf_gudang_nama_staf" for="x_nama_staf" class="<?= $Page->LeftColumnClass ?>"><?= $Page->nama_staf->caption() ?><?= $Page->nama_staf->Required ? $Language->phrase("FieldRequiredIndicator") : "" ?></label>
        <div class="<?= $Page->RightColumnClass ?>"><div<?= $Page->nama_staf->cellAttributes() ?>>
<span id="el_staf_gudang_nama_staf">
<input type="<?= $Page->nama_staf->getInputTextType() ?>" name="x_nama_staf" id="x_nama_staf" data-table="staf_gudang" data-field="x_nama_staf" value="<?= $Page->nama_staf->EditValue ?>" size="30" maxlength="100" placeholder="<?= HtmlEncode($Page->nama_staf->getPlaceHolder()) ?>" data-format-pattern="<?= HtmlEncode($Page->nama_staf->formatPattern()) ?>"<?= $Page->nama_staf->editAttributes() ?> aria-describedby="x_nama_staf_help">
<?= $Page->nama_staf->getCustomMessage() ?>
<div class="invalid-feedback"><?= $Page->nama_staf->getErrorMessage() ?></div>
</span>
</div></div>
    </div>
<?php } ?>
<?php if ($Page->_email->Visible) { // email ?>
    <div id="r__email"<?= $Page->_email->rowAttributes() ?>>
        <label id="elh_staf_gudang__email" for="x__email" class="<?= $Page->LeftColumnClass ?>"><?= $Page->_email->caption() ?><?= $Page->_email->Required ? $Language->phrase("FieldRequiredIndicator") : "" ?></label>
        <div class="<?= $Page->RightColumnClass ?>"><div<?= $Page->_email->cellAttributes() ?>>
<span id="el_staf_gudang__email">
<input type="<?= $Page->_email->getInputTextType() ?>" name="x__email" id="x__email" data-table="staf_gudang" data-field="x__email" value="<?= $Page->_email->EditValue ?>" size="30" maxlength="50" placeholder="<?= HtmlEncode($Page->_email->getPlaceHolder()) ?>" data-format-pattern="<?= HtmlEncode($Page->_email->formatPattern()) ?>"<?= $Page->_email->editAttributes() ?> aria-describedby="x__email_help">
<?= $Page->_email->getCustomMessage() ?>
<div class="invalid-feedback"><?= $Page->_email->getErrorMessage() ?></div>
</span>
</div></div>
    </div>
<?php } ?>
<?php if ($Page->no_telp->Visible) { // no_telp ?>
    <div id="r_no_telp"<?= $Page->no_telp->rowAttributes() ?>>
        <label id="elh_staf_gudang_no_telp" for="x_no_telp" class="<?= $Page->LeftColumnClass ?>"><?= $Page->no_telp->caption() ?><?= $Page->no_telp->Required ? $Language->phrase("FieldRequiredIndicator") : "" ?></label>
        <div class="<?= $Page->RightColumnClass ?>"><div<?= $Page->no_telp->cellAttributes() ?>>
<span id="el_staf_gudang_no_telp">
<input type="<?= $Page->no_telp->getInputTextType() ?>" name="x_no_telp" id="x_no_telp" data-table="staf_gudang" data-field="x_no_telp" value="<?= $Page->no_telp->EditValue ?>" size="30" maxlength="12" placeholder="<?= HtmlEncode($Page->no_telp->getPlaceHolder()) ?>" data-format-pattern="<?= HtmlEncode($Page->no_telp->formatPattern()) ?>"<?= $Page->no_telp->editAttributes() ?> aria-describedby="x_no_telp_help">
<?= $Page->no_telp->getCustomMessage() ?>
<div class="invalid-feedback"><?= $Page->no_telp->getErrorMessage() ?></div>
</span>
</div></div>
    </div>
<?php } ?>
<?php if ($Page->_password->Visible) { // password ?>
    <div id="r__password"<?= $Page->_password->rowAttributes() ?>>
        <label id="elh_staf_gudang__password" for="x__password" class="<?= $Page->LeftColumnClass ?>"><?= $Page->_password->caption() ?><?= $Page->_password->Required ? $Language->phrase("FieldRequiredIndicator") : "" ?></label>
        <div class="<?= $Page->RightColumnClass ?>"><div<?= $Page->_password->cellAttributes() ?>>
<span id="el_staf_gudang__password">
<input type="<?= $Page->_password->getInputTextType() ?>" name="x__password" id="x__password" data-table="staf_gudang" data-field="x__password" value="<?= $Page->_password->EditValue ?>" size="30" maxlength="10" placeholder="<?= HtmlEncode($Page->_password->getPlaceHolder()) ?>" data-format-pattern="<?= HtmlEncode($Page->_password->formatPattern()) ?>"<?= $Page->_password->editAttributes() ?> aria-describedby="x__password_help">
<?= $Page->_password->getCustomMessage() ?>
<div class="invalid-feedback"><?= $Page->_password->getErrorMessage() ?></div>
</span>
</div></div>
    </div>
<?php } ?>
</div><!-- /page* -->
<?= $Page->IsModal ? '<template class="ew-modal-buttons">' : '<div class="row ew-buttons">' ?><!-- buttons .row -->
    <div class="<?= $Page->OffsetColumnClass ?>"><!-- buttons offset -->
<button class="btn btn-primary ew-btn" name="btn-action" id="btn-action" type="submit" form="fstaf_gudangedit"><?= $Language->phrase("SaveBtn") ?></button>
<?php if (IsJsonResponse()) { ?>
<button class="btn btn-default ew-btn" name="btn-cancel" id="btn-cancel" type="button" data-bs-dismiss="modal"><?= $Language->phrase("CancelBtn") ?></button>
<?php } else { ?>
<button class="btn btn-default ew-btn" name="btn-cancel" id="btn-cancel" type="button" form="fstaf_gudangedit" data-href="<?= HtmlEncode(GetUrl($Page->getReturnUrl())) ?>"><?= $Language->phrase("CancelBtn") ?></button>
<?php } ?>
    </div><!-- /buttons offset -->
<?= $Page->IsModal ? "</template>" : "</div>" ?><!-- /buttons .row -->
</form>
</main>
<?php
$Page->showPageFooter();
echo GetDebugMessage();
?>
<script>
// Field event handlers
loadjs.ready("head", function() {
    ew.addEventHandlers("staf_gudang");
});
</script>
<script>
loadjs.ready("load", function () {
    // Write your table-specific startup script here, no need to add script tags.
});
</script>
