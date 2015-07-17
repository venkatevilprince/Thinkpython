 var kcgfunc = function(index) 
  {
        
        // change width
		a = "KCG College"
        b = "http://www.kcgcollege.ac.in";
		
		return [a,b]
      };
var txt = "Hello World!";
var htmlWriterhref = function(url, fontsize, color, label)
{
document.write("<a href =\"" + url +  "\"style=\"font-size: "+ fontSize +"px; text-decoration: none; color: "+ color +"\" > "+ label +" </a>"	);
}

/*
for (i = 0; i < myhref.length; i++) 
{ var x = kcgfunc(i);
  myhref[i].innerHTML = x[0]
  myhref[i].href = x[1]
  myhref[i].style.fontSize = (50+10*i) + 'px';
  console.log((50+10*i)+'px')
  myhref[i].style.color = "blue"
  
}*/
x = kcgfunc(0)
color = "green"
fontSize = 50
htmlWriterhref(x[0],60,"purple","GAME")
