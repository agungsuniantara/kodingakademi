document.addEventListener("DOMContentLoaded", function () {
  let isDarkMode = true;

  function darkmode() {
    var change1 = document.getElementsByClassName("navbar");
    change1[0].style.backgroundColor = "#910A67";
    var change2 = document.getElementsByClassName("dropdown");
    change2[0].style.backgroundColor = "#910A67";

    var change3 = document.getElementsByClassName("main");
    change3[0].style.backgroundColor = "#030637";
    var change4 = document.getElementsByClassName("mainjs");
    change4[0].style.backgroundColor = "#910A67";
    change4[1].style.backgroundColor = "#030637";
    var change5 = document.getElementsByClassName("exploreus");
    change5[0].style.backgroundColor = "#720455";

    var change6 = document.getElementsByClassName("whatweserve");
    change6[0].style.backgroundColor = "#910A67";
    change6[1].style.backgroundColor = "#910A67";

    var change7 = document.getElementsByClassName("table");
    change7[0].style.backgroundColor = "#910A67";
    change7[1].style.backgroundColor = "#910A67";
    change7[2].style.backgroundColor = "#720455";
    change7[3].style.backgroundColor = "#720455";
    change7[4].style.backgroundColor = "#c05299";
    change7[5].style.backgroundColor = "#c05299";
    change7[6].style.backgroundColor = "#c05299";
    change7[7].style.backgroundColor = "#c05299";

    var change8 = document.getElementsByClassName("quantity");
    change8[0].style.backgroundColor = "#c05299";
    change8[1].style.backgroundColor = "#c05299";
    change8[2].style.backgroundColor = "#c05299";
    change8[3].style.backgroundColor = "#c05299";

    var change8 = document.getElementsByClassName("confirm");
    change8[0].style.backgroundColor = "#910A67";
    change8[1].style.backgroundColor = "#910A67";
    change8[2].style.backgroundColor = "#910A67";
    change8[3].style.backgroundColor = "#910A67";

    var change9 = document.getElementsByClassName("footer");
    change9[0].style.backgroundColor = "#030637";
    change9[1].style.backgroundColor = "#030637";
    change9[2].style.backgroundColor = "#030637";
    change9[3].style.backgroundColor = "#030637";
    change9[4].style.backgroundColor = "#030637";
    change9[5].style.backgroundColor = "#030637";
    change9[6].style.backgroundColor = "#030637";
    change9[7].style.backgroundColor = "#030637";
    change9[8].style.backgroundColor = "#030637";
    change9[9].style.backgroundColor = "#030637";
    change9[10].style.backgroundColor = "#030637";
    change9[11].style.backgroundColor = "#030637";
    change9[12].style.backgroundColor = "#030637";

    var change9 = document.getElementsByClassName("contact");
    change9[0].style.backgroundColor = "#910A67";
    change9[1].style.backgroundColor = "#910A67";
    change9[2].style.backgroundColor = "#910A67";

    // updateButtonImage("lightmode.png");
    updateButtonText("Light Mode");
  }

  function lightmode() {
    var change1 = document.getElementsByClassName("navbar");
    change1[0].style.backgroundColor = "#ff6289";
    var change2 = document.getElementsByClassName("dropdown");
    change2[0].style.backgroundColor = "#ff6289";

    var change3 = document.getElementsByClassName("main");
    change3[0].style.backgroundColor = "#ffc2cd";
    var change4 = document.getElementsByClassName("mainjs");
    change4[0].style.backgroundColor = "#ff6289";
    change4[1].style.backgroundColor = "#ffc2cd";
    var change5 = document.getElementsByClassName("exploreus");
    change5[0].style.backgroundColor = "#ff084a";

    var change6 = document.getElementsByClassName("whatweserve");
    change6[0].style.backgroundColor = "#ff6289";
    change6[1].style.backgroundColor = "#ff6289";

    var change7 = document.getElementsByClassName("table");
    change7[0].style.backgroundColor = "#ff6289";
    change7[1].style.backgroundColor = "#ff6289";
    change7[2].style.backgroundColor = "#ff084a";
    change7[3].style.backgroundColor = "#ff084a";
    change7[4].style.backgroundColor = "#ff93ac";
    change7[5].style.backgroundColor = "#ff93ac";
    change7[6].style.backgroundColor = "#ff93ac";
    change7[7].style.backgroundColor = "#ff93ac";

    var change8 = document.getElementsByClassName("quantity");
    change8[0].style.backgroundColor = "#ff93ac";
    change8[1].style.backgroundColor = "#ff93ac";
    change8[2].style.backgroundColor = "#ff93ac";
    change8[3].style.backgroundColor = "#ff93ac";

    var change8 = document.getElementsByClassName("confirm");
    change8[0].style.backgroundColor = "#ff6289";
    change8[1].style.backgroundColor = "#ff6289";
    change8[2].style.backgroundColor = "#ff6289";
    change8[3].style.backgroundColor = "#ff6289";

    var change9 = document.getElementsByClassName("footer");
    change9[0].style.backgroundColor = "#ffc2cd";
    change9[1].style.backgroundColor = "#ffc2cd";
    change9[2].style.backgroundColor = "#ffc2cd";
    change9[3].style.backgroundColor = "#ffc2cd";
    change9[4].style.backgroundColor = "#ffc2cd";
    change9[5].style.backgroundColor = "#ffc2cd";
    change9[6].style.backgroundColor = "#ffc2cd";
    change9[7].style.backgroundColor = "#ffc2cd";
    change9[8].style.backgroundColor = "#ffc2cd";
    change9[9].style.backgroundColor = "#ffc2cd";
    change9[10].style.backgroundColor = "#ffc2cd";
    change9[11].style.backgroundColor = "#ffc2cd";
    change9[12].style.backgroundColor = "#ffc2cd";

    var change9 = document.getElementsByClassName("contact");
    change9[0].style.backgroundColor = "#ff6289";
    change9[1].style.backgroundColor = "#ff6289";
    change9[2].style.backgroundColor = "#ff6289";

    // updateButtonImage("darkmode.png");
    updateButtonText("Dark Mode");
  }

//   function updateButtonImage(imageSrc) {
//     const toggleButton = document.getElementsByClassName("toggleButton")[0];
//     toggleButton.innerHTML = ""; // Clear existing content
//     const imgElement = document.createElement("img");
//     imgElement.src = imageSrc;
//     toggleButton.appendChild(imgElement);
//   }

  function handletoggle() {
    if (isDarkMode) {
      darkmode();
    } else {
      lightmode();
    }

    isDarkMode = !isDarkMode;
  }

  function updateButtonText(text) {
    const toggleButton = document.getElementsByClassName("toggleButton")[0];
    toggleButton.textContent = text;
  }

  const toggleButton = document.getElementsByClassName("toggleButton")[0];
  toggleButton.addEventListener("click", handletoggle);
});
