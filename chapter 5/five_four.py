
def is_triangle(l1,l2,l3):
    
    """Returns whether or not a triangle can be
       constructed with the side lengths"""
    
    if(l1>l2+l3 or l2>l1+l3 or l3>l1+l2):
        print "no, cannot form a triangle"
    else:
        print "yes, ofcourse you can make a triangle";

l1=raw_input("enter the side length1");l1=int(l1)
l2=raw_input("enter the side length2");l2=int(l2)
l3=raw_input("enter the side length3");l3=int(l3)

is_triangle(l1,l2,l3)




        
