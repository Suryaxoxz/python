class Node:
    def __init__(self, data):
        self.data= data
        self.left= None
        self.right= None

class Tree:
    def __init__(self):
        self.root=None

    def insert(self,data):
        newnode=Node(data)
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
  

def Preorder(root):
    if root is None:
        return

    print(root.data, end=' ')
    Preorder(root.left)
    Preorder(root.right)


tree=Tree()
tree.insert(1)
tree.insert(2)

tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
print("Preorder traversal of binary tree is:")
Preorder(tree.root)