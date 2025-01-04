# 입력 처리
N = int(input())
inputs = []

for i in range(0, N):
    inputs.append(input().split())

class BinaryTree:
    def __init__(self):
        self.tree = {}
    
    def add_node(self, parent, left, right):
        self.tree[parent] = (left, right)
    
    def pre_order(self, node):
        if node == '.':
            return
        print(node, end="")
        self.pre_order(self.tree[node][0])
        self.pre_order(self.tree[node][1])
    
    def post_order(self, node):
        if node == '.':
            return
        self.post_order(self.tree[node][0])
        self.post_order(self.tree[node][1])
        print(node, end="")

    def in_order(self, node):
        if node == '.':
            return
        self.in_order(self.tree[node][0])
        print(node, end="")
        self.in_order(self.tree[node][1])

bt = BinaryTree()
for i in range(0, N):
    parent, left, right = inputs[i]
    bt.add_node(parent, left, right)

bt.pre_order('A')
print()
bt.in_order('A')
print()
bt.post_order('A')