class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class bst:
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
    def min(node):
        if node is None:
            return 0

        leftval=min(node.left)           
        rightval=min(node.right)

        value=0

        if leftval < rightval:
            value=leftval
        else:
            value=rightval

        if value <node:
            value = node.data    

    def max(node):
        if node is None:
            return 0

        leftval=max(node.left)
        rightval=min(node.right)

        value=0

        if leftval > rightval:
            value=leftval
        else:
            value=rightval

        if value <node.data:
            value=node.data                    

    def isbinary(node):
        if node is None:
            return True
        
        if(node.left is not None and max(node.left) > node.data):
            return False
        if(node.right is not None and min(node.right) < node.data):
            return False
        if(isbinary(node.left) is False or isbinary(node.right) is False):
            return False
        
        return True    

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

if __name__ == "__main__":
    root=bst()
    root.insert(1)
    root.insert(2)

    root.insert(3)
    root.insert(4)
    root.insert(5)

    root.isbinary()
    root.print_tree()
