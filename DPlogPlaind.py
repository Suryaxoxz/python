#MANACHER ALGORITHM
#F#O#R#G#E#E#K#S#S#K#E#E#G#F#O#R#
def longestPalSubstr(string):
	n = len(string) 
	if (n < 2):
		return n 
	
	start=0
	maxLength = 1
	for i in range(n):

		low = i - 1
		high = i + 1
		while (high < n and string[high] == string[i] ):					 
			high=high+1
	
		while (low >= 0 and string[low] == string[i] ):				 
			low=low-1
	
		while (low >= 0 and high < n and string[low] == string[high] ):
			low=low-1
			high = high+1

		length = high - low - 1	
		if (maxLength < length):
			maxLength = length
			start=low+1
			
	print ("Longest palindrome substring is:",end=" ")
	print (string[start:start + maxLength])
	
	return maxLength
	
string = ("abcdracecarghij")
print("Length is: " + str(longestPalSubstr(string)))
'''

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s2 = s[::-1]
        n = len(s)

        prev = [0 for i in range(n+1)]

        for i in range(1, n+1):
            curr = [0 for x in range(n+1)]
            for j in range(1, n+1):
                if s[i-1] == s2[j-1]:
                    curr[j] = prev[j-1] + 1
                else:
                    curr[j] = max(curr[j-1], prev[j])
            prev = curr

        return curr[n]

		
'''