class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def add_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def add_rear(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node

    def remove_front(self):
        if self.is_empty():
            return None
        removed_data = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        return removed_data

    def remove_rear(self):
        if self.is_empty():
            return None
        removed_data = self.rear.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        return removed_data

    def peek_front(self):
        if self.is_empty():
            return None
        return self.front.data

    def peek_rear(self):
        if self.is_empty():
            return None
        return self.rear.data
