$(document).ready(function () {
    function animateOnScroll() {
      $(".fade").each(function () {
        var position = $(this).offset().top;
        var scroll = $(window).scrollTop();
        var windowHeight = $(window).height();

        if (scroll > position - windowHeight + 200) {
          $(this).addClass("fade-in");
        } else {
          $(this).removeClass("fade-in");
        }
      });
    }

    animateOnScroll();
    $(window).scroll(function () {
      animateOnScroll();
    });

    let currentPage = 0;
    const rooms = $(".room-content");
    const totalRooms = rooms.length;
    const roomsPerPage = 4;
    const totalPages = Math.ceil(totalRooms / roomsPerPage);

    function displayRooms() {
      rooms.stop(true, true).fadeOut(500, function () {
        const startIndex = currentPage * roomsPerPage;
        const endIndex = startIndex + roomsPerPage;
        rooms.slice(startIndex, endIndex).stop(true, true).fadeIn(500);
      });
    }

    function updatePaginationButtons() {
      $("#prev").prop("disabled", currentPage === 0);
      $("#next").prop("disabled", currentPage === totalPages - 1);
    }

    $("#prev").click(function () {
      if (currentPage > 0) {
        currentPage--;
        displayRooms();
        updatePaginationButtons();
      }
    });

    $("#next").click(function () {
      if (currentPage < totalPages - 1) {
        currentPage++;
        displayRooms();
        updatePaginationButtons();
      }
    });

    displayRooms();
    updatePaginationButtons();
  });