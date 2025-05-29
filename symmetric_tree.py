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

class SymmetricTree:
    inorder_list = list()
    def __init__(self,r):
        self.root = r
    
    def checkSymmetric(self,root):
        if root:
            self.checkSymmetric(root.left)
            SymmetricTree.inorder_list.append(root.data)
            self.checkSymmetric(root.right)
        else:
            SymmetricTree.inorder_list.append(None)


r = Node(10)
r.insert(r,9)
r.insert(r,11)

obj1 = SymmetricTree(r)
obj1.checkSymmetric(r)

i=0
j=len(obj1.inorder_list)-1
treeSymmetry = True
while i<j:
    if obj1.inorder_list[i]!=obj1.inorder_list[j]:
        treeSymmetry = False
        break
    i+=1
    j-=1
if treeSymmetry:
    print("Tree is symmetrical")
else:
    print("Tree is not symmetrical")