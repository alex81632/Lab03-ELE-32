import numpy as np

class CanalBSC:
    def __init__(self, prob):
        self.prob = prob

    def canal(self, x):
        for i in range(len(x)):
            if self.prob > np.random.rand():
                if x[i] == 0:
                    x[i] = 1
                else:
                    x[i] = 0
        return x