
class Node: 
	def __init__(self,key): 
		self.left = None
		self.right = None
		self.val = key
		
def insert(root,parent,key):
    if root.val==parent:
        if root.left==None:
            root.left=Node(key)
            #print(key)
        else:
            root.right=Node(key)
    elif root.left!=None:
        insert(root.left,parent,key)
    elif root.right!=None:
        insert(root.right,parent,key)
        
def pri(root):
    if root!=None:
        print(root.val)
        pri(root.left)
        pri(root.right)
n,k=map(int,input().split())
A=list(map(int,input().split()))
par=list(map(int,input().split()))
root=Node(A[0])
for i in range(0,n-1):
    insert(root,par[i],A[i+1])
pri(root)
