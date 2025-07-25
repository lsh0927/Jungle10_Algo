import sys,math
input= sys.stdin.readline

N=int(input())

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

nodes={}

def cal_node(char):
    if char=='.':
        return None
    
    if char not in nodes:
        nodes[char]= TreeNode(char)
    return nodes[char]


for _ in range(N):
    p,l,r= input().split()

    p_node= cal_node(p)
    p_node.left= cal_node(l)
    p_node.right= cal_node(r)


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