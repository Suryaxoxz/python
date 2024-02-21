class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' <-> ')
            current = current.next
        print("None")

# Function to take user input for adding a node
def add_node(dll):
    data = input("Enter data for the new node: ")
    position = input("Enter 'A' to append, 'P' to prepend: ").upper()
    if position == 'A':
        dll.append(data)
    elif position == 'P':
        dll.prepend(data)
    else:
        print("Invalid position specified.")

# Function to take user input for deleting a node
def delete_node(dll):
    data = input("Enter data to delete: ")
    dll.delete(data)

# Example usage:
dll = DoublyLinkedList()
n=int(input("enter number of datas:")) 
for i in range(n):
    add_node(dll)

dll.display()

delete_node(dll)
dll.display()
