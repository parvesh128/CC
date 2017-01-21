# Enter your code here. Read input from STDIN. Print output to STDOUT

class TreeNode:
    
    def __init__(self, val):
        self.val = val
        self.child = []
        self.nodesPerChild = []
        
    def addChild(self, childNode):
        self.child.append(childNode)
        self.nodesPerChild.append(0)
        
        
    def populateNumChildren(self):
        
        numChildren = 0
        
        for idx,child in enumerate(self.child):
            self.nodesPerChild[idx] = 1 + child.populateNumChildren()
            numChildren += self.nodesPerChild[idx]
            
        return numChildren
    
    def getNumEdgesToRemove(self):
        
        numEdges = 0
        
        for idx,c in enumerate(self.child):
            nodesPerChild = self.nodesPerChild[idx]
            
            if nodesPerChild == 0:
                continue
            
            if nodesPerChild % 2 == 0:
                numEdges += 1
                
            numEdges += c.getNumEdgesToRemove()
            
        return numEdges
            
class Tree:
    
    def __init__(self, numNodes, edges):
        self.nodeMap = {}
        
        for node in range(1, numNodes + 1):
            self.nodeMap[node] = TreeNode(node)
            
        for edge in edges:
            child, parent = edge
            self.nodeMap[parent].addChild(self.nodeMap[child])
            
        self.root = self.nodeMap[1]
        
        numChild = self.root.populateNumChildren()
        
        #for idx, numChild in enumerate(self.root.nodesPerChild):
        #    print self.root.child[idx].val, numChild
            
    def getNumEdgesToRemove(self):
        return self.root.getNumEdgesToRemove()
        
        
        
if __name__ == '__main__':
    numNodes, numEdges = map(int, raw_input().split())
    
    edges = [None for x in range(numEdges)]
    
    
    for x in range(numEdges):
        edges[x] = map(int, raw_input().split())
        
    tree = Tree(numNodes, edges)
    
    print tree.getNumEdgesToRemove()
    
    
        
        
        
