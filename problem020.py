# top version is 38ms and >75 percentile,
# bottom is 49ms and <50 percentile
# so, uh, don't know that that's meaningful

class Solution:
    def isValid(self, s: str) -> bool:
        result = True
        a = []
        match = { "{": "}", "(": ")", "[": "]"}
        
        for c in s:
            if c in ("{", "(", "["): # this could be c in match, but the list is length 3 so....
                a.append(c)
            elif c in ("}", ")", "]"): # and technically this test could be skipped because of the problem statement, but, that's dumb
                try:
                    b = a.pop()
                except IndexError:
                    result = False
                    break
                if match[b] == c:
                    continue
                else:
                    result = False
                    break

        if len(a) != 0:
            result = False

        return result
        
    def isValid_this_is_slower_somehow???(self, s: str) -> bool:
        a = []
        match = { "{": "}", "(": ")", "[": "]"}
        
        for c in s:
            if c in ("{", "(", "["):
                a.append(c)
            elif c in ("}", ")", "]"):
                try:
                    b = a.pop()
                except IndexError:
                    return False
                if match[b] == c:
                    continue
                else:
                    return False

        if len(a) != 0:
            return False

        return True