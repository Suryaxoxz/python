class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.next = None
        self.head = None
        self.temp = None

    def create(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.temp = self.head
        else:
            self.temp.next = newnode
            self.temp = newnode

    def display(self):
        temp = self.head
        if self.head is None:
            print("None")
            return
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def swaping(self):

        x = int(input("\n Enter swap data : "))
        y = int(input("\n Enter swap data : "))
        if x == y:
            return

        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next

        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next

        if currX == None or currY == None:
            return
        if prevX != None:
            prevX.next = currY
        else: 
            self.head = currY

        if prevY != None:
            prevY.next = currX
        else:  
            self.head = currX

        temp = currX.next
        currX.next = currY.next
        currY.next = temp
        ll.display()



ll = LinkedList()
a = [1, 2, 3, 4, 5, 6]
for i in a:
    ll.create(i)
ll.display()

ll.swaping()
ll.swaping()
ll.swaping()