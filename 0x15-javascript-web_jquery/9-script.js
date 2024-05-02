// Fetches translation of "hello" in French and displays it in the DIV#hello tag

$.get('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .done(function(data) {
    $('#hello').text(data.hello);
  })
  .fail(function() {
    $('#hello').text('Error fetching translation');
  });
