def spaces(n,x,y):
    g=0
    print (n,x,y)
    for i in range(n):
        if x[i] == "c" and y[i]== "c":
            g+=1
    return g
print (g)
spaces(5,"c..c.c","cc.c.")
