const minPriceSlider = document.getElementById("min-price-slider");
const maxPriceSlider = document.getElementById("max-price-slider");
const minPriceValue = document.getElementById("min-price-value");
const maxPriceValue = document.getElementById("max-price-value");
const productList = document.getElementById("product-list");

minPriceSlider.addEventListener("input", function () {
  minPriceValue.textContent = minPriceSlider.value;
  updateProductList();
});

maxPriceSlider.addEventListener("input", function () {
  maxPriceValue.textContent = maxPriceSlider.value;
  updateProductList();
});

function updateProductList() {
  const minPrice = parseInt(minPriceSlider.value);
  const maxPrice = parseInt(maxPriceSlider.value);
  const products = productList.getElementsByTagName("li");

  for (let i = 0; i < products.length; i++) {
    const productPrice = parseInt(
      products[i].textContent.split(" - ")[1].replace("$", "")
    );
    if (productPrice >= minPrice && productPrice <= maxPrice) {
      products[i].style.display = "inline-block";
    } else {
      products[i].style.display = "none";
    }
  }
}
