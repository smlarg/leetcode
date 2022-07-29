#1530ms, 69.65%, there are answers at around 1200 but they seem to (mostly) be the same but with a result array declared
# which in the real world won't speed anything up, so whatever
# (there's also a way to go backwards, but I don't think it's faster, but maybe)
# 24.5Mb, 93.06%

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack:
                if temperatures[stack[-1]] < temp:
                    previousDate = stack.pop()
                    temperatures[previousDate] = i - previousDate
                else:
                    break
            stack.append(i)
        
        
        while stack:
            hottestDay = stack.pop()
            temperatures[hottestDay] = 0
        
        
        return temperatures