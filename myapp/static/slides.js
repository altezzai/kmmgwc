const SLIDE_DELAY = 3000;
let slideIndex = 1;
let slideIndices = {};  // For multiple sliders

// NEWS SLIDER — global
function plusSlides(n) {
  slideIndex += n;
  showSlidesGlobal(slideIndex);
}

function currentSlide(n) {
  slideIndex = n;
  showSlidesGlobal(slideIndex);
}

function showSlidesGlobal(n) {
  const slides = document.getElementsByClassName("mySlides");
  if (!slides.length) return;

  if (n > slides.length) slideIndex = 1;
  if (n < 1) slideIndex = slides.length;

  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }

  slides[slideIndex - 1].style.display = "block";
  console.log("Showing news slide", slideIndex);
}

// ACTIVITY SLIDERS (per activity ID)
function plusSlidesActivity(n, sliderId) {
  if (!(sliderId in slideIndices)) slideIndices[sliderId] = 1;
  showSlidesActivity(sliderId, slideIndices[sliderId] + n);
}

function showSlidesActivity(sliderId, n) {
  const slides = document.getElementsByClassName(`mySlides-${sliderId}`);
  if (!slides.length) return;

  slideIndices[sliderId] = n;

  if (n > slides.length) slideIndices[sliderId] = 1;
  if (n < 1) slideIndices[sliderId] = slides.length;

  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }

  slides[slideIndices[sliderId] - 1].style.display = "block";
}

// Initialize sliders on DOM ready
document.addEventListener("DOMContentLoaded", function () {
  // Activity sliders
  const sliders = document.querySelectorAll('[id^="slider-"]');
  sliders.forEach((slider) => {
    const id = slider.id.replace("slider-", "");
    slideIndices[id] = 1;
    showSlidesActivity(id, 1);
    setInterval(() => {
      showSlidesActivity(id, slideIndices[id] + 1);
    }, SLIDE_DELAY);
  });

  // News slider
  const newsSlides = document.getElementsByClassName("mySlides");
  if (newsSlides.length > 0) {
    slideIndex = 1;
    showSlidesGlobal(slideIndex);
    setInterval(() => {
      plusSlides(1);
    }, SLIDE_DELAY);
  }
});
