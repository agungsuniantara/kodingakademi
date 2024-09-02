<?php

namespace PHPMaker2023\ta;

use Slim\App;
use Slim\Routing\RouteCollectorProxy;
use Slim\Exception\HttpNotFoundException;

// Handle Routes
return function (App $app) {
    // staf_gudang
    $app->map(["GET", "POST", "OPTIONS"], '/StafGudangList[/{id_staf}]', StafGudangController::class . ':list')->add(PermissionMiddleware::class)->setName('StafGudangList-staf_gudang-list'); // list
    $app->map(["GET", "POST", "OPTIONS"], '/StafGudangAdd[/{id_staf}]', StafGudangController::class . ':add')->add(PermissionMiddleware::class)->setName('StafGudangAdd-staf_gudang-add'); // add
    $app->map(["GET", "POST", "OPTIONS"], '/StafGudangEdit[/{id_staf}]', StafGudangController::class . ':edit')->add(PermissionMiddleware::class)->setName('StafGudangEdit-staf_gudang-edit'); // edit
    $app->map(["GET", "POST", "OPTIONS"], '/StafGudangDelete[/{id_staf}]', StafGudangController::class . ':delete')->add(PermissionMiddleware::class)->setName('StafGudangDelete-staf_gudang-delete'); // delete
    $app->group(
        '/staf_gudang',
        function (RouteCollectorProxy $group) {
            $group->map(["GET", "POST", "OPTIONS"], '/' . Config('LIST_ACTION') . '[/{id_staf}]', StafGudangController::class . ':list')->add(PermissionMiddleware::class)->setName('staf_gudang/list-staf_gudang-list-2'); // list
            $group->map(["GET", "POST", "OPTIONS"], '/' . Config('ADD_ACTION') . '[/{id_staf}]', StafGudangController::class . ':add')->add(PermissionMiddleware::class)->setName('staf_gudang/add-staf_gudang-add-2'); // add
            $group->map(["GET", "POST", "OPTIONS"], '/' . Config('EDIT_ACTION') . '[/{id_staf}]', StafGudangController::class . ':edit')->add(PermissionMiddleware::class)->setName('staf_gudang/edit-staf_gudang-edit-2'); // edit
            $group->map(["GET", "POST", "OPTIONS"], '/' . Config('DELETE_ACTION') . '[/{id_staf}]', StafGudangController::class . ':delete')->add(PermissionMiddleware::class)->setName('staf_gudang/delete-staf_gudang-delete-2'); // delete
        }
    );

    // stok_barang
    $app->map(["GET", "POST", "OPTIONS"], '/StokBarangList[/{id_barang}]', StokBarangController::class . ':list')->add(PermissionMiddleware::class)->setName('StokBarangList-stok_barang-list'); // list
    $app->map(["GET", "POST", "OPTIONS"], '/StokBarangAdd[/{id_barang}]', StokBarangController::class . ':add')->add(PermissionMiddleware::class)->setName('StokBarangAdd-stok_barang-add'); // add
    $app->map(["GET", "POST", "OPTIONS"], '/StokBarangEdit[/{id_barang}]', StokBarangController::class . ':edit')->add(PermissionMiddleware::class)->setName('StokBarangEdit-stok_barang-edit'); // edit
    $app->map(["GET", "POST", "OPTIONS"], '/StokBarangDelete[/{id_barang}]', StokBarangController::class . ':delete')->add(PermissionMiddleware::class)->setName('StokBarangDelete-stok_barang-delete'); // delete
    $app->group(
        '/stok_barang',
        function (RouteCollectorProxy $group) {
            $group->map(["GET", "POST", "OPTIONS"], '/' . Config('LIST_ACTION') . '[/{id_barang}]', StokBarangController::class . ':list')->add(PermissionMiddleware::class)->setName('stok_barang/list-stok_barang-list-2'); // list
            $group->map(["GET", "POST", "OPTIONS"], '/' . Config('ADD_ACTION') . '[/{id_barang}]', StokBarangController::class . ':add')->add(PermissionMiddleware::class)->setName('stok_barang/add-stok_barang-add-2'); // add
            $group->map(["GET", "POST", "OPTIONS"], '/' . Config('EDIT_ACTION') . '[/{id_barang}]', StokBarangController::class . ':edit')->add(PermissionMiddleware::class)->setName('stok_barang/edit-stok_barang-edit-2'); // edit
            $group->map(["GET", "POST", "OPTIONS"], '/' . Config('DELETE_ACTION') . '[/{id_barang}]', StokBarangController::class . ':delete')->add(PermissionMiddleware::class)->setName('stok_barang/delete-stok_barang-delete-2'); // delete
        }
    );

    // barang_masuk
    $app->map(["GET", "POST", "OPTIONS"], '/BarangMasukList[/{id_brgmsk}]', BarangMasukController::class . ':list')->add(PermissionMiddleware::class)->setName('BarangMasukList-barang_masuk-list'); // list
    $app->map(["GET", "POST", "OPTIONS"], '/BarangMasukAdd[/{id_brgmsk}]', BarangMasukController::class . ':add')->add(PermissionMiddleware::class)->setName('BarangMasukAdd-barang_masuk-add'); // add
    $app->map(["GET", "POST", "OPTIONS"], '/BarangMasukEdit[/{id_brgmsk}]', BarangMasukController::class . ':edit')->add(PermissionMiddleware::class)->setName('BarangMasukEdit-barang_masuk-edit'); // edit
    $app->map(["GET", "POST", "OPTIONS"], '/BarangMasukDelete[/{id_brgmsk}]', BarangMasukController::class . ':delete')->add(PermissionMiddleware::class)->setName('BarangMasukDelete-barang_masuk-delete'); // delete
    $app->group(
        '/barang_masuk',
        function (RouteCollectorProxy $group) {
            $group->map(["GET", "POST", "OPTIONS"], '/' . Config('LIST_ACTION') . '[/{id_brgmsk}]', BarangMasukController::class . ':list')->add(PermissionMiddleware::class)->setName('barang_masuk/list-barang_masuk-list-2'); // list
            $group->map(["GET", "POST", "OPTIONS"], '/' . Config('ADD_ACTION') . '[/{id_brgmsk}]', BarangMasukController::class . ':add')->add(PermissionMiddleware::class)->setName('barang_masuk/add-barang_masuk-add-2'); // add
            $group->map(["GET", "POST", "OPTIONS"], '/' . Config('EDIT_ACTION') . '[/{id_brgmsk}]', BarangMasukController::class . ':edit')->add(PermissionMiddleware::class)->setName('barang_masuk/edit-barang_masuk-edit-2'); // edit
            $group->map(["GET", "POST", "OPTIONS"], '/' . Config('DELETE_ACTION') . '[/{id_brgmsk}]', BarangMasukController::class . ':delete')->add(PermissionMiddleware::class)->setName('barang_masuk/delete-barang_masuk-delete-2'); // delete
        }
    );

    // barang_keluar
    $app->map(["GET", "POST", "OPTIONS"], '/BarangKeluarList[/{id_brgkel}]', BarangKeluarController::class . ':list')->add(PermissionMiddleware::class)->setName('BarangKeluarList-barang_keluar-list'); // list
    $app->map(["GET", "POST", "OPTIONS"], '/BarangKeluarAdd[/{id_brgkel}]', BarangKeluarController::class . ':add')->add(PermissionMiddleware::class)->setName('BarangKeluarAdd-barang_keluar-add'); // add
    $app->map(["GET", "POST", "OPTIONS"], '/BarangKeluarEdit[/{id_brgkel}]', BarangKeluarController::class . ':edit')->add(PermissionMiddleware::class)->setName('BarangKeluarEdit-barang_keluar-edit'); // edit
    $app->map(["GET", "POST", "OPTIONS"], '/BarangKeluarDelete[/{id_brgkel}]', BarangKeluarController::class . ':delete')->add(PermissionMiddleware::class)->setName('BarangKeluarDelete-barang_keluar-delete'); // delete
    $app->group(
        '/barang_keluar',
        function (RouteCollectorProxy $group) {
            $group->map(["GET", "POST", "OPTIONS"], '/' . Config('LIST_ACTION') . '[/{id_brgkel}]', BarangKeluarController::class . ':list')->add(PermissionMiddleware::class)->setName('barang_keluar/list-barang_keluar-list-2'); // list
            $group->map(["GET", "POST", "OPTIONS"], '/' . Config('ADD_ACTION') . '[/{id_brgkel}]', BarangKeluarController::class . ':add')->add(PermissionMiddleware::class)->setName('barang_keluar/add-barang_keluar-add-2'); // add
            $group->map(["GET", "POST", "OPTIONS"], '/' . Config('EDIT_ACTION') . '[/{id_brgkel}]', BarangKeluarController::class . ':edit')->add(PermissionMiddleware::class)->setName('barang_keluar/edit-barang_keluar-edit-2'); // edit
            $group->map(["GET", "POST", "OPTIONS"], '/' . Config('DELETE_ACTION') . '[/{id_brgkel}]', BarangKeluarController::class . ':delete')->add(PermissionMiddleware::class)->setName('barang_keluar/delete-barang_keluar-delete-2'); // delete
        }
    );

    // order_barang
    $app->map(["GET", "POST", "OPTIONS"], '/OrderBarangList[/{id_receipt}]', OrderBarangController::class . ':list')->add(PermissionMiddleware::class)->setName('OrderBarangList-order_barang-list'); // list
    $app->map(["GET", "POST", "OPTIONS"], '/OrderBarangAdd[/{id_receipt}]', OrderBarangController::class . ':add')->add(PermissionMiddleware::class)->setName('OrderBarangAdd-order_barang-add'); // add
    $app->map(["GET", "POST", "OPTIONS"], '/OrderBarangEdit[/{id_receipt}]', OrderBarangController::class . ':edit')->add(PermissionMiddleware::class)->setName('OrderBarangEdit-order_barang-edit'); // edit
    $app->map(["GET", "POST", "OPTIONS"], '/OrderBarangDelete[/{id_receipt}]', OrderBarangController::class . ':delete')->add(PermissionMiddleware::class)->setName('OrderBarangDelete-order_barang-delete'); // delete
    $app->group(
        '/order_barang',
        function (RouteCollectorProxy $group) {
            $group->map(["GET", "POST", "OPTIONS"], '/' . Config('LIST_ACTION') . '[/{id_receipt}]', OrderBarangController::class . ':list')->add(PermissionMiddleware::class)->setName('order_barang/list-order_barang-list-2'); // list
            $group->map(["GET", "POST", "OPTIONS"], '/' . Config('ADD_ACTION') . '[/{id_receipt}]', OrderBarangController::class . ':add')->add(PermissionMiddleware::class)->setName('order_barang/add-order_barang-add-2'); // add
            $group->map(["GET", "POST", "OPTIONS"], '/' . Config('EDIT_ACTION') . '[/{id_receipt}]', OrderBarangController::class . ':edit')->add(PermissionMiddleware::class)->setName('order_barang/edit-order_barang-edit-2'); // edit
            $group->map(["GET", "POST", "OPTIONS"], '/' . Config('DELETE_ACTION') . '[/{id_receipt}]', OrderBarangController::class . ':delete')->add(PermissionMiddleware::class)->setName('order_barang/delete-order_barang-delete-2'); // delete
        }
    );

    // personal_data
    $app->map(["GET", "POST", "OPTIONS"], '/personaldata', OthersController::class . ':personaldata')->add(PermissionMiddleware::class)->setName('personaldata');

    // login
    $app->map(["GET", "POST", "OPTIONS"], '/login[/{provider}]', OthersController::class . ':login')->add(PermissionMiddleware::class)->setName('login');

    // logout
    $app->map(["GET", "POST", "OPTIONS"], '/logout', OthersController::class . ':logout')->add(PermissionMiddleware::class)->setName('logout');

    // Swagger
    $app->get('/' . Config("SWAGGER_ACTION"), OthersController::class . ':swagger')->setName(Config("SWAGGER_ACTION")); // Swagger

    // Index
    $app->get('/index.php', OthersController::class . ':index')->add(PermissionMiddleware::class)->setName('index');

    // Route Action event
    if (function_exists(PROJECT_NAMESPACE . "Route_Action")) {
        if (Route_Action($app) === false) {
            return;
        }
    }

    /**
     * Catch-all route to serve a 404 Not Found page if none of the routes match
     * NOTE: Make sure this route is defined last.
     */
    $app->map(
        ['GET', 'POST', 'PUT', 'DELETE', 'PATCH'],
        '/{routes:.+}',
        function ($request, $response, $params) {
            throw new HttpNotFoundException($request, str_replace("%p", $params["routes"], Container("language")->phrase("PageNotFound")));
        }
    );
};
