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

    def rev(self,k):
        while(current != None):
            

obj=link()
obj.create(1)
obj.create(2)
obj.create(3)
obj.create(4)
obj.create(5)
obj.display()
obj.rev(3)
obj.display()