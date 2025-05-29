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

    
class HBT:
    balanced = True
    def __init__(self,root):
        self.root = root 
    
    def hbt(self,root):
        if root:
            left_height = self.hbt(root.left)
            right_height = self.hbt(root.right)
            print('This is the value of root ',root.data)
            print('This is the value of left tree ',left_height)
            print('This is the height of right tree ',right_height)
            if abs(left_height - right_height) > 1:
                HBT.balanced = False
                return -1

            else:
                return max(left_height, right_height)+1
        else:
            return 0

r = Node(3)
r.insert(r,2)
r.insert(r,1)
r.insert(r,4)


obj1 = HBT(r)
obj1.hbt(r)
if obj1.balanced:
    print('tree is balanced')
else:
    print('tree is not balanced')

