document.addEventListener("DOMContentLoaded", function () {
  // Inisialisasi status awal
  let isDarkMode = true;

  // Fungsi dark mode
  function darkmode() {
    var ganti = document.body;
    ganti.style.backgroundColor = "black";
  }

  // Fungsi light mode
  function lightmode() {
    var ganti = document.body;
    ganti.style.backgroundColor = "white";
  }

  // Fungsi untuk menangani klik tombol
  function handleToggle() {
    if (isDarkMode) {
      darkmode();
    } else {
      lightmode();
    }

    // Toggle status untuk mode berikutnya
    isDarkMode = !isDarkMode;
  }

  // Tambahkan event listener ke tombol
  const toggleButton = document.getElementsByClassName("toggleButton")[0];
  toggleButton.addEventListener("click", handleToggle);
});
