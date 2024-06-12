import numpy as np

class VNode:
    def __init__(self, index):
        self.index = index
        self.cnodes = []
        self.value = 0
    
    def __str__(self):
        return str(self.index)

class CNode:
    def __init__(self, index):
        self.index = index
        self.vnodes = []

    def __str__(self):
        return str(self.index)
        
class LDPC:
    def __init__(self, N, dv, dc):
        self.N = N
        self.dv = dv
        self.dc = dc
        self.M = (N*dv)//dc
        self.VNodes = [VNode(i) for i in range(self.N)]
        self.CNodes = [CNode(i) for i in range(self.M)]
        self.H = []
        self.generateLDPCCode()
        self.H = np.array(self.H)
        print(self.H)
        self.max_iter = 10
        self.iter = 0

    def generateLDPCCode(self):
        for i in range(self.N):
            for j in range(self.dv):
                possibleCNodes = self.getPossibleCNodes(i)
                if(len(possibleCNodes) == 0):
                    self.printGraph()
                    break
                randomIndex = np.random.randint(0, len(possibleCNodes))
                self.VNodes[i].cnodes.append(possibleCNodes[randomIndex])
                possibleCNodes[randomIndex].vnodes.append(self.VNodes[i])
        
        for i in range(self.M):
            line = []
            for j in range(self.N):                
                if(self.VNodes[j] in self.CNodes[i].vnodes):
                    line.append(1)
                else:
                    line.append(0)
            self.H.append(line)

    def getPossibleCNodes(self, Vindex):
        possibleCNodes = []
        for i in range(self.M):
            if(len(self.CNodes[i].vnodes) < self.dc and self.VNodes[Vindex] not in self.CNodes[i].vnodes):
                possibleCNodes.append(self.CNodes[i])
        possibleCNodes.sort(key = lambda CNode: len(CNode.vnodes))
        smallest = []
        for i in range(len(possibleCNodes)):
            if(len(possibleCNodes[i].vnodes) == len(possibleCNodes[0].vnodes)):
                smallest.append(possibleCNodes[i])
        possibleCNodes = smallest
        return possibleCNodes