class Node:
    def _init_(self, data):
        self.data = data
        self.right = None
        self.left = None

class Tree:
    def _init_(self):
        self.root = None

    def create(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = Node(data)
                        break
                    else:
                        current = current.left
                elif data > current.data:
                    if current.right is None:
                        current.right = Node(data)
                        break
                    else:
                        current = current.right

    def search(self, node, key):
        if node is None or node.data == key:
            return node
        if key < node.data:
            return self.search(node.left, key)
        return self.search(node.right, key)

    def printPreorder(self, root):
        if root:
            print(root.data, end=" ")
            self.printPreorder(root.left)
            self.printPreorder(root.right)
          
tree = Tree()
lst = list(map(int, input().split()))
for i in lst:
    tree.create(i)

print("Preorder traversal of binary tree is:")
tree.printPreorder(tree.root)

key = int(input("\nEnter the element to search: "))
result = tree.search(tree.root, key)
if result:
    print(f"Element {key} found in the tree.")
else:
    print(f"Element {key} not found in the tree.")