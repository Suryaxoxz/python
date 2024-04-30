def longest_palin(s):
	count = -1
	ans = ""

	n = len(s)
	
	dp = [[False] * n for _ in range(n)]

	for g in range(n):
		for i in range(n - g):
			j = i + g
			if g == 0:
				dp[i][j] = True
			elif g == 1:
				dp[i][j] = (s[i] == s[j])
			else:
				dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])

			if dp[i][j] and count < j - i + 1:
				ans = s[i:j + 1]
				count = len(ans)
	return ans

str = input()

#abcdracecarhjkl
#manacher agorithm 
#A#B#C#D#R#A#C##C#A#R#G#H#I#J#

print(longest_palin(str))