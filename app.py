words = ("""3
The red cat sat on the mat.
Why are you so sad cat?
Don't ask that.""")
print (words)
t=0
s=0
for letters in words:
    if letters == "t" or letters == "T":
        t=t+1
    elif letters == "s" or letters == "S":
        s=s+1
compare = t-s
if compare <= 0:
    print("(probably) French text")
elif compare > 0:
    print("(probably) English text")
"""print (compare)
print (f"t={t}")
print (f"s={s}")"""