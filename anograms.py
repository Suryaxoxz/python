def anogram(a,b):
    if sorted(a)==sorted(b):
        print("anogram")
    else:
        print("not an anogram")

x="listen"
y="silent" 
print(anogram(x,y))       