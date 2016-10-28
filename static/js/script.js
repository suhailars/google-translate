$(function(){
  var time;
  $('#english').on('input', (function(){
    var user = $('#english').val();
    var pass = $('#other').val();
    clearTimeout(time)
    time = setTimeout(function () {
      $.ajax({
        url: '/translate',
        data: $('form').serialize(),
        type: 'POST',
        success: function(response){
        	var result = JSON.parse(response).resp;

        	console.log(JSON.parse(response).resp);
          $('#other').val(result);
        },
        error: function(error){
        	console.log(error);
        }
      })
    }, 500);
  }));
});
