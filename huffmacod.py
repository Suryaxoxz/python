from collections import defaultdict

class Node:
    def _init_(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

def build_frequency_dict(text):
    freq_dict = defaultdict(int)
    for char in text:
        freq_dict[char] += 1
    return freq_dict

def build_huffman_tree(freq_dict):
    
    nodes = [Node(value, freq) for value, freq in freq_dict.items()]

    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.freq)
        left_node = nodes.pop(0)
        right_node = nodes.pop(0)

        parent_node = Node(None, left_node.freq + right_node.freq)
        parent_node.left = left_node
        parent_node.right = right_node

        nodes.append(parent_node)

    return nodes[0]

def traverse_tree(node, current_code, codes):
    if node.value is not None:
        codes[node.value] = current_code
        return

    if node.left:
        traverse_tree(node.left, current_code + "0", codes)
    if node.right:
        traverse_tree(node.right, current_code + "1", codes)

text = "hhhdsbdhdn"
freq_dict = build_frequency_dict(text)
root = build_huffman_tree(freq_dict)
codes = {}
traverse_tree(root, "", codes)

print("Huffman codes:")
for char, code in codes.items():
    print(f"{char}: {code}")
