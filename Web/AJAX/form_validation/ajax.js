$(document).ready(function () {
  $("#myForm").submit(function (event) {
    event.preventDefault();

    var name = $("#name").val().trim();
    var email = $("#email").val().trim();
    var number = $("#number").val().trim();
    var phone = $("#phone").val().trim();
    var file = $("#file").val().trim();
    var password = $("#password").val().trim();
    var confirm = $("#confirm").val().trim();

    if (
      name === "" ||
      email === "" ||
      number === "" ||
      phone === "" ||
      password === "" ||
      confirm === "" ||
      file === ""
    ) {
      alert("data harus lengkap terisi");
    } else {
      var form = $("#myForm")[0];
      var data = new FormData(form);

      $.ajax({
        type: "POST",
        enctype: "multipart/form-data",
        url: "proses.php",
        data: data,
        processData: false,
        contentType: false,
        cache: false,
        success: function (response) {
          alert(response);
        },
        error: function (response) {
          alert(response);
        },
      });
    }
  });
});
