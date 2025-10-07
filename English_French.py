
def lang(x):

    print (x)
    t=0
    s=0
    for i in x:
        if i == "t" or i == "T":
            t+=1
        elif i == "s" or i == "S":
           s+=1
    compare = t-s
    if compare <= 0:
        print("(probably) French text")
    elif compare > 0:
        print("(probably) English text")

lang("3 The red cat sat on the mat.Why are you so sad cat? Dont ask that.")
def lang(x):
    t=0
    s=0
    for char in x:
        if char =="t" or char =="T":
            t+=1
        if char =="w" or char =="S":
            s+=1