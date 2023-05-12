var containerId = "clock-container";
var html = "<div id='" + containerId + "'></div>";
Office.context.application.getActivePage().content.insertHtml(html);
function updateClock() {
  var now = new Date();
  var hours = now.getHours();
  var minutes = now.getMinutes();
  var seconds = now.getSeconds();
  var timeString = hours + ":" + minutes + ":" + seconds;
  document.getElementById("clock-container").innerText = timeString;
}

updateClock();
setInterval(updateClock, 1000);
