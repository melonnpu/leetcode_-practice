"""
209. 长度最小的子数组
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # 1.双指针
        n = len(nums)
        res = n+1
        left = 0
        right = 0
        sum = 0
        while right <n:
            sum += nums[right]
            while sum >= target:
                res = min(res, right-left+1)
                sum -= nums[left]
                left += 1
            right += 1
        return 0 if res == n+1 else res

        # 2.暴力解法
        # n = len(nums)
        # res = n + 1
        # for i in range(n):
        #     sum = 0
        #     for j in range(i, n):
        #         sum += nums[j]
        #         if sum >= target:
        #             res = min(res, j - i + 1)
        #             break
        # return 0 if res == n + 1 else res
