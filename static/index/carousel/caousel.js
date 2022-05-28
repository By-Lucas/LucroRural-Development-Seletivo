/* Open when someone clicks on the span element */
function openNav() {
    document.getElementById("myNav").style.width = "100%";
  }
  
  /* Close when someone clicks on the "x" symbol inside the overlay */
  function closeNav() {
    document.getElementById("myNav").style.width = "0%";
  }
  
  /* Muda o tempo do carousel, e tira o mousehover */
  $('.carousel').carousel({
    interval: 3200,
    cycle: true,
    pause: "null"
  })