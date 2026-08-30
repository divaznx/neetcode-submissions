class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()

        for i in range(len(nums)):
            seen = set()

            for j in range(i + 1, len(nums)):
                target = -(nums[i] + nums[j])

                if target in seen:
                    result.add(tuple(sorted([nums[i], nums[j], target])))

                seen.add(nums[j])

        return list(result)