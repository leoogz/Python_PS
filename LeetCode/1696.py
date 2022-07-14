class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        import heapq
        ePoint = len(nums) - 1
        dp = [nums[ePoint]] * (ePoint + 1)
        
        max_score = -1
        hq = []
        heapq.heappush(hq,(-dp[ePoint],ePoint))
        for i in reversed(range(ePoint)):
            pos = i + k
            if(pos > ePoint):
                pos = ePoint
            maxValue, index = hq[0]
            while len(hq) != 0 and hq[0][1] > pos:
                heapq.heappop(hq)
                maxValue, index = hq[0]
 
            dp[i] = nums[i]-maxValue
            heapq.heappush(hq,(-dp[i],i))
        return dp[0]