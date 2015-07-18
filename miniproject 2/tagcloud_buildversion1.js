//variables
var lines;
var linklabelarray = [];

var htmlWriterhref = function(url, fontsize, color, label)
{
return ("<a href =\"" + url +  "\"style=\"font-size: "+ fontsize +"px; text-decoration: none; color: "+ color +"\" > "+ "<span class=\"underline_me\">"+label +"</span> | </a>"	);

}

document.getElementById('file').onchange = function()
{

var file = this.files[0];

//console.log( file2);
var reader = new FileReader();

reader.onload = function(progressEvent){
    // Entire file
    //console.log(this.result);

    // By lines
    lines = this.result.split('\n');
    for(var i = 0; i < lines.length; i++)
	{ temp = lines[i].split(',');
      label = temp[1];
	  link = temp[2];
	  a = htmlWriterhref(link, 60, "RebeccaPurple ",label);
	  linklabelarray += a;
      //console.log(a);
    
	} 
	
	document.write("<p> " +linklabelarray+ "</p>")
	//document.write(a)
	document.write( "<style>.underline_me:hover{text-decoration: underline;color: GoldenRod  }</style>")
     
  };
  
  reader.readAsText(file);
};

//a = htmlWriterhref("http://www.kcgcollege.ac.in", 60, "RebeccaPurple ","GAME");
//document.write("<p> " +a+a+a+a+a+a+a+a+a+a+ "</p>")
