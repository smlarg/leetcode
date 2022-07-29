# wow. I was worrying about this way too much,
# first shot out of the box, with all my conservative checks because I get confused by even and odd:
# 201ms, 97.12% !!!!, memory 1% above the median
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def checkOddPalidromeAtPivot(pivot,s):
            # will return 1 even if pivot is invalid, so, don't pass an invalid pivot
            
            l, length, n = len(s), 1, 1
            while pivot - n >= 0 and pivot + n < l:
                if s[pivot - n] == s[pivot + n]:
                    length +=2
                    n +=1
                else:
                    break
            return length
        
        def checkEvenPalidromeAtPivot(pivot,s):
            l, length, n = len(s), 0, 0
            while pivot - n - 1 >= 0 and pivot + n < l:
                if s[pivot - n - 1] == s[pivot + n]:
                    length +=2
                    n +=1
                else:
                    break
            return length
        
        l = len(s)
        
        center = l//2
        
        result_pivot = center
        result_length = 1
        
        i = 1
        while center + i//2 < l:
            # +0, -1, +1, -2, +2, etc.
            
            # move iterator up
            pivot = center + i//2
            # check odd
            current_palindrome_length = checkOddPalidromeAtPivot(pivot,s)
            if current_palindrome_length > result_length:
                result_length, result_pivot = current_palindrome_length, pivot
            #check even
            current_palindrome_length = checkEvenPalidromeAtPivot(pivot,s)
            if current_palindrome_length > result_length:
                result_length, result_pivot = current_palindrome_length, pivot
            
            # move iterator down
            i += 1 
            if center - i//2 >= 0:
                pivot =  center - i//2
                current_palindrome_length = checkOddPalidromeAtPivot(pivot,s)
                if current_palindrome_length > result_length:
                    result_length, result_pivot = current_palindrome_length, pivot
                current_palindrome_length = checkEvenPalidromeAtPivot(pivot,s)
                if current_palindrome_length > result_length:
                    result_length, result_pivot = current_palindrome_length, pivot
            
            i += 1
            
            max_possible_unfound = (center - i//2)*2 + 3 # three is wrong, but safe
            if result_length > max_possible_unfound: break
        
        if result_length%2:
            # ey ey ey
            result = s[result_pivot- result_length//2: result_pivot + result_length//2+1]
        else:
            result = s[result_pivot- result_length//2: result_pivot + result_length//2]
        
        return result
        