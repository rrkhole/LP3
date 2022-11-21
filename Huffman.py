import heapq

class node:
    def __init__(self,freq,symbol,left=None,right=None):
        self.freq=freq 
        self.symbol=symbol 
        self.left=left 
        self.right=right 
        self.huff=''

    def __lt__(self,nxt):
        return self.freq<nxt.freq 

chars= ['a','b','c','d','e','f']
freq=[5, 9, 12, 13, 16, 45]

nodes=[]

def printNodes(Node,val=''):
    newVal=val+str(Node.huff)
    if(Node.left):
        printNodes(Node.left,newVal)
    if(Node.right):
        printNodes(Node.right,newVal)
    if(not Node.left and not Node.right):
        print(f"{Node.symbol}->{newVal}")

for i in range(len(chars)):
    newNode=node(freq[i],chars[i])
    heapq.heappush(nodes,newNode)

while(len(nodes))>1:
    left=heapq.heappop(nodes)
    right=heapq.heappop(nodes)
    left.huff=0 
    right.huff=1 
    newNode=node(left.freq+right.freq,left.symbol+right.symbol,left,right)
    #print(newNode.left.symbol)
    heapq.heappush(nodes,newNode) 

printNodes(nodes[0])
        
