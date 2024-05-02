$(document).ready(function(){
  // Function to fetch and print translation of "Hello" depending on the language
  function fetchTranslation(languageCode) {
    $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode })
      .done(function(data) {
        $('#hello').text(data.hello);
      })
      .fail(function() {
        $('#hello').text('Error fetching translation');
      });
  }

  // Event listener for the button click
  $('#btn_translate').click(function(){
    var languageCode = $('#language_code').val();
    fetchTranslation(languageCode);
  });
});
