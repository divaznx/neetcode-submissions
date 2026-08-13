class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        longest = 1
        current_number = 1

        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current_number += 1

            elif nums[i] == nums[i - 1]:
                continue

            else:
                longest = max(longest, current_number)
                current_number = 1

        longest = max(longest, current_number)

        return longest