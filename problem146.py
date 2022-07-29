# Oh! Rank updated! But not by much!
# Rank 597,741
# I don't think I'm planning on breaking hald a million anymore....


# with a queue of unbounded size, so that's not a very good idea
# yeup, okay
# 1191ms, 59.07% so fine,
# 80.2Mb, 10.75%, oh well actually most are above 75Mb? huh

# A doubly-linked list is the more-right way to do this, but my parents are in town so I'm resisting the urge to do that too
class LRUCache:
    
    def __init__(self, capacity: int):
        from collections import deque
        
        self.valueKeyTimeArray     = [[-1,-1,-1] for _ in range(capacity)]
        self.touchOrder = deque() # (index, time)
        self.keysToIndex = {}
        
        self.time = 0
        self.fullness = 0
    
    def get(self, key: int) -> int:
        if key in self.keysToIndex:
            self.valueKeyTimeArray[self.keysToIndex[key]][2] = self.time
            self.touchOrder.append((self.keysToIndex[key],self.time))
            self.time += 1
            return self.valueKeyTimeArray[self.keysToIndex[key]][0]
        else:
            return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.keysToIndex:
            
            self.valueKeyTimeArray[self.keysToIndex[key]] = [value,key,self.time]
            self.touchOrder.append((self.keysToIndex[key],self.time))
            self.time += 1
        
        elif self.fullness < len(self.valueKeyTimeArray):
            self.valueKeyTimeArray[self.fullness] = [value, key, self.time]
            self.keysToIndex[key] = self.fullness
            self.touchOrder.append((self.fullness, self.time))
            self.time += 1
            self.fullness +=1
        
        else:
            while True:
                index, oldestTime = self.touchOrder.popleft()
                
                if oldestTime == self.valueKeyTimeArray[index][2]:
                    oldkey = self.valueKeyTimeArray[index][1]
                    self.valueKeyTimeArray[index] = [value, key, self.time]
                    self.touchOrder.append((index, self.time))
                    self.time += 1
                    self.keysToIndex.pop(oldkey)
                    self.keysToIndex[key] = index
                    return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)