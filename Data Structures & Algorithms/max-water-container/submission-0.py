class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res=[]
        largest=0
        second=0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                res.append(min(heights[i], heights[j]) * (j - i))
        
        return max(res)