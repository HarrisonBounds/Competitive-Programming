
#Traverse the left subtree, i.e., call Inorder(left->subtree)
#Visit the root.
#Traverse the right subtree, i.e., call Inorder(right->subtree)
#RECURSION !!! 
def inorderTraversal(self, root):
   #we make a nested function so we can define res outside
    res = []
    def inorder(root):
        if root == None:
            return
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)

    inorder(root)
    return res 
        