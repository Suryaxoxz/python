def pair_wise_consecutive(s):
	if len(s) % 2 != 0:
		s.pop()

	prev = s[-1] # Initialize prev with the top element
	s.pop()

	while s:
		curr = s[-1]
		s.pop()
		
		if abs(curr - prev) != 1:
			return "No"

		if s:
			prev = s[-1]
			s.pop()

	return "Yes"

if __name__ == "__main__":
	s = [4, 5, -2, -3, 11, 10, 5, 6, 20]
	result = pair_wise_consecutive(s)
	print(result) 
