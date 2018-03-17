// Carrega o formulário de saída que é utilizado no home
// $(document).ready(function() {

  function loadSaidaForm(url){
    $.ajax({
        type: "GET",
        url: url,

        beforeSend: function(xhr, settings) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: function(data){
          $("#saidaform").html(data);
          $('select').select2();
        }
    });
  }
  // Carraga o formulário de devolução que é utilizado na home
  function loadDevolucaoForm(url){
    $.ajax({
        type: "GET",
        url: url,

        beforeSend: function(xhr, settings) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: function(data){
          $("#retornoform").html(data);
          $('select').select2();
        }
    });
  }


// });
