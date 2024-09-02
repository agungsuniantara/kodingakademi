$(document).ready(function () {
  $("#myDataTable").DataTable({
    ajax: "proses.php",
    columns: [
      { data: "name" },
      { data: "email" },
      { data: "number" },
      { data: "phone" },
      {
        data: "file",
        render: function (data) {
          return (
            "<img class='image' src='" +
            data +
            "' style='width:100px; height:100px'>"
          );
        },
      },
      { data: "password" },
      {
        data: "id",
        render: function (data) {
          return (
            "<div style = 'display: flex; gap: 5px;'><button onclick='deleteData(" +
            data +
            ")' style='background-color: red; color: white;'>Delete</button>" +
            "<button onclick='editData(" +
            data +
            ")' style='background-color: green; color: white;'>Edit</button> </div>"
          );
        },
      },
    ],
    autoWidth: false,
    responsive: true,
  });

  // Tambahkan tombol di bawah kolom pencarian
  var button = $("<div class='custom-buttons'></div>").insertAfter(
    ".dataTables_wrapper .dataTables_filter input"
  );

  // Tambahkan tombol di sini
  button.append(
    "<button class='btn btn-primary' onclick='tambahData()' style='background-color: blue; color: white;'>Tambah</button>"
  );

  // Gaya CSS tambahan (opsional)
  button.css({
    "margin-top": "20px",
  });
});

function deleteData(id) {
  var confirmation = confirm("apakah ingin hapus data ?");

  if (confirmation) {
    $.ajax({
      type: "POST",
      url: "proses.php",
      data: {
        action: "delete",
        id: id,
      },
      dataType: "json",
      success: function () {
        alert("berhasil hapus data");
        // Reload the DataTable after deleting data
        $("#myDataTable").DataTable().ajax.reload();
      },
      error: function () {
        alert("gagal hapus data");
      },
    });
  }
}

function editData(id) {
  var confirmation = confirm("apakah ingin edit data ?");

  if (confirmation) {
    $.ajax({
      type: "POST",
      url: "proses.php",
      data: {
        action: "fetch",
        id: id,
      },
      dataType: "json",
      success: function (tampil) {
        var formHtml = `
        <div id="tampil">
          <form id="editDataForm" enctype="multipart/form-data">
            <input type="text" id="id" name="id" value="${tampil["id"]}" hidden>
            <input type="text" id="name" name="name" value="${tampil["name"]}" required>
            <input type="email" id="email" name="email" value="${tampil["email"]}" required>
            <input type="text" id="number" name="number" value="${tampil["number"]}" required>
            <input type="text" id="phone" name="phone" value="${tampil["phone"]}" required>
            <label>Gambar : </label>
            <img src='${tampil["file"]}' style='width:100px; height:100px'></img>
            <input type="file" id="file" name="file" required>
            <input type="password" id="password" name="password" value="${tampil["password"]}" required>

            <button type="submit" style="background-color: red; color: white;">Edit Data</button>
            <a href="index.php">Back</a>
          </form>
        </div>`;

        // Append the form HTML to the body
        $("body").append(formHtml);

        // Handle form submission
        $("#editDataForm").submit(function (event) {
          event.preventDefault();

          // Create a FormData object and append form data
          var formData = new FormData(this);

          // Append the action to the form data
          formData.append("action", "edit");
          formData.append("id", id);

          // Submit the form using AJAX
          $.ajax({
            type: "POST",
            enctype: "multipart/form-data",
            url: "proses.php",
            data: formData,
            contentType: false,
            processData: false,
            cache: false,
            success: function () {
              alert("berhasil edit data");

              // Reload the DataTable after editing data
              $("#myDataTable").DataTable().ajax.reload();

              // Remove the form after success
              $("#tampil").remove();
            },
            error: function () {
              alert("gagal edit data");
            },
          });
        });
      },
    });
  }
}

function tambahData() {
  // Create a form for adding new data
  var formHtml = `
    <div id="tampil">
      <form id="addDataForm" enctype="multipart/form-data">
        <input type="text" id="name" name="name" placeholder="Masukkan nama" required>
        <input type="email" id="email" name="email" placeholder="Masukkan email" required>
        <input type="text" id="number" name="number" placeholder="Masukkan number" required>
        <input type="text" id="phone" name="phone" placeholder="Masukkan phone" required>
        <input type="file" id="file" name="file" required>
        <input type="password" id="password" name="password" placeholder="Masukkan password" required>
        <button type="submit" style="background-color: red; color: white;">Add Data</button>
        <a href="index.php">Back</a>
      </form>
    </div>
  `;

  // Append the form HTML to the body
  $("body").append(formHtml);

  // Handle form submission
  $("#addDataForm").submit(function (event) {
    event.preventDefault();

    // Create a FormData object
    var formData = new FormData(this);

    // Append the action to the form data
    formData.append("action", "tambah");

    // Submit the form using AJAX
    $.ajax({
      type: "POST",
      enctype: "multipart/form-data",
      url: "proses.php",
      data: formData, // Use FormData directly
      contentType: false,
      processData: false,
      cache: false,
      success: function () {
        alert("berhasil tambah data");
        // Reload the DataTable after adding new data
        $("#myDataTable").DataTable().ajax.reload();

        // Remove the form after success
        $("#tampil").remove();
      },
      error: function () {
        alert("gagal tambah data");
      },
    });
  });
}
