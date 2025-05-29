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

class MinDepth:
    def __init__(self,root):
        self.root = root 
    
    def minDepth(self,root):
        if root:
            left_height = self.minDepth(root.left)
            right_height = self.minDepth(root.right)
            if left_height !=0 and right_height!=0:
                return 1+min(left_height , left_height)
            elif left_height==0 and right_height!=0:
                return 1+right_height
            elif left_height!=0 and right_height==0:
                return 1+left_height
            else:
                return 1
        else:
            return 0
r=Node(3)
r.insert(r,1)
r.insert(r,9)
r.insert(r,20)
r.insert(r,15)
r.insert(r,7)

obj1 = MinDepth(r)
print(obj1.minDepth(r))
