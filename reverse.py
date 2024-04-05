class node():
    def __init__(self,data):
        self.data=data
        self.next=None
class link():
    def __init__(self):
        self.head=None
        self.temp=None
    def create(self,data):
        if self.head==None:
            self.head= node(data)
            self.temp=self.head
        else:
            self.temp.next=node(data)
            self.temp=self.temp.next
        print(self.temp.data)

    def display(self):
        self.temp=self.head
        while self.temp.next !=None:
            print(self.temp.data,end=" ")
            self.temp=self.temp.next
        print(self.temp.data)

    def delete_end(self):
        if self.head==None:
            print( "list is empty")
        else:
            self.temp = self.head
            self.prev = self.head
            while self.temp.next != None:
                self.prev = self.temp
                self.temp = self.temp.next
            self.prev.next = None
  
    def insert_start(self,data):
        Node = node(data)
        if self.head==None:
            self.head=Node
            self.head.next=None
        else:
            self.temp = self.head
            self.head = Node
            self.head.next = self.temp

  
    def rev(self):
        self.prev=None
        current_node=self.head
        self.next=current_node.next
        while (current_node != None):
            self.next=current_node.next
            current_node.next=self.prev
            self.prev=current_node
            current_node=current_node.next
        self.head=self.prev             

obj=link()
obj.insert_start(5)
obj.insert_start(4)
obj.insert_start(3)
obj.insert_start(2)
obj.insert_start(1)
obj.display()
obj.rev()
obj.display()

