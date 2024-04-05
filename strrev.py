def reverse(string):
    s=""
    for i in string:
        s = i+s
    return s
        
st="surya"
a=reverse(st)
print(a)