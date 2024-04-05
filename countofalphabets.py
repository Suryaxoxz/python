vowel="aeiouAEIOU"
consonents="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

v_count=0
c_count=0

a="surya"
for i in a:
    if i in vowel:
        v_count=v_count+1
    else:
        c_count+=1
print("Vowel count",v_count)
print("consonents count",c_count)


            