class Solution:

    def findMin(self, nums: list[int]) -> int:

        minimum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < minimum:
                minimum = nums[i]

        return minimum


obj = Solution()

print(obj.findMin([8, 3, 10, 2, 6]))