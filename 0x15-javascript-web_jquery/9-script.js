const $ = window.$;
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, tStatus) {
  $('DIV#hello').text(data.hello);
});
