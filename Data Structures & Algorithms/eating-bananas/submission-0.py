class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 0 
        res=0
        left = 1
        right=max(piles)

        while(left<=right):
            k=(left+right)//2
            total_time=0

            for p in piles:
                total_time+=math.ceil(float(p)/k)
            if total_time<=h:
                res=k
                right=k-1
            else:
                left=k+1
        return res
