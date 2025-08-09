import sys
sys.setrecursionlimit(10**6)
input_lines = [int(line.strip()) for line in sys.stdin]


class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def build_Tree(preorder):
    if not preorder:
        return None
    
    def build(min_val, max_val):
        nonlocal idx
        if idx>=len(preorder):
            return None

        val= preorder[idx]
        if val<min_val or val> max_val:
            return None
        
        idx+=1
        root= TreeNode(val)
        root.left=build(min_val,val)
        root.right=build(val,max_val)
        return root
    
    idx=0
    return build(float('-inf'),float('inf'))

def postorder(root):
    if root:
        postorder(root.left)          
        postorder(root.right)
        print(root.val)

root= build_Tree(input_lines)
print(root)

