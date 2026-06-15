// Gallery Modal - CSP compliant (no inline handlers)
document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById("imageModal");
    const modalImg = document.getElementById("modalImg");
    const closeBtn = document.getElementById("modalClose");

    function openModal(imgSrc) {
        if (modal && modalImg) {
            modal.style.display = "block";
            modalImg.src = imgSrc;
        }
    }

    function closeModal() {
        if (modal) {
            modal.style.display = "none";
        }
    }

    // Attach click to all gallery images
    document.querySelectorAll('.gallery-img').forEach(function (img) {
        img.addEventListener('click', function () {
            openModal(this.src);
        });
    });

    // Close button
    if (closeBtn) {
        closeBtn.addEventListener('click', closeModal);
    }

    // Click outside modal
    if (modal) {
        window.addEventListener('click', function (event) {
            if (event.target === modal) {
                closeModal();
            }
        });
    }

    // ESC key
    document.addEventListener('keydown', function (event) {
        if (event.key === "Escape") {
            closeModal();
        }
    });
});
