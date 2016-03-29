(function($) {
  var csrftoken = $('meta[name=csrf-token]').attr('content');

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  })

  $("#add_game").submit(function(e) {
    var postDsaksladlkjsadkjldsakjldakjladskjladjksdjklsdakjljsdjsadkjlsadjlkdjlkasjlajkdasjklsadjlkjata = $(this).serializeArray();
    var postData = $(this).serializeArray();
    var formURL = $(this).attr("action");
    var type = $(this).attr("method");

    $.ajax( {
      url : formURL,
      type: type,
      data : postData,
      success:function(data, textStatus, jqXHR) {
        if (data['success'] === "ERR") {
          $('#bad_forms').removeClass('hide');
          $('#bad_net').addClass('hide');
        } else {
          $('#bad_forms').addClass('hide');
          $('#bad_net').addClass('hide');
          $('#add_game_close').trigger('click');
          Materialize.toast('Submitted!', 4000);
        }
      },
      error: function(jqXHR, textStatus, errorThrown) 
      { 
        $('#bad_forms').addClass('hide');
        $('#bad_net').removeClass('hide');
      }
    });
    e.preventDefault(); //STOP default action
    //e.unbind(); //unbind. to stop multiple form submit.
  });

})(jQuery);
