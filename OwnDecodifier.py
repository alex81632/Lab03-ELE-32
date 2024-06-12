
class OwnDecodifier:
    def __init__(self):
        pass

    def decodify(self, codeword):
        xor_sum1 = codeword[0] ^ codeword[1] ^ codeword[2]
        xor_sum2 = codeword[1] ^ codeword[2] ^ codeword[3]
        xor_sum3 = codeword[2] ^ codeword[3] ^ codeword[4]
        xor_sum4 = codeword[5] ^ codeword[6] ^ codeword[7]

        if(xor_sum1 == codeword[5] and xor_sum2 == codeword[6] and xor_sum3 == codeword[7] and xor_sum4 == codeword[8]):
            return codeword
    
        if(xor_sum4 != codeword[8]):
            codeword[5] = codeword[0] ^ codeword[1] ^ codeword[2]
            codeword[6] = codeword[1] ^ codeword[2] ^ codeword[3]
            codeword[7] = codeword[2] ^ codeword[3] ^ codeword[4]
            codeword[8] = codeword[5] ^ codeword[6] ^ codeword[7]
        
        match (xor_sum1 == codeword[5], xor_sum2 == codeword[6], xor_sum3 == codeword[7]):
            case (False, True, True):
                # bit 0 errado
                codeword[0] = codeword[0] ^ 1
            case (False, False, True):
                # bit 1 errado
                codeword[1] = codeword[1] ^ 1
            case (False, False, False):
                # bit 2 errado
                codeword[2] = codeword[2] ^ 1
            case (True, False, False):
                # bit 3 errado
                codeword[3] = codeword[3] ^ 1
            case (True, True, False):
                # bit 4 errado
                codeword[4] = codeword[4] ^ 1

        return codeword
