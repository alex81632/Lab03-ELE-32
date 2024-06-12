import numpy as np

class HammingDecodifier:
    def __init__(self):
        self.HT = [[1,1,1],
                   [1,0,1],
                   [1,1,0],
                   [0,1,1],
                   [1,0,0],
                   [0,1,0],
                   [0,0,1]]

    def decodify(self, r):
        self.s = np.matmul(r, self.HT)
        for i in range(len(self.s)):
            if self.s[i] % 2 == 0:
                self.s[i] = 0
            else:
                self.s[i] = 1
        
        for i in range(len(self.HT)):
            if((self.s == self.HT[i]).all()):
                r[i] = (r[i]+1)%2
                break

        return r