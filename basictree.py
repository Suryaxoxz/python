class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None

    def insert(self,data):
        newnode=node(data)
        if self.root is None:
            self.root=newnode
            print(self.root.data)
        else:
            temp=self.root
            flag=0
            temp1=self.root
            while True:
                if temp.left is None:
                    temp.left=newnode
                    print(temp.left.data)
                    break
                elif temp.right is None:
                    temp.right=newnode
                    print(temp.right.data)
                    break
                elif flag==0:
                    temp=temp1.left
                    flag=1
                else:
                    temp=temp1.right
                    flag=0
                    temp1=temp1.left
    def search(root,key):
        if root is None:
            return node(key)
        elif root.data > key:
            root.left= search(root.left,key)
        elif root.data < key:
            root.right = search(root.right,key)
        return root
           

    def print_tree(self):
        if self.root is None:
            print("Tree is empty")
            return

        def print_recursive(node, level=0):
            if node:
                print("  " * level + str(node.data))
                print_recursive(node.left, level + 1)
                print_recursive(node.right, level + 1)

        print_recursive(self.root)

        
t=tree()
t.insert(1)
t.insert(2)
t.insert(3)
t.insert(4)
t.insert(5)
t.insert(6)
t.insert(7)
t.print_tree()
key=6
root = None
t.search(key)
if t.search(key) is None:
    print("key not found")
else:
    print("key found")    