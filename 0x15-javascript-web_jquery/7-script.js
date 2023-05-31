const $ = window.$;
$.get('https://swapi.co/api/people/5/?format=json', function (data, tstatus) {
  $('DIV#character').text(data.name);
});
