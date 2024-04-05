x,y=map(int,input().split())
maxi=[]
for _ in range(x):
    li=list(map(int,input().split()))
    maxi.append(max(li))
print(*maxi)

'''100 198 333 323
122 232 221 111
223 565 245 764'''