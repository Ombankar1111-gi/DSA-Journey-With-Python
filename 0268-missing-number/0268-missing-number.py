class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        for num in range(n + 1):
            found = False

            for i in nums:
                if i == num:
                    found = True
                    break

            if not found:
                return num