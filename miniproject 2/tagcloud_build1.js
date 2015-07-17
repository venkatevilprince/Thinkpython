
var htmlWriterhref = function(url, fontsize, color, label)
{
return ("<a href =\"" + url +  "\"style=\"font-size: "+ fontsize +"px; text-decoration: none; color: "+ color +"\" > "+ "<span class=\"underline_me\">"+label +"</span> </a>"	);

}


a = htmlWriterhref("http://www.kcgcollege.ac.in", 60, "RebeccaPurple ","GAME");


document.write("<p> " +a+a+a+a+a+a+a+a+a+a+ "</p>")