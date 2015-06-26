def right_justify(word,spaces):
    for i in range(spaces):
        print " ",
    print "%s" %(word)
decision='y'    
while(decision=='y' or decision =='Y'):
    s=raw_input("enter the spaces")
    s = int(s)
    right_justify("allen",s)
    decision=raw_input("Do you want t continue(Press y to continue)")
