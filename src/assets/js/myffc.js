var slideIndex = 0;
var idx;
//carousel();
//loadIndex();

function carousel() {
    var i;
    var x = document.getElementsByClassName("indexSlides");
    for (i = 0; i < x.length; i++) {
      x[i].style.display = "none"; 
    }
    slideIndex++;
    if (slideIndex > x.length) {slideIndex = 1} 
    x[slideIndex-1].style.display = "block"; 
    setTimeout(carousel, 5000); 
}

//index is the parsed JSON file
function loadIndex(){
	var client = new XMLHttpRequest();
	var iresponse;
	client.open('GET', '/searchIndex.json');
	client.onreadystatechange = function() {
	  //alert(client.responseText);
	  iresponse = client.responseText;
	}
	client.send();
//	searchIndex = JSON.stringify(iresponse);
	searchIndex = JSON.parse(iresponse);
	try {
		idx = lunr.Index.load(searchIndex);
		console.log("index loaded");
	}catch(e){
		console.log("index load error -> "+e.message);
		idx = "nothing";
	}
}

function search(idx,searchterm) {
  var results = idx.search(searchterm);
  console.log(results);
}

