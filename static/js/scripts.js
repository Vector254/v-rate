$(document).ready(function() {
  $('.progress .progress-bar').css("width",
  function() {
  scale=$(this).attr("aria-valuenow")*10;
  return scale + "%";
  }
  )
  });