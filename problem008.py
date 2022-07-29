# ranks update Sunday night I guess
# 699,408
# 31 medium, 65.8%

# actually good metrics, but not obviously a hard problem
# just tedious to figure out exactly what the format is
# 41ms, 83.59%, 13.9Mb, 79.54%
class Solution:
    def myAtoi(self, s: str) -> int:
        
        def overflow_checker(digitArray, neg):
            if len(digitArray) > 10: return True
            if len(digitArray) < 10: return False
            
            #two_to_the_31_array = [int(ch) for ch in str(2**31)]
            if neg:
                two_to_the_31_array = [2, 1, 4, 7, 4, 8, 3, 6, 4, 8]
            else:
                two_to_the_31_array = [2, 1, 4, 7, 4, 8, 3, 6, 4, 7]
            
            for x, y in zip(digitArray,two_to_the_31_array):
                if x > y: return True
                if x < y: return False
            
            return False
        
        l, index, digitArray, neg = len(s), 0, [], False
        
        if l == 0 : return 0
        
        while index < l and s[index] == ' ':
            index += 1
        
        if index == l: return 0
        
        if s[index] == "+" or s[index] == "-":
            if s[index] == "-": neg = True
            index += 1
        
        while index < l and s[index] == '0':
            index += 1
        
        if index == l: return 0
        
        char2Num = {str(i):i for i in range(10)}
        
        while index < l and s[index] in char2Num:
            digitArray.append( char2Num[ s[index] ] )
            index +=1
        
        if len(digitArray) == 0: return 0
        
        if overflow_checker(digitArray,neg):
            if neg:
                return -2147483648
            return 2147483647
        
        i, n = 1, 0
        while digitArray:
            num = digitArray.pop()
            n += num*i
            i *= 10
        
        if neg:
            n *= -1
        
        return n