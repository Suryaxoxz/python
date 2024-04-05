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

    def insert_at_position(self, data, position):
        if position < 0:
            print("Invalid position")
            return
        new_node = Node(data)
        if position == 0:
            self.prepend(data)
            return
        current = self.head
        current_position = 0
        while current_position < position - 1 and current.next:
            current = current.next
            current_position += 1
        if current is None:
            print("Position out of range")
            return
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node


    def delete_at_position(self, position):
        if position < 0:
            print("Invalid position")
            return
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        if position == 0:
            self.head = current.next
            if self.head:
                self.head.prev = None
            return
        current_position = 0
        while current_position < position and current.next:
            current = current.next
            current_position += 1
        if current is None:
            print("Position out of range")
            return
        if current.next:
            current.next.prev = current.prev
        current.prev.next = current.next
    
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
