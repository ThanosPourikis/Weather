function getCurLoc(){
    var x = document.getElementById('clickMe');
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
      } else {
        x.value = "Geolocation is not supported by this browser.";
      }
      
}

function showPosition(position) {
    var x = document.getElementById('clickMe');
    x.value = "Latitude: " + position.coords.latitude +
    "<br>Longitude: " + position.coords.longitude;
  }

