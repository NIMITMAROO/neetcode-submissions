class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        sort = sorted(piles)
        left = 1
        right = sort[-1]
        k = 1
        ans = right

        while left <= right:

            k = (left + right) // 2
            time = 0
            for s in sort:
                time += math.ceil(s / k)

            if time > h:
                left = k + 1
            
            elif time <= h:
                right = k - 1
                ans = min(ans,k)



        
        return ans




        