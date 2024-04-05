class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            first_item = self.items[-1]
            del self.items[-1]
            return first_item
        else:
            raise IndexError("Queue is empty")

    def size(self):
        count = 0
        for _ in self.items:
            count += 1
        return count

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue is empty")


# Example Usage:
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print("Queue size:", q.size())
    print("Front of the queue:", q.peek())

    print("Dequeue:", q.dequeue())
    print("Queue size after dequeue:", q.size())
