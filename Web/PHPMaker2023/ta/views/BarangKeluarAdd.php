<?php

namespace PHPMaker2023\ta;

// Page object
$BarangKeluarAdd = &$Page;
?>
<script>
var currentTable = <?= JsonEncode($Page->toClientVar()) ?>;
ew.deepAssign(ew.vars, { tables: { barang_keluar: currentTable } });
var currentPageID = ew.PAGE_ID = "add";
var currentForm;
var fbarang_keluaradd;
loadjs.ready(["wrapper", "head"], function () {
    let $ = jQuery;
    let fields = currentTable.fields;

    // Form object
    let form = new ew.FormBuilder()
        .setId("fbarang_keluaradd")
        .setPageId("add")

        // Add fields
        .setFields([
            ["kode_barang", [fields.kode_barang.visible && fields.kode_barang.required ? ew.Validators.required(fields.kode_barang.caption) : null], fields.kode_barang.isInvalid],
            ["nama_barang", [fields.nama_barang.visible && fields.nama_barang.required ? ew.Validators.required(fields.nama_barang.caption) : null], fields.nama_barang.isInvalid],
            ["jumlah_stok", [fields.jumlah_stok.visible && fields.jumlah_stok.required ? ew.Validators.required(fields.jumlah_stok.caption) : null, ew.Validators.integer], fields.jumlah_stok.isInvalid],
            ["tgl_keluar", [fields.tgl_keluar.visible && fields.tgl_keluar.required ? ew.Validators.required(fields.tgl_keluar.caption) : null, ew.Validators.datetime(fields.tgl_keluar.clientFormatPattern)], fields.tgl_keluar.isInvalid],
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
<?php $Page->showPageHeader(); ?>
<?php
$Page->showMessage();
?>
<form name="fbarang_keluaradd" id="fbarang_keluaradd" class="<?= $Page->FormClassName ?>" action="<?= CurrentPageUrl(false) ?>" method="post" novalidate autocomplete="off">
<?php if (Config("CHECK_TOKEN")) { ?>
<input type="hidden" name="<?= $TokenNameKey ?>" value="<?= $TokenName ?>"><!-- CSRF token name -->
<input type="hidden" name="<?= $TokenValueKey ?>" value="<?= $TokenValue ?>"><!-- CSRF token value -->
<?php } ?>
<input type="hidden" name="t" value="barang_keluar">
<input type="hidden" name="action" id="action" value="insert">
<input type="hidden" name="modal" value="<?= (int)$Page->IsModal ?>">
<?php if (IsJsonResponse()) { ?>
<input type="hidden" name="json" value="1">
<?php } ?>
<input type="hidden" name="<?= $Page->OldKeyName ?>" value="<?= $Page->OldKey ?>">
<div class="ew-add-div"><!-- page* -->
<?php if ($Page->kode_barang->Visible) { // kode_barang ?>
    <div id="r_kode_barang"<?= $Page->kode_barang->rowAttributes() ?>>
        <label id="elh_barang_keluar_kode_barang" for="x_kode_barang" class="<?= $Page->LeftColumnClass ?>"><?= $Page->kode_barang->caption() ?><?= $Page->kode_barang->Required ? $Language->phrase("FieldRequiredIndicator") : "" ?></label>
        <div class="<?= $Page->RightColumnClass ?>"><div<?= $Page->kode_barang->cellAttributes() ?>>
<span id="el_barang_keluar_kode_barang">
    <select
        id="x_kode_barang"
        name="x_kode_barang"
        class="form-select ew-select<?= $Page->kode_barang->isInvalidClass() ?>"
        <?php if (!$Page->kode_barang->IsNativeSelect) { ?>
        data-select2-id="fbarang_keluaradd_x_kode_barang"
        <?php } ?>
        data-table="barang_keluar"
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
loadjs.ready("fbarang_keluaradd", function() {
    var options = { name: "x_kode_barang", selectId: "fbarang_keluaradd_x_kode_barang" },
        el = document.querySelector("select[data-select2-id='" + options.selectId + "']");
    if (!el)
        return;
    options.closeOnSelect = !options.multiple;
    options.dropdownParent = el.closest("#ew-modal-dialog, #ew-add-opt-dialog");
    if (fbarang_keluaradd.lists.kode_barang?.lookupOptions.length) {
        options.data = { id: "x_kode_barang", form: "fbarang_keluaradd" };
    } else {
        options.ajax = { id: "x_kode_barang", form: "fbarang_keluaradd", limit: ew.LOOKUP_PAGE_SIZE };
    }
    options.minimumResultsForSearch = Infinity;
    options = Object.assign({}, ew.selectOptions, options, ew.vars.tables.barang_keluar.fields.kode_barang.selectOptions);
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
        <label id="elh_barang_keluar_nama_barang" for="x_nama_barang" class="<?= $Page->LeftColumnClass ?>"><?= $Page->nama_barang->caption() ?><?= $Page->nama_barang->Required ? $Language->phrase("FieldRequiredIndicator") : "" ?></label>
        <div class="<?= $Page->RightColumnClass ?>"><div<?= $Page->nama_barang->cellAttributes() ?>>
<span id="el_barang_keluar_nama_barang">
<input type="<?= $Page->nama_barang->getInputTextType() ?>" name="x_nama_barang" id="x_nama_barang" data-table="barang_keluar" data-field="x_nama_barang" value="<?= $Page->nama_barang->EditValue ?>" size="30" maxlength="50" placeholder="<?= HtmlEncode($Page->nama_barang->getPlaceHolder()) ?>" data-format-pattern="<?= HtmlEncode($Page->nama_barang->formatPattern()) ?>"<?= $Page->nama_barang->editAttributes() ?> aria-describedby="x_nama_barang_help">
<?= $Page->nama_barang->getCustomMessage() ?>
<div class="invalid-feedback"><?= $Page->nama_barang->getErrorMessage() ?></div>
</span>
</div></div>
    </div>
<?php } ?>
<?php if ($Page->jumlah_stok->Visible) { // jumlah_stok ?>
    <div id="r_jumlah_stok"<?= $Page->jumlah_stok->rowAttributes() ?>>
        <label id="elh_barang_keluar_jumlah_stok" for="x_jumlah_stok" class="<?= $Page->LeftColumnClass ?>"><?= $Page->jumlah_stok->caption() ?><?= $Page->jumlah_stok->Required ? $Language->phrase("FieldRequiredIndicator") : "" ?></label>
        <div class="<?= $Page->RightColumnClass ?>"><div<?= $Page->jumlah_stok->cellAttributes() ?>>
<span id="el_barang_keluar_jumlah_stok">
<input type="<?= $Page->jumlah_stok->getInputTextType() ?>" name="x_jumlah_stok" id="x_jumlah_stok" data-table="barang_keluar" data-field="x_jumlah_stok" value="<?= $Page->jumlah_stok->EditValue ?>" size="30" placeholder="<?= HtmlEncode($Page->jumlah_stok->getPlaceHolder()) ?>" data-format-pattern="<?= HtmlEncode($Page->jumlah_stok->formatPattern()) ?>"<?= $Page->jumlah_stok->editAttributes() ?> aria-describedby="x_jumlah_stok_help">
<?= $Page->jumlah_stok->getCustomMessage() ?>
<div class="invalid-feedback"><?= $Page->jumlah_stok->getErrorMessage() ?></div>
</span>
</div></div>
    </div>
<?php } ?>
<?php if ($Page->tgl_keluar->Visible) { // tgl_keluar ?>
    <div id="r_tgl_keluar"<?= $Page->tgl_keluar->rowAttributes() ?>>
        <label id="elh_barang_keluar_tgl_keluar" for="x_tgl_keluar" class="<?= $Page->LeftColumnClass ?>"><?= $Page->tgl_keluar->caption() ?><?= $Page->tgl_keluar->Required ? $Language->phrase("FieldRequiredIndicator") : "" ?></label>
        <div class="<?= $Page->RightColumnClass ?>"><div<?= $Page->tgl_keluar->cellAttributes() ?>>
<span id="el_barang_keluar_tgl_keluar">
<input type="<?= $Page->tgl_keluar->getInputTextType() ?>" name="x_tgl_keluar" id="x_tgl_keluar" data-table="barang_keluar" data-field="x_tgl_keluar" value="<?= $Page->tgl_keluar->EditValue ?>" placeholder="<?= HtmlEncode($Page->tgl_keluar->getPlaceHolder()) ?>" data-format-pattern="<?= HtmlEncode($Page->tgl_keluar->formatPattern()) ?>"<?= $Page->tgl_keluar->editAttributes() ?> aria-describedby="x_tgl_keluar_help">
<?= $Page->tgl_keluar->getCustomMessage() ?>
<div class="invalid-feedback"><?= $Page->tgl_keluar->getErrorMessage() ?></div>
<?php if (!$Page->tgl_keluar->ReadOnly && !$Page->tgl_keluar->Disabled && !isset($Page->tgl_keluar->EditAttrs["readonly"]) && !isset($Page->tgl_keluar->EditAttrs["disabled"])) { ?>
<script>
loadjs.ready(["fbarang_keluaradd", "datetimepicker"], function () {
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
    ew.createDateTimePicker("fbarang_keluaradd", "x_tgl_keluar", ew.deepAssign({"useCurrent":false,"display":{"sideBySide":false}}, options));
});
</script>
<?php } ?>
</span>
</div></div>
    </div>
<?php } ?>
<?php if ($Page->keterangan->Visible) { // keterangan ?>
    <div id="r_keterangan"<?= $Page->keterangan->rowAttributes() ?>>
        <label id="elh_barang_keluar_keterangan" for="x_keterangan" class="<?= $Page->LeftColumnClass ?>"><?= $Page->keterangan->caption() ?><?= $Page->keterangan->Required ? $Language->phrase("FieldRequiredIndicator") : "" ?></label>
        <div class="<?= $Page->RightColumnClass ?>"><div<?= $Page->keterangan->cellAttributes() ?>>
<span id="el_barang_keluar_keterangan">
<input type="<?= $Page->keterangan->getInputTextType() ?>" name="x_keterangan" id="x_keterangan" data-table="barang_keluar" data-field="x_keterangan" value="<?= $Page->keterangan->EditValue ?>" size="30" maxlength="50" placeholder="<?= HtmlEncode($Page->keterangan->getPlaceHolder()) ?>" data-format-pattern="<?= HtmlEncode($Page->keterangan->formatPattern()) ?>"<?= $Page->keterangan->editAttributes() ?> aria-describedby="x_keterangan_help">
<?= $Page->keterangan->getCustomMessage() ?>
<div class="invalid-feedback"><?= $Page->keterangan->getErrorMessage() ?></div>
</span>
</div></div>
    </div>
<?php } ?>
</div><!-- /page* -->
<?= $Page->IsModal ? '<template class="ew-modal-buttons">' : '<div class="row ew-buttons">' ?><!-- buttons .row -->
    <div class="<?= $Page->OffsetColumnClass ?>"><!-- buttons offset -->
<button class="btn btn-primary ew-btn" name="btn-action" id="btn-action" type="submit" form="fbarang_keluaradd"><?= $Language->phrase("AddBtn") ?></button>
<?php if (IsJsonResponse()) { ?>
<button class="btn btn-default ew-btn" name="btn-cancel" id="btn-cancel" type="button" data-bs-dismiss="modal"><?= $Language->phrase("CancelBtn") ?></button>
<?php } else { ?>
<button class="btn btn-default ew-btn" name="btn-cancel" id="btn-cancel" type="button" form="fbarang_keluaradd" data-href="<?= HtmlEncode(GetUrl($Page->getReturnUrl())) ?>"><?= $Language->phrase("CancelBtn") ?></button>
<?php } ?>
    </div><!-- /buttons offset -->
<?= $Page->IsModal ? "</template>" : "</div>" ?><!-- /buttons .row -->
</form>
<?php
$Page->showPageFooter();
echo GetDebugMessage();
?>
<script>
// Field event handlers
loadjs.ready("head", function() {
    ew.addEventHandlers("barang_keluar");
});
</script>
<script>
loadjs.ready("load", function () {
    // Write your table-specific startup script here, no need to add script tags.
});
</script>
