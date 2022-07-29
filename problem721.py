#28 medium, 63.8%

accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],\
 ["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]


# the right answer is a linked list. sorry.
# (only every time you search the linked list, all the pointers update to the last item, so it's O(1) to find the root)
# (amortized I guess? )
# this is a pretty clean example
# https://leetcode.com/problems/accounts-merge/discuss/2257442/Python-Clean-Easy-Union-Find-Solution
#
# oh actually, this is exactly union find isn't it?
# https://www.geeksforgeeks.org/union-find/


# it does work, but very bad metrics
# 994ms, 7.51%, 3 times the median
# 25.3Mb, 9.81%, 125% of the median, 150% of the right answer
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        import heapq

        email2account = {}
        mergeDict = {}
        for i, a in enumerate(accounts):
            for email in a[1:]:
                if email in email2account:
                    j = email2account[email]
                    mergeSet = mergeDict.get(i,set([i])).union(mergeDict.get(j,set([j])))
                    for k in mergeSet:
                        mergeDict[k] = mergeSet
                else:
                    email2account[email] = i

        mergeDict = list(set([tuple(item) for item in mergeDict.values()]))

        skipHeap = []

        while mergeDict:
            merge = mergeDict.pop()
            keeper = merge[0]
            others = list(merge[1:])
            newEmails = set(accounts[keeper][1:])
            for other in others:
                newEmails.update(accounts[other][1:])
                heapq.heappush(skipHeap,other)
            accounts[keeper] = [ accounts[keeper][0] ] + list(newEmails)
            
        heapq.heappush(skipHeap,len(accounts))
        skip = heapq.heappop(skipHeap)
        result = []

        for i,a in enumerate(accounts):
            if i == skip:
                skip = heapq.heappop(skipHeap)
                continue
            else:
                a = [a[0]] + sorted(a[1:])
                result.append(a)

        return result


#33% faster to not edit the orignal list, which okay right that makes sense
# 632ms,11.51%, still double the median

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        import heapq

        email2account = {}
        mergeDict = {}
        for i, a in enumerate(accounts):
            for email in a[1:]:
                if email in email2account:
                    j = email2account[email]
                    mergeSet = mergeDict.get(i,set([i])).union(mergeDict.get(j,set([j])))
                    for k in mergeSet:
                        mergeDict[k] = mergeSet
                else:
                    email2account[email] = i

        mergeDict = list(set([tuple(item) for item in mergeDict.values()]))

        skipHeap = []
        
        result = []
        while mergeDict:
            merge = mergeDict.pop()
            newEmails = set()
            for id in merge:
                newEmails.update(accounts[id][1:])
                heapq.heappush(skipHeap,id)
            result.append([ accounts[id][0] ] + sorted(list(newEmails)))
            
        heapq.heappush(skipHeap,len(accounts))
        skip = heapq.heappop(skipHeap)

        for i,a in enumerate(accounts):
            if i == skip:
                skip = heapq.heappop(skipHeap)
                continue
            else:
                a = [a[0]] + sorted(a[1:])
                result.append(a)

        return result


# and just a little better still
#562ms, 13.74%
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        import heapq

        email2account = {}
        mergeDict = {i:set([i]) for i in range(len(accounts))}
        for i, a in enumerate(accounts):
            for email in a[1:]:
                if email in email2account:
                    j = email2account[email]
                    mergeSet = mergeDict.get(i,set([i])).union(mergeDict.get(j,set([j])))
                    for k in mergeSet:
                        mergeDict[k] = mergeSet
                else:
                    email2account[email] = i

        mergeDict = list(set([tuple(item) for item in mergeDict.values()]))

        skipHeap = []
        
        result = []
        while mergeDict:
            merge = mergeDict.pop()
            newEmails = set()
            for id in merge:
                newEmails.update(accounts[id][1:])
                heapq.heappush(skipHeap,id)
            result.append([ accounts[id][0] ] + sorted(list(newEmails)))
        
        return result