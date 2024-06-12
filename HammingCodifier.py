import numpy as np

class HammingCodifier:
    def __init__(self):
        self.G =[[1, 0, 0, 0, 1, 1, 1],
                 [0, 1, 0, 0, 1, 0, 1],
                 [0, 0, 1, 0, 1, 1, 0],
                 [0, 0, 0, 1, 0, 1, 1]]

    def codify(self, u):
        val = np.matmul(u, self.G)
        for i in range(len(val)):
            if val[i] % 2 == 0:
                val[i] = 0
            else:
                val[i] = 1
        return val