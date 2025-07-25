import sys
sys.setrecursionlimit(10 ** 6)
node = [int(readline.rstrip()) for readline in sys.stdin]

def postorder(root_idx,end_idx):
    if root_idx > end_idx:
        return
    
    root=node[root_idx]
    start_idx=root_idx+1

    while start_idx<=end_idx:
        if root< node[start_idx]:
            break
        start_idx+=1

    
    postorder(root_idx+1, start_idx-1)
    postorder(start_idx, end_idx)
    print(root)

postorder(0,len(node)-1)