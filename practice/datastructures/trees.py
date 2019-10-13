class node:
   def __init__(self, key):
      self.left = None
      self.right = None
      self.val = key

def printInorder(root):
   if root:
      printInorder(root.right)

      print(root.val)

      printInorder(root.left)

def preOrder(root):
   if root:
      print(root.val)
      preOrder(root.left)
      preOrder(root.right)

def postOrder(root):
   if root:
      postOrder(root.left)
      postOrder(root.right)
      print(root.val)

root = node(1) 
root.left      = node(2) 
root.right     = node(3) 
root.left.left  = node(4) 
root.left.right  = node(5) 

postOrder(root)
