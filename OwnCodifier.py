import numpy as np

class OwnCodifier:
    def __init__(self):
        pass

    def codify(self, data):
        codeword = [0] * 9

        # Preencher os bits de dados na palavra-código
        codeword[0] = data[0]
        codeword[1] = data[1]
        codeword[2] = data[2]
        codeword[3] = data[3]
        codeword[4] = data[4]

        # Calcular os bits de paridade
        xor_sum1 = data[0] ^ data[1] ^ data[2]
        xor_sum2 = data[1] ^ data[2] ^ data[3]
        xor_sum3 = data[2] ^ data[3] ^ data[4]
        codeword[5] = xor_sum1
        codeword[6] = xor_sum2
        codeword[7] = xor_sum3
        codeword[8] = xor_sum1 ^ xor_sum2 ^ xor_sum3

        return codeword