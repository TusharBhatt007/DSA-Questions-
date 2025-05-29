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

class TreePath:
    pathList = list()
    def __init__(self,root):
        self.root = root
    
    def findPath(self,currentList,root):
        if root:
            currentList = currentList + [root.data]
            if root.left == None and root.right == None:
                TreePath.pathList.append(currentList)
    
            else:
                self.findPath(currentList,root.left)
                self.findPath(currentList,root.right)
        else:
            return -1
        
r=Node(3)
r.insert(r,1)
r.insert(r,9)
r.insert(r,20)
r.insert(r,15)
r.insert(r,7)
r.insert(r,21)

obj1 = TreePath(r)
obj1.findPath(list(),r)
print(obj1.pathList)