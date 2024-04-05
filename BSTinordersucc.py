class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class tree:
    def __init__(self,root):
        self.root=None

        def insert(self,node,data):
            if node is None:
                return node(data)
 
            if data < node.data:
                node.left = self.insert(node.left,data)
            else:
                node.right = self.insert(node.right, data)
 
            return node
        
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.data:
            node.left = self._delete(node.left, key)
        elif key > node.data:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self._min_value_node(node.right)
            node.data = temp.data
            node.right = self._delete(node.right, temp.data)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def inordersuccessor(self,node,key):
        sp=self.node
        succ=self.node.right
        while(succ.left is not None):
            sp=succ
            succ=succ.left

        if(node!=sp):
            sp.left=succ.right
            sp.right=succ.right



       