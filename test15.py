class Solution:

    def findMax(self, nums: list[int]) -> int:

        maximum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > maximum:
                maximum = nums[i]

        return maximum


obj = Solution()

print(obj.findMax([4, 8, 2, 10, 6]))