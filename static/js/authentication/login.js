$(document).ready(function () {
  var domainUrl = document.location.protocol + '//' + document.domain + ':' + document.location.port
  var route = domainUrl + '/'

  $('#login').on('submit', function (e) {
    e.preventDefault();
    $.ajax({
      headers: { 'X-CSRFToken': $("meta[name='csrf-token']").attr('content') },
      type: 'POST',
      url: route + 'login/',
      data: {
        username: $('#username').val(),
        password: $('#password').val()
      },
      success: function (response) {
        if (response.success) {
          alertify.success('Bienvenido!!!')
          window.location.href = route + 'dashboard/';
        } else {
          alertify.warning("Clave o Usuario invalido!")
        }
      },
      error: function () {
      }
    });
  });

  $('#register').on('submit', function (e) {
    e.preventDefault();
    $.ajax({
      headers: { 'X-CSRFToken': $("meta[name='csrf-token']").attr('content') },
      type: 'POST',
      url: route + 'register/',
      data: {
        name: $('#name_reg').val(),
        lastname: $('#lastname_reg').val(),
        email: $('#email_reg').val(),
        password: $('#password_reg').val()
      },
      success: function (response) {
        if (response.success) {
          alertify.success('Usuario Creado con exito!!!')
          window.location.href = route + 'login/';
        }
      },
      error: function () {
      }
    });
  });

});