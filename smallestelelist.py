def Smallerval(arr, n):
	for i in range(1, n ):	
		for j in range(i-1 ,-2 ,-1):		
			if (arr[j] > arr[i]):			
				print(arr[j] ,", ",end="")
				break

arr = [6, 4, 2, 1, 5]
n = len(arr)
Smallerval(arr, n)