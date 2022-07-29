class Solution:
    #97ms, 20.86%, 14.8Mb, 32.50%
    def isPalindromeStringOps(self, s: str) -> bool:
        s = "".join([ch for ch in s if ch.isalnum()]).lower()
        for i in range(len(s)//2):
            if s[i] != s[-1-i]:
                return False
        return True
    
    
    #80ms, 40.11%, 14.7Mb, 36.65%
    def isPalindromeOrd(self, s: str) -> bool:
        ar = []
        for ch in s:
            n = ord(ch)
            if n >= 48:
                if n <= 57:
                    ar.append(n)
                elif n >= 65:
                    if n <= 90:
                        ar.append(n + 32)
                    elif n >= 97:
                        if n <= 122:
                            ar.append(n)
        
        for i in range(len(ar)//2):
            if ar[i] != ar[-1-i]:
                return False
        return True