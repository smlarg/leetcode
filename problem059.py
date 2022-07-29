# submitted

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        #result = [[0]*n]*n # this creates a list of the same n-length list n times
        #    # I'm sure there's a reason for that, but, uh, that's not what I wanted
        
        result = []
        for i in range(n):
            result.append([0]*n)
        
        
        k = 1
        i_min = 0
        j_min = 0
        i_max = n
        j_max = n
        #while (k < n**2+1):
        j = 0
        while (i_min < i_max):
            for i in range(i_min, i_max):
                result[j][i] = k
                k +=1
            j_min+=1
            for j in range(j_min, j_max):
                result[j][i] = k
                k +=1
            i_max -=1
            for i in range(i_max-1, i_min-1,-1):
                result[j][i] = k
                k+=1
            j_max -=1
            for j in range(j_max-1,j_min-1,-1):
                result[j][i] = k
                k+=1
            i_min +=1
        
        return result
                

    def generateMatrix_slow(self, n: int) -> List[List[int]]:
        # but actually really good memory usage
        # oh. ha. no.
        # 13.9 MB is in the top 10%,
        # but 14 MB is in the bottom 10%
        
        # (it's meant to be a generator, which is irrelevent to the problem description, so)
        
        
        #  0 1 2   0 1 2 3   0 1 2 3 4
        #  0 1 0   0 1 1 0   0 1 2 1 0
        #
        #  (n - abs( 2*i - n ))//2
        def ring_number(i,j,n):
            # i,j,n all 0-indexed, so n is actually different from problem description
            # so
            n -= 1
            return min((n - abs( 2*i - n ))//2, (n - abs( 2*j - n ))//2 )

        
        #   1  2  3  4  5
        #   16 1  2  3  6
        #   .  8  1  4  7
        #   .  7  6  5  8
        #   .  .  .  .  9
        
        # even sequence = 0, 4, 12, 20 = 4(n-1), great
        # odd sequence  = 1, 8, 16, 24 = 4(n-1) unless n = 1, very odd
        #
        # hmm, I don't know that I need that though?
        
        def location_in_ring(i,j,n):
            #if n == 1:
            #    return 1
            if i == 0:
                return j + 1
            if j == n-1:
                return n + i
            if i == n-1:
                return 3*n-2-j
            if j == 0:
                return 4*n-3 - i
            raise(BaseException)
        
        
                
        def value(i,j,n):
            r = ring_number(i,j,n)
            sub_i = i - r
            sub_j = j - r
            
            # sum from x = 1 to r of 4(n-1-2(x-1)) = 4(n+1-2x)
            # sum(2*range(x)+2*x) = x**2 + 1
            #r = 0: 0
            #    1: 4(n-1)
            #    2: 4(n-1) + 4(n-1-2)
            #    3: 4(n-1) + 4(n-1-2) + 4(n-1-4)
            
            total_in_outer_rings = 4*(n+1)*r -4*r**2 - 4*r
            return total_in_outer_rings + location_in_ring(sub_i, sub_j, n-2*r)
            
        
        # okay, uh, but now I need to overload the indexing syntax...
        #, oh, well, it doesn't solve anything but
        result = [[value(i,j,n) for j in range(n)] for i in range(n)]
        return result