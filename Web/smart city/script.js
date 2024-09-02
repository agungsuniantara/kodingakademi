// scripts.js

// Contoh script untuk peta interaktif
document.addEventListener("DOMContentLoaded", function () {
  var mapContainer = document.getElementById("map-container");
  // Inisialisasi peta di sini (gunakan library peta seperti Leaflet atau Google Maps API)
  // Contoh dengan Leaflet.js
  var map = L.map(mapContainer).setView([-6.2, 106.816666], 13);
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: "Map data &copy; OpenStreetMap contributors",
  }).addTo(map);
  // Tambahkan marker untuk tempat wisata
  var marker = L.marker([-6.2, 106.816666])
    .addTo(map)
    .bindPopup("<b>Tempat Wisata</b><br>Deskripsi singkat tempat wisata.")
    .openPopup();
});

// Dark mode toggle
document
  .getElementById("dark-mode-toggle")
  .addEventListener("click", function () {
    document.body.classList.toggle("dark-mode");
  });
