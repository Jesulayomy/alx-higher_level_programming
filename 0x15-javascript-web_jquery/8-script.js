const $ = window.$;
$.get('https://swapi.co/api/films/?format=json', function (data, tStatus) {
  const result = data.results;
  for (let i = 0; i < result.length; i++) {
    $('UL#list_movies').append('<li>' + result[i].title + '</li>');
  }
});
