
var htmlWriterhref = function(url, fontsize, color, label)
{
return ("<a href =\"" + url +  "\"style=\"font-size: "+ fontsize +"px; text-decoration: none; color: "+ color +"\" > "+ "<span class=\"underline_me\">"+label +"</span> </a>"	);

}
/*
var read_csv_file = function(filename)
{
     var reader = new FileReader();
	 reader.onload = function(e) 
	 {var text = reader.result;
	 console.log(text);
	 }
reader.readAsText(filename);

}*/
filename = "collegelist.txt"
function analyze(){
   var f = new FileReader();

   f.onloadend = function(){
       console.log("success");
   }
   f.readAsText("collegelist.txt");
}



a = htmlWriterhref("http://www.kcgcollege.ac.in", 60, "RebeccaPurple ","GAME");


analyze()

document.write("<p> " +a+a+a+a+a+a+a+a+a+a+ "</p>")