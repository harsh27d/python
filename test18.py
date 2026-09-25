class Solution:

    def countEven(self, nums: list[int]) -> int:
        count = 0

        for i in nums:
            if i % 2 == 0:
                count = count + 1

        return count


obj = Solution()

print(obj.countEven([1, 2, 3, 4, 5, 6]))