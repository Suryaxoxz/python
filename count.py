def occurance(wrd,k):
    count=0
    for i in wrd:
        if i==k:
            count=count+1
    return count

a="Umbrella"
k="l"
print(occurance(a,k))        