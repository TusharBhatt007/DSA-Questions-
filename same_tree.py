class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None 
    
    def insert(self,r,data):
        if r == None:
            return Node(data)
        elif r.data > data:
            r.left = self.insert(r.left,data)
        elif r.data < data:
            r.right = self.insert(r.right,data)
        return r
    
class SameTree:
    treeSame = True
    def __init__(self,r1,r2):
        self.r1 = r1
        self.r2 = r2
    
    def sameTree(self,r1,r2):
        if r1 and r2 and SameTree.treeSame:
            self.sameTree(r1.left , r2.left)
            if r1.data !=r2.data:
                    print("inside trees not identical condition")
                    SameTree.treeSame = False
            self.sameTree(r1.right,r2.right)
            
        else:
            if r1!=r2:
                SameTree.treeSame = False

r1 = Node(10)
r2 = Node(10)
r1.insert(r1,11)
r2.insert(r2,11)
r1.insert(r1,9)
r2.insert(r2,9)
r2.insert(r2,16)

obj1 = SameTree(r1,r2)
obj1.sameTree(r1,r2)
print('value of ',obj1.treeSame)
if obj1.treeSame:
    print("trees are indentical")
else:
    print('trees are not identical')
        
