const $ = window.$;
window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    const link = 'https://fourtonfish.com/hellosalut/?lang=';
    $.get(link + lang, function (data, tStatus) {
      $('DIV#hello').text(data.hello);
    });
  });
};
