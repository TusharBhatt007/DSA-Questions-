class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value 

    def insert_node(self,root,data):
        if root is None:
            return Node(data)
        else:
            if root.data > data:
                root.left = self.insert_node(root.left,data)
            elif root.data<data:
                root.right = self.insert_node(root.right , data)
            return root 

class InorderTraversal:
    def __init__(self,root):
        self.root = root
    
    def inorder_traversal(self,root):
        if root!=None:
            self.inorder_traversal(root.left)
            print(root.data)
            self.inorder_traversal(root.right)

r = Node(10)
r.insert_node(r,5)
r.insert_node(r,11)
r.insert_node(r,4)

obj1 = InorderTraversal(r)
obj1.inorder_traversal(r)

