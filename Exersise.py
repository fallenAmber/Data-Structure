class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data



    """def showNode(self):
        if self.left:
            self.left.showNode()
        print(self.data)
        if self.right:
            self.right.showNode()"""

    def inorderTraversal(self, root):
        Traversed_list = []
        if root:
            Traversed_list=Traversed_list+self.inorderTraversal(root.left)
            Traversed_list.append(root.data)
            Traversed_list= Traversed_list+self.inorderTraversal(root.right)
        return Traversed_list

    def PreorderTraversal(self, root):
        Traversed_list=[]
        if root:
            Traversed_list.append(root.data)
            Traversed_list= Traversed_list+ self.PreorderTraversal(root.left)
            Traversed_list= Traversed_list+self.PreorderTraversal(root.right)
        return Traversed_list


    def PostorderTraversal(self, root):
        Traversed_list=[]
        if root:
            Traversed_list= Traversed_list+self.PostorderTraversal(root.left)
            Traversed_list= Traversed_list+self.PostorderTraversal(root.right)
            Traversed_list.append(root.data)
        return Traversed_list

    def FindNode(self,node):
        if node < self.data:
            if self.left is None:
                return str(node) +" Is not Found"
            else:
                return self.left.FindNode(node)

        elif node > self.data:
            if self.right is None:
                return str(node) + " Is not Found"
            else:
                return self.right.FindNode(node)
        else:
            return str(node)+" Is found"


    def insertNode(self,node):
        p=[]
        if self.data is None:
            return p.append(self.data)
        elif node > self.data:
            if self.right is None:
                return p.append(node)
            else:
                self.right.insertNode(node)
        else:
            if self.left is None:
                return p.append(node)
            else:
                self.left.insertNode(node)



root=Node(int(input('Would ye mind declaring the parent node?')))
print('Elements of the Tree: ')
for i in range(3):
    root.insert(int(input()))
print("The Nodes of the tree as follows-")
print(root.PostorderTraversal(root))
print('Put the Node to be Searched: ')
#root.FindNode("10")
print(root.FindNode(int(input())))
"""print('inserting a Node')

print(root.insertNode(int(input())))
print('after the insertion:')

print(root.PreorderTraversal(root))
#root = Node(int(input('Enter the parent Node:')))
#tree_in=int(int(input('The three will be consisted of:')))
#print("We\'re taking 8 values for creating a tree:")"""
"""for p in range(6):
    root.insert(int(input(p)))
#print(root.inorderTraversal(root))
#print("Here\'s the preOrder traversed tree:")
#print("Here\'s the inOrder traversed tree:")
print("Here\'s the PreOrder traversed tree:")
print(root.PreorderTraversal(root))"""
#bt.showNode(8))
"""bt=Node(1)
bt.left=Node(7)
bt.right=Node(9)
bt.left.left=Node(1)
bt.left.right=Node(6)
bt.left.left.left=Node(5)
bt.left.left.right=Node(10)
bt.right.right=Node(8)
bt.right.right.left=Node(3)
bt.right.right.right=Node(4)
print(bt.inorderTraversal(bt))"""
#bt.showNode()
