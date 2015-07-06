def sed(pstr,rstr,fil1,fil2):
    """Reads a text file and replaces the pattern string
       with replacemnt dtring and writes it into a text file in append mode""" 
    try:
        with open(fil1,'r') as fin:
            with open(fil2, 'a') as fout:
                
                for data in fin:
                    
                    print data
                    data = data.replace(pstr,rstr)
                    fout.write(data)
    except:
        print "Error"
sed("hello","jolly","fil1.txt","fil2.txt")
