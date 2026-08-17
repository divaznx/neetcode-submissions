class Solution:
    def productExceptSelf(self, nums):
        output = [1] * len(nums)

        # Left products
        left = 1

        for i in range(len(nums)):
            output[i] = left
            left *= nums[i]

        # Right products
        right = 1

        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output
        