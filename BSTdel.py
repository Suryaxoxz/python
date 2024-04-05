class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class Tree:
    def __init__(self):
        self.node = None
    
    def insert(self,node,data):
        if node is None:
            return Node(data)
 
        if data < node.data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right, data)
 
        return node

    def delete(self, key):
        self.root = self._delete(self.node, key)

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
    
    def print_tree(self):
        print("\nPREORDER:")
        self._preorder(self.root)
        print("\nINORDER:")
        self._inorder(self.root)
        print("\nPOSTORDER:")
        self._postorder(self.root)

    def _preorder(self, node_data):
        if node_data is not None:
            print(node_data.data, end=' ')
            self._preorder(node_data.left)
            self._preorder(node_data.right)

    def _inorder(self, node_data):
        if node_data is not None:
            self._inorder(node_data.left)
            print(node_data.data, end=' ')
            self._inorder(node_data.right)

    def _postorder(self, node_data):
        if node_data is not None:
            self._postorder(node_data.left)
            self._postorder(node_data.right)
            print(node_data.data, end=' ')




       

tree = Tree()
lst = list(map(int, input().split()))
for i in lst:
   tree.node=tree.insert(tree.node,i)

k=int(input())
tree.delete(k)
tree.print_tree()