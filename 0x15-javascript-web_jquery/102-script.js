$(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();

    // I changed the link given in the task because it returns a 301 moved perminantly error
    // This is the new link I got from the same website.
    const urlApi = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;

    $.get(urlApi, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
