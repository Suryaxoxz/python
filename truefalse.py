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


ll = LinkedList()
a = [6, 2, 6, 4, 5, 6]
for i in a:
    ll.create(i)
ll.display()            