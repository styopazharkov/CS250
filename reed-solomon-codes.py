# this file generates reed solomon codes with a given alphabet size q, length n, and dimention k
ALPHABET_SIZE = 5
LENGTH =  4
DIMENTION = 3
def print_rs_code(q,n,k):
    pass
def

class RS_CODE():
    def __init__(self, q, alpha, n, k, codewords=False):
        self.q=q
        self.alpha=alpha
        self.n = n
        self.k = k
        if codewords:
            self.codewords=self.create_codewords()


