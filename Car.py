def spaces(x,y):
    n=5
    g=0
    for i in range(n):
        if x[i] == "c" and y[i] == "c":
            x+=1
    print(x)
spaces("ccc..",".c.c.c")
