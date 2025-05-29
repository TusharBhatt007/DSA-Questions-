class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data 
    def insert(self,root,data):
        if root == None:
            return Node(data)
        elif root.data > data:
            root.left = self.insert(root.left,data)
        elif root.data < data:
            root.right = self.insert(root.right , data)
        return root
    
class MaxDepth:
    def __init__(self,root):
        self.root = root
    
    def maxDepth(self,root):
        if root:
            return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        else:
            return 0
r = Node(10)
r.insert(r,9)
# r.insert(r,11)
# r.insert(r,12)
# r.insert(r,13)
# r.insert(r,14)
# r.insert(r,8)
# r.insert(r,7)

obj1 = MaxDepth(r)
print(obj1.maxDepth(r))