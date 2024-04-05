def insertAtBottom(stack, val):
	if isEmpty(stack):
		push(stack, val)
	else:
		temp = pop(stack)
		insertAtBottom(stack, val)
		push(stack, temp)

def reverse(stack):
	if not isEmpty(stack):
		
        temp = pop(stack)
        reverse(stack)
        insertAtBottom(stack, temp)
		
        
def createStack():
	stack = []
	return stack

def isEmpty(stack):
	return len(stack) == 0

def push(stack, val):
	stack.append(val)

def pop(stack):

	if(isEmpty(stack)):
		print("Stack Underflow ")
		exit(1)
	return stack.pop()

def prints(stack):
	for i in range(len(stack)-1, -1, -1):
		print(stack[i], end=' ')
	print()

stack = createStack()
push(stack, str(4))
push(stack, str(3))
push(stack, str(2))
push(stack, str(1))
push(stack, str(5))
print("Original Stack ")
print(stack)

#reverse(stack)
print("Reversed Stack ")
print(stack)

