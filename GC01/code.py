
# Structure
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None 
    self.right = None

# Build tree
# Depth 0
root = Node(data=1)

# Depth 1
root.left = Node(data=2)
root.right = Node(data=3)

# Depth 2
root.left.left = Node(data=4)
root.right.left = Node(data=5)
root.right.right = Node(data=6)

# Depth 3
root.left.left.left = Node(data=7)
root.left.left.right = Node(data=8)

root.right.right.left  = Node(data=9)

# Depth 4
root.left.left.right.left = Node(data=10)


def inorder(node: Node):
  if node.left is not None:
    inorder(node.left)
    print(node.data)
    if node.right is not None:
      inorder(node.right)
  else:
    print(node.data)
  
  
# L - 자신 - R
inorder(root)