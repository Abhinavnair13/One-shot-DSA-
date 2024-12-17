class TreeNode:
    def __init__(self,val = 0,left =None,right =None):
        self.val = val
        self.right = right
        self.left = left
def bfs(root):
    if not root:
        return None
    queue = []
    queue.append(root)
    while len(queue)>0:
        node = queue.pop(0)
        print(f"value is : {node.val}")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(44)
root.left.left= TreeNode(12)
root.right.right = TreeNode(1)
bfs(root)
