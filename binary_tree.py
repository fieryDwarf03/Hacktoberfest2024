class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# Inorder traversal (Left -> Root -> Right)
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

# Preorder traversal (Root -> Left -> Right)
def preorder_traversal(root):
    if root:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Postorder traversal (Left -> Right -> Root)
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")

# Example Usage
if __name__ == "__main__":
    # Creating the tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder traversal:")
    inorder_traversal(root)
    print("\nPreorder traversal:")
    preorder_traversal(root)
    print("\nPostorder traversal:")
    postorder_traversal(root)
