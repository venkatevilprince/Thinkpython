def draw_grid(n,m):
    for i in range(n):
        for j in range(m):
            print "+",
            for k in range(4):
                print "-",
        print"+"
        for l in range(4):
            for l2 in range(m+1):
                print "|        ",
            print""    
    for j in range(m):
            print "+",
            for k in range(4):
                print "-",
    print"+"
# parameters are rows and columns
# u can try different rows and columns

draw_grid(5,5)




    
