(function() {
  'use strict';

  // Django CSRF setup

  var csrftoken = $.cookie('csrftoken');

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });

  $('[data-delete]').click(function(event) {
    var deleteId = $(event.currentTarget).data('delete');
    $.ajax({
      url: '/',
      method: 'DELETE',
      data: JSON.stringify({
        'id': deleteId
      }),
      success: function() {
        console.log('success!');
        location.reload();
      },
      error: function(jqXHR, textStatus, errorThrown) {
        console.log('error!');
        console.log(errorThrown);
      }
    })
  });
})();
