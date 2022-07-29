# Rank just will not change
# 2 hard, 20.3%

# from the forums, a simpler solution (or at least code) is:
# keep a count of *every* number (using something called collections.Counter() )
# start the count for the needed letters off negative,
# so when you add them it goes up to zero
# have a variable which keeps track of how many zeros you have, and increiment it when a count changes sign
# ( basically just like my third, ugliest solution below)
# (but *only* the orignially needed leters can go negative, so it's fine to treat all letters the same)
# and *don't* bother to slide the window; just slide the front pointer till you're good,
# then the back pointer till you're bad, then repeat
# *but* keep track of the size of the smallest interval you've found
# the added complexity of keeping track of this (a single min statement, essentially)
# is more than made up for by not needing the 'width' variable, and having just two nested loops (one for, one while)

# actually, let me also just link to it, I want to remember this
# https://leetcode.com/problems/minimum-window-substring/discuss/26804/12-lines-Python

# also, obvious now that I see it: enumerate(thing, n) enumerates thing starting at n


s = "ADOBECODEBANC"
t = "ABC"

s = 'ttWtXaaacYoZooburritoXtaco'
t = 'taco'


# works, but terrible everything
# 10x time, and 2x memory
# hmm. hmmmmmmm.
# oh. numpy. right.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == '': return ''
        
        import numpy as np
        
        
        # why on earth did I think having an dict *and* an array was clever???!?
        # It is not clever!!!
        chars_to_ints = {}
        char_counts = []
        for ch in t:
            if ch in chars_to_ints:
                char_counts[chars_to_ints[ch]] +=1
            else:
                chars_to_ints[ch] = len(char_counts)
                char_counts.append(1)
        
        char_counts = tuple(char_counts) # I was accidentally writing to this; don't do that!
        
        sub_string_counts = np.zeros(len(char_counts), dtype = np.int32)
        # find the shortest leading string
        for j,ch in enumerate(s):
            if ch in chars_to_ints:
                sub_string_counts[chars_to_ints[ch]] += 1
                if (sub_string_counts >= char_counts).all():
                    j += 1 # This was, I now believe, really really dumb
                    break
        
        if j == len(s)-1 and not (sub_string_counts >= char_counts).all(): return ""
        
        #Remove anything unneeded from the front
        # There might be a way to refactor the next loop and eliminate this one
        # but as it is now, the next loop won't trigger in the case that there's no more advancing to do
        for i, ch in enumerate(s):
            if ch in chars_to_ints:
                sub_string_counts[chars_to_ints[ch]] -= 1
                if not (sub_string_counts >= char_counts).all():
                    sub_string_counts[chars_to_ints[ch]] +=1
                    break
        
        width = j-i
        result_tuple = (j- width,j)
        
        for k in range(j,len(s)):
            # move forward one in front and back
            if s[k] in chars_to_ints:
                sub_string_counts[chars_to_ints[s[k]]] +=1
                
            if s[k - width] in chars_to_ints:
                sub_string_counts[chars_to_ints[s[k-width]]] -=1
            
            # if you're still good, try shortening from the back
            if (sub_string_counts >= char_counts).all():
                while (sub_string_counts >= char_counts).all():
                    result_tuple = (k-width+1,k+1)
                    width -=1
                    if s[k-width] in chars_to_ints:
                        sub_string_counts[chars_to_ints[s[k-width]]] -=1
                sub_string_counts[chars_to_ints[s[k-width]]] +=1
                width += 1
        
        return s[result_tuple[0]:result_tuple[1]]


#yes, a factor of 2 better on memory (now fine) and 5 on speed
# speed is still about 2-2.5x too slow though
class Solution:
    def minWindowNoNumpy(self, s: str, t: str) -> str:
        
        if t == '': return ''
                
        chars_to_ints = {}
        char_counts = []
        for ch in t:
            if ch in chars_to_ints:
                char_counts[chars_to_ints[ch]] +=1
            else:
                chars_to_ints[ch] = len(char_counts)
                char_counts.append(1)
        
        char_counts = tuple(char_counts) # I was accidentally writing to this; don't do that!
        
        sub_string_counts = [0]*len(char_counts)
        # find the shortest leading string
        for j,ch in enumerate(s):
            if ch in chars_to_ints:
                sub_string_counts[chars_to_ints[ch]] += 1
                if all( [ x >= y for x, y in zip(sub_string_counts,char_counts)] ):
                    j += 1 # This was, I now believe, really really dumb
                    break
        
        if j == len(s)-1 and not all( [ x >= y for x, y in zip(sub_string_counts,char_counts)] ): return ""
        
        #Remove anything unneeded from the front
        # There might be a way to refactor the next loop and eliminate this one
        # but as it is now, the next loop won't trigger in the case that there's no more advancing to do
        for i, ch in enumerate(s):
            if ch in chars_to_ints:
                sub_string_counts[chars_to_ints[ch]] -= 1
                if not all( [ x >= y for x, y in zip(sub_string_counts,char_counts)] ):
                    sub_string_counts[chars_to_ints[ch]] +=1
                    break
        
        width = j-i
        result_tuple = (j- width,j)
        
        for k in range(j,len(s)):
            # move forward one in front and back
            if s[k] in chars_to_ints:
                sub_string_counts[chars_to_ints[s[k]]] +=1
                
            if s[k - width] in chars_to_ints:
                sub_string_counts[chars_to_ints[s[k-width]]] -=1
            
            # if you're still good, try shortening from the back
            if all( [ x >= y for x, y in zip(sub_string_counts,char_counts)] ):
                while all( [ x >= y for x, y in zip(sub_string_counts,char_counts)] ):
                    result_tuple = (k-width+1,k+1)
                    width -=1
                    if s[k-width] in chars_to_ints:
                        sub_string_counts[chars_to_ints[s[k-width]]] -=1
                sub_string_counts[chars_to_ints[s[k-width]]] +=1
                width += 1
        
        return s[result_tuple[0]:result_tuple[1]]


# hmm. only about 20% faster, 210ms, 33.82%
# I think maybe oh well
class Solution:
    def minWindowRemoveAllCall(self, s: str, t: str) -> str:
        
        if t == '': return ''
                
        chars_to_ints = {}
        char_counts = []
        for ch in t:
            if ch in chars_to_ints:
                char_counts[chars_to_ints[ch]] +=1
            else:
                chars_to_ints[ch] = len(char_counts)
                char_counts.append(1)
        
        char_counts = tuple(char_counts) # I was accidentally writing to this; don't do that!
        
        l = len(char_counts)
        
        sub_string_counts = [0]*l
        
        constraints_satisfied = 0
        
        # find the shortest leading string
        for j,ch in enumerate(s):
            if ch in chars_to_ints:
                sub_string_counts[chars_to_ints[ch]] += 1
                if sub_string_counts[chars_to_ints[ch]]  - char_counts[chars_to_ints[ch]] ==0:
                    constraints_satisfied +=1
                
                if constraints_satisfied == l :
                    j += 1 # This was, I now believe, really really dumb
                    break
        
        if j == len(s)-1 and not all( [ x >= y for x, y in zip(sub_string_counts,char_counts)] ): return ""
        
        #Remove anything unneeded from the front
        # There might be a way to refactor the next loop and eliminate this one
        # but as it is now, the next loop won't trigger in the case that there's no more advancing to do
        for i, ch in enumerate(s):
            if ch in chars_to_ints:
                sub_string_counts[chars_to_ints[ch]] -= 1
                if sub_string_counts[chars_to_ints[ch]]  - char_counts[chars_to_ints[ch]] == -1:
                    constraints_satisfied -=1
                if constraints_satisfied < l :
                    sub_string_counts[chars_to_ints[ch]] +=1
                    constraints_satisfied +=1
                    break
        
        width = j-i
        result_tuple = (j- width,j)
        
        for k in range(j,len(s)):
            # move forward one in front and back
            if s[k] in chars_to_ints:
                sub_string_counts[chars_to_ints[s[k]]] +=1
                if sub_string_counts[chars_to_ints[s[k]]]  - char_counts[chars_to_ints[s[k]]] ==0:
                    constraints_satisfied +=1
                
                
            if s[k - width] in chars_to_ints:
                sub_string_counts[chars_to_ints[s[k-width]]] -=1
                if sub_string_counts[chars_to_ints[s[k-width]]]  - char_counts[chars_to_ints[s[k-width]]] == -1:
                    constraints_satisfied -= 1
            
            # if you're still good, try shortening from the back
            if constraints_satisfied == l:
                while constraints_satisfied == l:
                    result_tuple = (k-width+1,k+1)
                    width -=1
                    if s[k-width] in chars_to_ints:
                        sub_string_counts[chars_to_ints[s[k-width]]] -=1
                        if sub_string_counts[chars_to_ints[s[k-width]]]  - char_counts[chars_to_ints[s[k-width]]] == -1:
                            constraints_satisfied -= 1
                        
                sub_string_counts[chars_to_ints[s[k-width]]] +=1
                width += 1
                constraints_satisfied +=1
        
        return s[result_tuple[0]:result_tuple[1]]   
        