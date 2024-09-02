<?php

namespace PHPMaker2023\ta;

// Page object
$OrderBarangEdit = &$Page;
?>
<?php $Page->showPageHeader(); ?>
<?php
$Page->showMessage();
?>
<main class="edit">
<form name="forder_barangedit" id="forder_barangedit" class="<?= $Page->FormClassName ?>" action="<?= CurrentPageUrl(false) ?>" method="post" novalidate autocomplete="off">
<script>
var currentTable = <?= JsonEncode($Page->toClientVar()) ?>;
ew.deepAssign(ew.vars, { tables: { order_barang: currentTable } });
var currentPageID = ew.PAGE_ID = "edit";
var currentForm;
var forder_barangedit;
loadjs.ready(["wrapper", "head"], function () {
    let $ = jQuery;
    let fields = currentTable.fields;

    // Form object
    let form = new ew.FormBuilder()
        .setId("forder_barangedit")
        .setPageId("edit")

        // Add fields
        .setFields([
            ["id_receipt", [fields.id_receipt.visible && fields.id_receipt.required ? ew.Validators.required(fields.id_receipt.caption) : null], fields.id_receipt.isInvalid],
            ["no_order", [fields.no_order.visible && fields.no_order.required ? ew.Validators.required(fields.no_order.caption) : null], fields.no_order.isInvalid],
            ["kode_barang", [fields.kode_barang.visible && fields.kode_barang.required ? ew.Validators.required(fields.kode_barang.caption) : null], fields.kode_barang.isInvalid],
            ["nama_barang", [fields.nama_barang.visible && fields.nama_barang.required ? ew.Validators.required(fields.nama_barang.caption) : null], fields.nama_barang.isInvalid],
            ["jumlah_barang", [fields.jumlah_barang.visible && fields.jumlah_barang.required ? ew.Validators.required(fields.jumlah_barang.caption) : null, ew.Validators.integer], fields.jumlah_barang.isInvalid]
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
<input type="hidden" name="t" value="order_barang">
<input type="hidden" name="action" id="action" value="update">
<input type="hidden" name="modal" value="<?= (int)$Page->IsModal ?>">
<?php if (IsJsonResponse()) { ?>
<input type="hidden" name="json" value="1">
<?php } ?>
<input type="hidden" name="<?= $Page->OldKeyName ?>" value="<?= $Page->OldKey ?>">
<div class="ew-edit-div"><!-- page* -->
<?php if ($Page->id_receipt->Visible) { // id_receipt ?>
    <div id="r_id_receipt"<?= $Page->id_receipt->rowAttributes() ?>>
        <label id="elh_order_barang_id_receipt" class="<?= $Page->LeftColumnClass ?>"><?= $Page->id_receipt->caption() ?><?= $Page->id_receipt->Required ? $Language->phrase("FieldRequiredIndicator") : "" ?></label>
        <div class="<?= $Page->RightColumnClass ?>"><div<?= $Page->id_receipt->cellAttributes() ?>>
<span id="el_order_barang_id_receipt">
<span<?= $Page->id_receipt->viewAttributes() ?>>
<input type="text" readonly class="form-control-plaintext" value="<?= HtmlEncode(RemoveHtml($Page->id_receipt->getDisplayValue($Page->id_receipt->EditValue))) ?>"></span>
<input type="hidden" data-table="order_barang" data-field="x_id_receipt" data-hidden="1" name="x_id_receipt" id="x_id_receipt" value="<?= HtmlEncode($Page->id_receipt->CurrentValue) ?>">
</span>
</div></div>
    </div>
<?php } ?>
<?php if ($Page->no_order->Visible) { // no_order ?>
    <div id="r_no_order"<?= $Page->no_order->rowAttributes() ?>>
        <label id="elh_order_barang_no_order" for="x_no_order" class="<?= $Page->LeftColumnClass ?>"><?= $Page->no_order->caption() ?><?= $Page->no_order->Required ? $Language->phrase("FieldRequiredIndicator") : "" ?></label>
        <div class="<?= $Page->RightColumnClass ?>"><div<?= $Page->no_order->cellAttributes() ?>>
<span id="el_order_barang_no_order">
<input type="<?= $Page->no_order->getInputTextType() ?>" name="x_no_order" id="x_no_order" data-table="order_barang" data-field="x_no_order" value="<?= $Page->no_order->EditValue ?>" size="30" maxlength="20" placeholder="<?= HtmlEncode($Page->no_order->getPlaceHolder()) ?>" data-format-pattern="<?= HtmlEncode($Page->no_order->formatPattern()) ?>"<?= $Page->no_order->editAttributes() ?> aria-describedby="x_no_order_help">
<?= $Page->no_order->getCustomMessage() ?>
<div class="invalid-feedback"><?= $Page->no_order->getErrorMessage() ?></div>
</span>
</div></div>
    </div>
<?php } ?>
<?php if ($Page->kode_barang->Visible) { // kode_barang ?>
    <div id="r_kode_barang"<?= $Page->kode_barang->rowAttributes() ?>>
        <label id="elh_order_barang_kode_barang" for="x_kode_barang" class="<?= $Page->LeftColumnClass ?>"><?= $Page->kode_barang->caption() ?><?= $Page->kode_barang->Required ? $Language->phrase("FieldRequiredIndicator") : "" ?></label>
        <div class="<?= $Page->RightColumnClass ?>"><div<?= $Page->kode_barang->cellAttributes() ?>>
<span id="el_order_barang_kode_barang">
<input type="<?= $Page->kode_barang->getInputTextType() ?>" name="x_kode_barang" id="x_kode_barang" data-table="order_barang" data-field="x_kode_barang" value="<?= $Page->kode_barang->EditValue ?>" size="30" maxlength="12" placeholder="<?= HtmlEncode($Page->kode_barang->getPlaceHolder()) ?>" data-format-pattern="<?= HtmlEncode($Page->kode_barang->formatPattern()) ?>"<?= $Page->kode_barang->editAttributes() ?> aria-describedby="x_kode_barang_help">
<?= $Page->kode_barang->getCustomMessage() ?>
<div class="invalid-feedback"><?= $Page->kode_barang->getErrorMessage() ?></div>
</span>
</div></div>
    </div>
<?php } ?>
<?php if ($Page->nama_barang->Visible) { // nama_barang ?>
    <div id="r_nama_barang"<?= $Page->nama_barang->rowAttributes() ?>>
        <label id="elh_order_barang_nama_barang" for="x_nama_barang" class="<?= $Page->LeftColumnClass ?>"><?= $Page->nama_barang->caption() ?><?= $Page->nama_barang->Required ? $Language->phrase("FieldRequiredIndicator") : "" ?></label>
        <div class="<?= $Page->RightColumnClass ?>"><div<?= $Page->nama_barang->cellAttributes() ?>>
<span id="el_order_barang_nama_barang">
<input type="<?= $Page->nama_barang->getInputTextType() ?>" name="x_nama_barang" id="x_nama_barang" data-table="order_barang" data-field="x_nama_barang" value="<?= $Page->nama_barang->EditValue ?>" size="30" maxlength="100" placeholder="<?= HtmlEncode($Page->nama_barang->getPlaceHolder()) ?>" data-format-pattern="<?= HtmlEncode($Page->nama_barang->formatPattern()) ?>"<?= $Page->nama_barang->editAttributes() ?> aria-describedby="x_nama_barang_help">
<?= $Page->nama_barang->getCustomMessage() ?>
<div class="invalid-feedback"><?= $Page->nama_barang->getErrorMessage() ?></div>
</span>
</div></div>
    </div>
<?php } ?>
<?php if ($Page->jumlah_barang->Visible) { // jumlah_barang ?>
    <div id="r_jumlah_barang"<?= $Page->jumlah_barang->rowAttributes() ?>>
        <label id="elh_order_barang_jumlah_barang" for="x_jumlah_barang" class="<?= $Page->LeftColumnClass ?>"><?= $Page->jumlah_barang->caption() ?><?= $Page->jumlah_barang->Required ? $Language->phrase("FieldRequiredIndicator") : "" ?></label>
        <div class="<?= $Page->RightColumnClass ?>"><div<?= $Page->jumlah_barang->cellAttributes() ?>>
<span id="el_order_barang_jumlah_barang">
<input type="<?= $Page->jumlah_barang->getInputTextType() ?>" name="x_jumlah_barang" id="x_jumlah_barang" data-table="order_barang" data-field="x_jumlah_barang" value="<?= $Page->jumlah_barang->EditValue ?>" size="30" placeholder="<?= HtmlEncode($Page->jumlah_barang->getPlaceHolder()) ?>" data-format-pattern="<?= HtmlEncode($Page->jumlah_barang->formatPattern()) ?>"<?= $Page->jumlah_barang->editAttributes() ?> aria-describedby="x_jumlah_barang_help">
<?= $Page->jumlah_barang->getCustomMessage() ?>
<div class="invalid-feedback"><?= $Page->jumlah_barang->getErrorMessage() ?></div>
</span>
</div></div>
    </div>
<?php } ?>
</div><!-- /page* -->
<?= $Page->IsModal ? '<template class="ew-modal-buttons">' : '<div class="row ew-buttons">' ?><!-- buttons .row -->
    <div class="<?= $Page->OffsetColumnClass ?>"><!-- buttons offset -->
<button class="btn btn-primary ew-btn" name="btn-action" id="btn-action" type="submit" form="forder_barangedit"><?= $Language->phrase("SaveBtn") ?></button>
<?php if (IsJsonResponse()) { ?>
<button class="btn btn-default ew-btn" name="btn-cancel" id="btn-cancel" type="button" data-bs-dismiss="modal"><?= $Language->phrase("CancelBtn") ?></button>
<?php } else { ?>
<button class="btn btn-default ew-btn" name="btn-cancel" id="btn-cancel" type="button" form="forder_barangedit" data-href="<?= HtmlEncode(GetUrl($Page->getReturnUrl())) ?>"><?= $Language->phrase("CancelBtn") ?></button>
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
    ew.addEventHandlers("order_barang");
});
</script>
<script>
loadjs.ready("load", function () {
    // Write your table-specific startup script here, no need to add script tags.
});
</script>
