class TreeNode:
    def __init__(self,val = 0,left =None,right =None):
        self.val = val
        self.right = right
        self.left = left
def dfs(root):
    if not root:
        return
    dfs(root.left)
    print(f"value is : {root.val}")
    dfs(root.right)
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(44)
root.left.left= TreeNode(12)
root.right.right = TreeNode(1)
dfs(root)
