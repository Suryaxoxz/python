class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue_rear(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            removed_item = self.front.data
            if self.front == self.rear:
                self.front = self.rear = None
            else:
                current = self.front
                while current.next != self.rear:
                    current = current.next
                current.next = None
                self.rear = current
                del self.front
                self.front = self.rear
            return removed_item

    def insert_front(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front = new_node

    def insert_rear(self, item):
        self.enqueue_rear(item)

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            current = self.front
            while current:
                print(current.data, end=" ")
                current = current.next
            print()


if __name__ == "__main__":
    q = Queue()
    q.enqueue_rear(1)
    q.enqueue_rear(2)
    q.enqueue_rear(3)

    q.display()

    q.dequeue_front()
    q.display()

    q.insert_front(4)
    q.display()

    q.insert_rear(5)
    q.display()
