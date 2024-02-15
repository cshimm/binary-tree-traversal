import unittest

class TreeNode():
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

# create an array to store values from TreeNodes for assertions
preorder_arr = []    
postorder_arr = []
inorder_arr = []
# When we visit a node, we append to appropriate array
def preorder(node):
    if node:
        preorder_arr.append(node.value)
        preorder(node.left)
        preorder(node.right)
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        postorder_arr.append(node.value)
def inorder(node):
    if node:
        inorder(node.left)
        inorder_arr.append(node.value)
        inorder(node.right)

def levelorder(node):
    level_height = height(node)
    for i in range(1, level_height + 1):
        printcurrentlevel(node, i)
# Find the height of a given node represented as an integer
def height(node) -> int:
    if (node == None): return 0
    lheight = height(node.left)
    rheight = height(node.right)
    return lheight + 1 if lheight > rheight else rheight + 1

#print all the node values given a current level
def printcurrentlevel(node, level):
    if node == None: return
    if level == 1:
        print(node.value, end=" ")
    elif level > 1:
        printcurrentlevel(node.left, level - 1)
        printcurrentlevel(node.right, level - 1)

#Test cases where we compare the arrays with an expected array
class TestBinaryTreeTraversal(unittest.TestCase):
    def test_inorder(self):
        tree = TestTree()
        inorder(tree.root)
        self.assertEqual(inorder_arr, [3, 5, 9, 10, 15, 20, 25])
    def test_preorder(self):
        tree = TestTree()
        preorder(tree.root)
        self.assertEqual(preorder_arr, [10, 5, 3, 9, 20, 15, 25])
    def test_postorder(self):
        tree = TestTree()
        postorder(tree.root)
        self.assertEqual(postorder_arr, [3, 9, 5, 15, 25, 20, 10])
    def test_levelorder(self):
        tree = TestTree()
        levelorder(tree.root)

# Test tree that reflects the tree used in the slides
class TestTree():
    def __init__(self) -> None:
        self.root = TreeNode(10)
        self.root.left = TreeNode(5)
        self.root.left.left = TreeNode(3)
        self.root.left.right = TreeNode(9)
        self.root.right = TreeNode(20)
        self.root.right.left = TreeNode(15)
        self.root.right.right = TreeNode(25)

if '__main__' == __name__:
    unittest.main()