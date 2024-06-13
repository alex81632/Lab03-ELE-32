import numpy as np
import random

class VNode:
    def __init__(self, index):
        self.index = index
        self.edges = []
        self.value = 0
    
    def __str__(self):
        return str(self.index)

class CNode:
    def __init__(self, index):
        self.index = index
        self.edges = []

    def __str__(self):
        return str(self.index)
    
class Edge:
    def __init__(self, cnode, vnode):
        self.cnode = cnode
        self.vnode = vnode
        self.val = 0
       
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
        # np.savetxt("H.txt", self.H, fmt='%d')

    def cols_to_rows(self, h):
        h2 = []
        for i in range(len(h[0])):
            h1 = []
            for j in range(len(h)):
                h1.append(h[j][i])
            h2.append(h1)
        return h2

    def generateLDPCCode(self):
        h = self.M//self.dv
        h1 = []
        for i in range(self.N):
            v1 = [0]*h
            v1[i//self.dc] = 1
            h1.append(v1)

        for i in range(self.dv):
            ht = self.cols_to_rows(h1)
            for elem in ht:
                self.H.append(elem)
            # shuffle h collumns
            random.shuffle(h1)
        
        for i in range(self.N):
            for j in range(self.M):
                if(self.H[j][i] == 1):
                    edge = Edge(self.CNodes[j], self.VNodes[i])
                    self.CNodes[j].edges.append(edge)
                    self.VNodes[i].edges.append(edge)

class CanalGauss:
    def __init__(self, eb_n0):
        self.sigma2 = 1/(2*eb_n0)
        self.max_iter = 50
    
    def canal(self, v):
        r = []
        for i in range(len(v)):
            if(v[i] == 0):
                v[i] = 1
            else:
                v[i] = -1
            r.append(v[i] + np.random.normal(0, np.sqrt(self.sigma2)))            
        return r
    
    def LLR(self, r):
        L = []
        for i in range(len(r)):
            L.append(2*r[i]/self.sigma2)
        return L

    def beliefPropagation(self, L, Vnodes, Cnodes):
        
        for v in Vnodes:
            for e in v.edges:
                e.val = 0
        for i in range(len(L)):
            Vnodes[i].value = L[i]

        for _ in range(self.max_iter):

            # Vnodes belief propagation
            for vnode in Vnodes:
                sum = vnode.value
                for edge in vnode.edges:
                    sum += edge.val
                for edge in vnode.edges:
                    edge.val = sum - edge.val
                # print(sum)

            # Stop condition
            if(self.stopCondition(Cnodes)):
                break

            # Cnodes belief propagation
            for cnode in Cnodes:
                min = np.Inf
                second_min = np.Inf
                prod = 1
                for edge in cnode.edges:
                    prod *= edge.val
                    if abs(edge.val) <= min:
                        second_min = min
                        min = abs(edge.val)
                    elif abs(edge.val) < second_min:
                        second_min = abs(edge.val)
                # print(min, second_min, prod)

                for edge in cnode.edges:
                    if abs(edge.val) == min:
                        edge.val = np.sign(prod * edge.val) * second_min
                    else:
                        edge.val = np.sign(prod *edge.val) * min

        # Decode
        r = []
        for vnode in Vnodes:
            sum = vnode.value
            for edge in vnode.edges:
                sum += edge.val
            r.append(0 if sum >= 0 else 1)

        return r
    
    def stopCondition(self, Cnodes):
        allPositive = True
        for cnode in Cnodes:
            prod = 1
            for edge in cnode.edges:
                prod *= edge.val
            if(prod < 0):
                allPositive = False
                break

        return allPositive

if __name__ == "__main__":
    N = 99
    dv = 6
    dc = 9
    d = LDPC(N, dv, dc)
