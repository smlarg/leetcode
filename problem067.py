class Solution:
    # 34ms, 93.18%, good enough
    def addBinary(self, a: str, b: str) -> str:
        #pythonic way
        return bin( int(a,2) + int(b,2))[2:]
    
    #loopy way
    #...no, too tedious and ineffient with python string opperations
            