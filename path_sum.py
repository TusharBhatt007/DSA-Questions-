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
    
class PathSum:
    pathPresent = False
    def __init__(self,root,target):
        self.root = root
        self.target = target
    
    def pathSum(self,target,total,root):
        if root:
            if root.left == None and root.right==None:
                total+=root.data
                if total == target:
                    PathSum.pathPresent = True
            
            self.pathSum(target,total+root.data,root.left)
            self.pathSum(target,total+root.data,root.right)
        else:
            return 0

r=Node(3)
r.insert(r,1)
r.insert(r,9)
r.insert(r,20)
r.insert(r,15)
r.insert(r,7)

obj1 = PathSum(r,104)
obj1.pathSum(104,0,r)
print(obj1.pathPresent)