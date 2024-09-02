<?php

namespace PHPMaker2023\ta;

// Page object
$BarangMasukEdit = &$Page;
?>
<?php $Page->showPageHeader(); ?>
<?php
$Page->showMessage();
?>
<main class="edit">
<form name="fbarang_masukedit" id="fbarang_masukedit" class="<?= $Page->FormClassName ?>" action="<?= CurrentPageUrl(false) ?>" method="post" novalidate autocomplete="off">
<script>
var currentTable = <?= JsonEncode($Page->toClientVar()) ?>;
ew.deepAssign(ew.vars, { tables: { barang_masuk: currentTable } });
var currentPageID = ew.PAGE_ID = "edit";
var currentForm;
var fbarang_masukedit;
loadjs.ready(["wrapper", "head"], function () {
    let $ = jQuery;
    let fields = currentTable.fields;

    // Form object
    let form = new ew.FormBuilder()
        .setId("fbarang_masukedit")
        .setPageId("edit")

        // Add fields
        .setFields([
            ["id_brgmsk", [fields.id_brgmsk.visible && fields.id_brgmsk.required ? ew.Validators.required(fields.id_brgmsk.caption) : null], fields.id_brgmsk.isInvalid],
            ["no_order", [fields.no_order.visible && fields.no_order.required ? ew.Validators.required(fields.no_order.caption) : null], fields.no_order.isInvalid],
            ["kode_barang", [fields.kode_barang.visible && fields.kode_barang.required ? ew.Validators.required(fields.kode_barang.caption) : null], fields.kode_barang.isInvalid],
            ["nama_barang", [fields.nama_barang.visible && fields.nama_barang.required ? ew.Validators.required(fields.nama_barang.caption) : null], fields.nama_barang.isInvalid],
            ["jumlah_stok", [fields.jumlah_stok.visible && fields.jumlah_stok.required ? ew.Validators.required(fields.jumlah_stok.caption) : null, ew.Validators.integer], fields.jumlah_stok.isInvalid],
            ["tgl_terima", [fields.tgl_terima.visible && fields.tgl_terima.required ? ew.Validators.required(fields.tgl_terima.caption) : null, ew.Validators.datetime(fields.tgl_terima.clientFormatPattern)], fields.tgl_terima.isInvalid],
            ["keterangan", [fields.keterangan.visible && fields.keterangan.required ? ew.Validators.required(fields.keterangan.caption) : null], fields.keterangan.isInvalid]
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
            "no_order": <?= $Page->no_order->toClientList($Page) ?>,
            "kode_barang": <?= $Page->kode_barang->toClientList($Page) ?>,
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
<input type="hidden" name="t" value="barang_masuk">
<input type="hidden" name="action" id="action" value="update">
<input type="hidden" name="modal" value="<?= (int)$Page->IsModal ?>">
<?php if (IsJsonResponse()) { ?>
<input type="hidden" name="json" value="1">
<?php } ?>
<input type="hidden" name="<?= $Page->OldKeyName ?>" value="<?= $Page->OldKey ?>">
<div class="ew-edit-div"><!-- page* -->
<?php if ($Page->id_brgmsk->Visible) { // id_brgmsk ?>
    <div id="r_id_brgmsk"<?= $Page->id_brgmsk->rowAttributes() ?>>
        <label id="elh_barang_masuk_id_brgmsk" class="<?= $Page->LeftColumnClass ?>"><?= $Page->id_brgmsk->caption() ?><?= $Page->id_brgmsk->Required ? $Language->phrase("FieldRequiredIndicator") : "" ?></label>
        <div class="<?= $Page->RightColumnClass ?>"><div<?= $Page->id_brgmsk->cellAttributes() ?>>
<span id="el_barang_masuk_id_brgmsk">
<span<?= $Page->id_brgmsk->viewAttributes() ?>>
<input type="text" readonly class="form-control-plaintext" value="<?= HtmlEncode(RemoveHtml($Page->id_brgmsk->getDisplayValue($Page->id_brgmsk->EditValue))) ?>"></span>
<input type="hidden" data-table="barang_masuk" data-field="x_id_brgmsk" data-hidden="1" name="x_id_brgmsk" id="x_id_brgmsk" value="<?= HtmlEncode($Page->id_brgmsk->CurrentValue) ?>">
</span>
</div></div>
    </div>
<?php } ?>
<?php if ($Page->no_order->Visible) { // no_order ?>
    <div id="r_no_order"<?= $Page->no_order->rowAttributes() ?>>
        <label id="elh_barang_masuk_no_order" for="x_no_order" class="<?= $Page->LeftColumnClass ?>"><?= $Page->no_order->caption() ?><?= $Page->no_order->Required ? $Language->phrase("FieldRequiredIndicator") : "" ?></label>
        <div class="<?= $Page->RightColumnClass ?>"><div<?= $Page->no_order->cellAttributes() ?>>
<span id="el_barang_masuk_no_order">
    <select
        id="x_no_order"
        name="x_no_order"
        class="form-select ew-select<?= $Page->no_order->isInvalidClass() ?>"
        <?php if (!$Page->no_order->IsNativeSelect) { ?>
        data-select2-id="fbarang_masukedit_x_no_order"
        <?php } ?>
        data-table="barang_masuk"
        data-field="x_no_order"
        data-value-separator="<?= $Page->no_order->displayValueSeparatorAttribute() ?>"
        data-placeholder="<?= HtmlEncode($Page->no_order->getPlaceHolder()) ?>"
        data-ew-action="autofill"
        <?= $Page->no_order->editAttributes() ?>>
        <?= $Page->no_order->selectOptionListHtml("x_no_order") ?>
    </select>
    <?= $Page->no_order->getCustomMessage() ?>
    <div class="invalid-feedback"><?= $Page->no_order->getErrorMessage() ?></div>
<?= $Page->no_order->Lookup->getParamTag($Page, "p_x_no_order") ?>
<?php if (!$Page->no_order->IsNativeSelect) { ?>
<script>
loadjs.ready("fbarang_masukedit", function() {
    var options = { name: "x_no_order", selectId: "fbarang_masukedit_x_no_order" },
        el = document.querySelector("select[data-select2-id='" + options.selectId + "']");
    if (!el)
        return;
    options.closeOnSelect = !options.multiple;
    options.dropdownParent = el.closest("#ew-modal-dialog, #ew-add-opt-dialog");
    if (fbarang_masukedit.lists.no_order?.lookupOptions.length) {
        options.data = { id: "x_no_order", form: "fbarang_masukedit" };
    } else {
        options.ajax = { id: "x_no_order", form: "fbarang_masukedit", limit: ew.LOOKUP_PAGE_SIZE };
    }
    options.minimumResultsForSearch = Infinity;
    options = Object.assign({}, ew.selectOptions, options, ew.vars.tables.barang_masuk.fields.no_order.selectOptions);
    ew.createSelect(options);
});
</script>
<?php } ?>
</span>
</div></div>
    </div>
<?php } ?>
<?php if ($Page->kode_barang->Visible) { // kode_barang ?>
    <div id="r_kode_barang"<?= $Page->kode_barang->rowAttributes() ?>>
        <label id="elh_barang_masuk_kode_barang" for="x_kode_barang" class="<?= $Page->LeftColumnClass ?>"><?= $Page->kode_barang->caption() ?><?= $Page->kode_barang->Required ? $Language->phrase("FieldRequiredIndicator") : "" ?></label>
        <div class="<?= $Page->RightColumnClass ?>"><div<?= $Page->kode_barang->cellAttributes() ?>>
<span id="el_barang_masuk_kode_barang">
    <select
        id="x_kode_barang"
        name="x_kode_barang"
        class="form-select ew-select<?= $Page->kode_barang->isInvalidClass() ?>"
        <?php if (!$Page->kode_barang->IsNativeSelect) { ?>
        data-select2-id="fbarang_masukedit_x_kode_barang"
        <?php } ?>
        data-table="barang_masuk"
        data-field="x_kode_barang"
        data-value-separator="<?= $Page->kode_barang->displayValueSeparatorAttribute() ?>"
        data-placeholder="<?= HtmlEncode($Page->kode_barang->getPlaceHolder()) ?>"
        data-ew-action="autofill"
        <?= $Page->kode_barang->editAttributes() ?>>
        <?= $Page->kode_barang->selectOptionListHtml("x_kode_barang") ?>
    </select>
    <?= $Page->kode_barang->getCustomMessage() ?>
    <div class="invalid-feedback"><?= $Page->kode_barang->getErrorMessage() ?></div>
<?= $Page->kode_barang->Lookup->getParamTag($Page, "p_x_kode_barang") ?>
<?php if (!$Page->kode_barang->IsNativeSelect) { ?>
<script>
loadjs.ready("fbarang_masukedit", function() {
    var options = { name: "x_kode_barang", selectId: "fbarang_masukedit_x_kode_barang" },
        el = document.querySelector("select[data-select2-id='" + options.selectId + "']");
    if (!el)
        return;
    options.closeOnSelect = !options.multiple;
    options.dropdownParent = el.closest("#ew-modal-dialog, #ew-add-opt-dialog");
    if (fbarang_masukedit.lists.kode_barang?.lookupOptions.length) {
        options.data = { id: "x_kode_barang", form: "fbarang_masukedit" };
    } else {
        options.ajax = { id: "x_kode_barang", form: "fbarang_masukedit", limit: ew.LOOKUP_PAGE_SIZE };
    }
    options.minimumResultsForSearch = Infinity;
    options = Object.assign({}, ew.selectOptions, options, ew.vars.tables.barang_masuk.fields.kode_barang.selectOptions);
    ew.createSelect(options);
});
</script>
<?php } ?>
</span>
</div></div>
    </div>
<?php } ?>
<?php if ($Page->nama_barang->Visible) { // nama_barang ?>
    <div id="r_nama_barang"<?= $Page->nama_barang->rowAttributes() ?>>
        <label id="elh_barang_masuk_nama_barang" for="x_nama_barang" class="<?= $Page->LeftColumnClass ?>"><?= $Page->nama_barang->caption() ?><?= $Page->nama_barang->Required ? $Language->phrase("FieldRequiredIndicator") : "" ?></label>
        <div class="<?= $Page->RightColumnClass ?>"><div<?= $Page->nama_barang->cellAttributes() ?>>
<span id="el_barang_masuk_nama_barang">
<span<?= $Page->nama_barang->viewAttributes() ?>>
<input type="text" readonly class="form-control-plaintext" value="<?= HtmlEncode(RemoveHtml($Page->nama_barang->getDisplayValue($Page->nama_barang->EditValue))) ?>"></span>
<input type="hidden" data-table="barang_masuk" data-field="x_nama_barang" data-hidden="1" name="x_nama_barang" id="x_nama_barang" value="<?= HtmlEncode($Page->nama_barang->CurrentValue) ?>">
</span>
</div></div>
    </div>
<?php } ?>
<?php if ($Page->jumlah_stok->Visible) { // jumlah_stok ?>
    <div id="r_jumlah_stok"<?= $Page->jumlah_stok->rowAttributes() ?>>
        <label id="elh_barang_masuk_jumlah_stok" for="x_jumlah_stok" class="<?= $Page->LeftColumnClass ?>"><?= $Page->jumlah_stok->caption() ?><?= $Page->jumlah_stok->Required ? $Language->phrase("FieldRequiredIndicator") : "" ?></label>
        <div class="<?= $Page->RightColumnClass ?>"><div<?= $Page->jumlah_stok->cellAttributes() ?>>
<span id="el_barang_masuk_jumlah_stok">
<input type="<?= $Page->jumlah_stok->getInputTextType() ?>" name="x_jumlah_stok" id="x_jumlah_stok" data-table="barang_masuk" data-field="x_jumlah_stok" value="<?= $Page->jumlah_stok->EditValue ?>" size="30" placeholder="<?= HtmlEncode($Page->jumlah_stok->getPlaceHolder()) ?>" data-format-pattern="<?= HtmlEncode($Page->jumlah_stok->formatPattern()) ?>"<?= $Page->jumlah_stok->editAttributes() ?> aria-describedby="x_jumlah_stok_help">
<?= $Page->jumlah_stok->getCustomMessage() ?>
<div class="invalid-feedback"><?= $Page->jumlah_stok->getErrorMessage() ?></div>
</span>
</div></div>
    </div>
<?php } ?>
<?php if ($Page->tgl_terima->Visible) { // tgl_terima ?>
    <div id="r_tgl_terima"<?= $Page->tgl_terima->rowAttributes() ?>>
        <label id="elh_barang_masuk_tgl_terima" for="x_tgl_terima" class="<?= $Page->LeftColumnClass ?>"><?= $Page->tgl_terima->caption() ?><?= $Page->tgl_terima->Required ? $Language->phrase("FieldRequiredIndicator") : "" ?></label>
        <div class="<?= $Page->RightColumnClass ?>"><div<?= $Page->tgl_terima->cellAttributes() ?>>
<span id="el_barang_masuk_tgl_terima">
<input type="<?= $Page->tgl_terima->getInputTextType() ?>" name="x_tgl_terima" id="x_tgl_terima" data-table="barang_masuk" data-field="x_tgl_terima" value="<?= $Page->tgl_terima->EditValue ?>" placeholder="<?= HtmlEncode($Page->tgl_terima->getPlaceHolder()) ?>" data-format-pattern="<?= HtmlEncode($Page->tgl_terima->formatPattern()) ?>"<?= $Page->tgl_terima->editAttributes() ?> aria-describedby="x_tgl_terima_help">
<?= $Page->tgl_terima->getCustomMessage() ?>
<div class="invalid-feedback"><?= $Page->tgl_terima->getErrorMessage() ?></div>
<?php if (!$Page->tgl_terima->ReadOnly && !$Page->tgl_terima->Disabled && !isset($Page->tgl_terima->EditAttrs["readonly"]) && !isset($Page->tgl_terima->EditAttrs["disabled"])) { ?>
<script>
loadjs.ready(["fbarang_masukedit", "datetimepicker"], function () {
    let format = "<?= DateFormat(14) ?>",
        options = {
            localization: {
                locale: ew.LANGUAGE_ID + "-u-nu-" + ew.getNumberingSystem(),
                hourCycle: format.match(/H/) ? "h24" : "h12",
                format,
                ...ew.language.phrase("datetimepicker")
            },
            display: {
                icons: {
                    previous: ew.IS_RTL ? "fa-solid fa-chevron-right" : "fa-solid fa-chevron-left",
                    next: ew.IS_RTL ? "fa-solid fa-chevron-left" : "fa-solid fa-chevron-right"
                },
                components: {
                    hours: !!format.match(/h/i),
                    minutes: !!format.match(/m/),
                    seconds: !!format.match(/s/i)
                },
                theme: ew.isDark() ? "dark" : "auto"
            }
        };
    ew.createDateTimePicker("fbarang_masukedit", "x_tgl_terima", ew.deepAssign({"useCurrent":false,"display":{"sideBySide":false}}, options));
});
</script>
<?php } ?>
</span>
</div></div>
    </div>
<?php } ?>
<?php if ($Page->keterangan->Visible) { // keterangan ?>
    <div id="r_keterangan"<?= $Page->keterangan->rowAttributes() ?>>
        <label id="elh_barang_masuk_keterangan" for="x_keterangan" class="<?= $Page->LeftColumnClass ?>"><?= $Page->keterangan->caption() ?><?= $Page->keterangan->Required ? $Language->phrase("FieldRequiredIndicator") : "" ?></label>
        <div class="<?= $Page->RightColumnClass ?>"><div<?= $Page->keterangan->cellAttributes() ?>>
<span id="el_barang_masuk_keterangan">
<input type="<?= $Page->keterangan->getInputTextType() ?>" name="x_keterangan" id="x_keterangan" data-table="barang_masuk" data-field="x_keterangan" value="<?= $Page->keterangan->EditValue ?>" size="30" maxlength="50" placeholder="<?= HtmlEncode($Page->keterangan->getPlaceHolder()) ?>" data-format-pattern="<?= HtmlEncode($Page->keterangan->formatPattern()) ?>"<?= $Page->keterangan->editAttributes() ?> aria-describedby="x_keterangan_help">
<?= $Page->keterangan->getCustomMessage() ?>
<div class="invalid-feedback"><?= $Page->keterangan->getErrorMessage() ?></div>
</span>
</div></div>
    </div>
<?php } ?>
</div><!-- /page* -->
<?= $Page->IsModal ? '<template class="ew-modal-buttons">' : '<div class="row ew-buttons">' ?><!-- buttons .row -->
    <div class="<?= $Page->OffsetColumnClass ?>"><!-- buttons offset -->
<button class="btn btn-primary ew-btn" name="btn-action" id="btn-action" type="submit" form="fbarang_masukedit"><?= $Language->phrase("SaveBtn") ?></button>
<?php if (IsJsonResponse()) { ?>
<button class="btn btn-default ew-btn" name="btn-cancel" id="btn-cancel" type="button" data-bs-dismiss="modal"><?= $Language->phrase("CancelBtn") ?></button>
<?php } else { ?>
<button class="btn btn-default ew-btn" name="btn-cancel" id="btn-cancel" type="button" form="fbarang_masukedit" data-href="<?= HtmlEncode(GetUrl($Page->getReturnUrl())) ?>"><?= $Language->phrase("CancelBtn") ?></button>
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
    ew.addEventHandlers("barang_masuk");
});
</script>
<script>
loadjs.ready("load", function () {
    // Write your table-specific startup script here, no need to add script tags.
});
</script>
