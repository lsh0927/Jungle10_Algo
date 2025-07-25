import sys,math
input= sys.stdin.readline

N=int(input())

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
 
nodes={}


def make_Tree(val):
    if val=='.':
        return None
    
    
    if val not in nodes:
        nodes[val]= TreeNode(val)
    return nodes[val]


for _ in range(N):
    root, left, right= input().split()
    node= make_Tree(root)
    node.left=make_Tree(left)
    node.right=make_Tree(right)


def preorder(node):
    if node==None:
        return
    
    print(node.val, end='')
    preorder(node.left)
    preorder(node.right)

def postorder(node):
    if node==None:
        return
    
    postorder(node.left)
    postorder(node.right)
    print(node.val, end='')

def inorder(node):
    if node==None:
        return
    
    inorder(node.left)
    print(node.val, end='')
    inorder(node.right)


preorder(nodes['A'])
print()
inorder(nodes['A'])
print()
postorder(nodes['A'])