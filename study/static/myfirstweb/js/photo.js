var API_KEY = '3101856-c81ddd27e6efeb0aaaf650ba9';
var CATEGORY = new Object();
var URL = "https://pixabay.com/api/?key=" + API_KEY + "&q=" + encodeURIComponent('fashion');
$.getJSON(URL, function(data) {
    if (parseInt(data.totalHits) > 0)
        $.each(data.hits, function(i, hit) { console.log(hit.pageURL); });
    else
        console.log('No hits');
});
