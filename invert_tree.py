class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self,root,data):
        if root == None:
            return Node(data)
        elif root.data > data:
            root.left = self.insert(root.left,data)
        elif root.data < data:
            root.right = self.insert(root.right,data) 
        return root

class InvertTree:
    def __init__(self,root):
        self.root1 = root
        self.root2 = root
    
    def invertTree(self,root1,root2):
        pass