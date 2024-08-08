$(function () {
  // Handle click on the translate button
  $('INPUT#btn_translate').click(salute);

  // Handle keydown event for the input field
  $('#language_code').keydown(function (event) {
    if (event.key === 'Enter' || event.keyCode === 13) {
      salute();
    }
  });

  // Function to fetch and display the translation
  function salute () {
    const languageCode = $('#language_code').val();
    const urlApi = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;

    $.get(urlApi, function (data) {
      $('#hello').text(data.hello);
    });
  }
});
