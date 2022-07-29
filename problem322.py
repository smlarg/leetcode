# Rank 1,029,876
# 19 medium, 56.0%`


# hmm, works, but twice the median runtime and storage
# 4031ms, 5.07%, 25.6Mb, 18.69%
class Solution:
    def __init__(self):
        self.known_bests = {0:0} # hacky, but
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        
        for coin in coins:
            self.known_bests[coin] = 1
        
        return self.coinChange2(coins, amount)
    
    
    def coinChange2(self, coins: List[int], amount: int) -> int:
        if amount in self.known_bests:
            return self.known_bests[amount]
        
        if amount < coins[0]:
            self.known_bests[amount] = -1
            return -1
        
        m = amount//coins[0] + 1
        mm = -1
        for coin in coins:
            mmm = self.coinChange2(coins, amount-coin)
            if mmm > 0: m = min(m, mmm)
            mm = max(mm,mmm)
        if mm == -1:
            self.known_bests[amount] = -1
            return -1
        self.known_bests[amount] = m + 1
        return m+1


# well a small change helped at least a bit
# 2448ms, 34.53%, memory no better though
class Solution:
    def __init__(self):
        self.known_bests = {0:0} # hacky, but
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        for coin in coins:
            self.known_bests[coin] = 1
        
        return self.coinChange2(coins, amount)
    
    
    def coinChange2(self, coins: List[int], amount: int) -> int:
        if amount in self.known_bests:
            return self.known_bests[amount]
        
        if amount < 0:
            self.known_bests[amount] = -1
            return -1
        
        m = amount 1
        mm = -1
        for coin in coins:
            mmm = self.coinChange2(coins, amount-coin)
            if mmm > 0: m = min(m, mmm)
            mm = max(mm,mmm)
        if mm == -1:
            self.known_bests[amount] = -1
            return -1
        self.known_bests[amount] = m + 1
        return m+1


# oh. right.
# I had to read other solutions to figure this out, but
# we could use an array as a 'memo'

# yeah. duh. sorry.
# 1547ms, 81.59%
# memory now fine

# and you know what though honestly, I think the above way really was better
# this way is quicker *per cycle*, but if the coins were large numbers this way could have more cycles
# so I'm okay here
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        known_bests = [amount+1]*(amount+1)
        
        known_bests[0] = 0
        for i in range(1,amount+1):
            m = amount+1
            for coin in coins:
                if coin <= i:
                    m = min(m, known_bests[i-coin] + 1)
            known_bests[i] = m
        
        if known_bests[amount] == amount+1 : return -1
        return known_bests[amount]
        
                    
        