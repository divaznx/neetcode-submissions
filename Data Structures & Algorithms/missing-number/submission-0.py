class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n  = len(nums)
        expected_sum = n*(n+1) // 2

        output = 0
        for num in nums:
            output+=num
        diff = expected_sum - output

        return diff