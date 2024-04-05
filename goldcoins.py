def goldcoins(n,k,coins):
    start=0
    cur_sum=0

    for i in range(n):
        cur_sum+=coins[i]
        while(cur_sum > k):
            cur_sum-=coins[i]
            start+=1
        if cur_sum == k:
            return start + 1 , i+1
n=10
k=15
coins = [5,3,7,14,18,1,18,4,8,3]
print(goldcoins(n,k,coins))