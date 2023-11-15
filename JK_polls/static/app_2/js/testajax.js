var create_note = function() {
  var param_nom = $("#nom").val()
  var param_date = $("#date").val()
  if (param_nom != "" && param_date != "" ) { // Fields must actually contain something
    var data = { param_nom, param_date};
    var args = { type:"POST", url:"create/", data:data };
    $.ajax(args);
  }
  else {
      console.log('woupse !' + errorMessage);
    // display an explanation of failure -- optional for starters
  }
  return false;
};