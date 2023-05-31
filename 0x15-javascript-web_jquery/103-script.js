const $ = window.$;
window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    greet();
  });
  $('INPUT#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      greet();
    }
  });
};

function greet () {
  const lang = $('INPUT#language_code').val();
  const link = 'https://fourtonfish.com/hellosalut/?lang=';
  $.get(link + lang, function (data, tStatus) {
    $('DIV#hello').text(data.hello);
  });
}
