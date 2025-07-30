<?php
function showAlert($message, $type = 'success', $redirect = null) {
    $icon = match($type) {
        'success' => 'success',
        'error' => 'error',
        'warning' => 'warning',
        'info' => 'info',
        default => 'info'
    };

    $title = match($type) {
        'success' => 'Berhasil!',
        'error' => 'Error!',
        'warning' => 'Peringatan!',
        'info' => 'Informasi',
        default => 'Informasi'
    };

    $redirectScript = $redirect ? "window.location.href = '$redirect';" : "";

    // Add SweetAlert2 script to head
    echo "
    <script src='https://cdn.jsdelivr.net/npm/sweetalert2@11'></script>
    <style>
        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translate3d(0, -20px, 0);
            }
            to {
                opacity: 1;
                transform: translate3d(0, 0, 0);
            }
        }
        .animated {
            animation-duration: 0.5s;
            animation-fill-mode: both;
        }
        .fadeInDown {
            animation-name: fadeInDown;
        }
    </style>
    ";

    // Show alert after page loads
    echo "
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            Swal.fire({
                title: '$title',
                text: '$message',
                icon: '$icon',
                confirmButtonText: 'OK',
                confirmButtonColor: '#224abe',
                customClass: {
                    popup: 'animated fadeInDown'
                }
            }).then((result) => {
                if (result.isConfirmed) {
                    $redirectScript
                }
            });
        });
    </script>
    ";
}
?>