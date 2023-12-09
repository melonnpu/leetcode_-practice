"""
15.三数之和

给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例：
    输入：nums = [-1,0,1,2,-1,-4]
    输出：[[-1,-1,2],[-1,0,1]]
    解释：
        nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
        nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
        nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
        不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
        注意，输出的顺序和三元组的顺序并不重要。
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i in range(n):
            if nums[i] > 0:
                return res
            # i去重,后面一个和前面一个相等的话，跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1  # j
            right = n - 1  # k
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    # 符合条件的添加后，后序j,k去重复
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # j向后移动，和前一个比较相等
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # k向前移动，和后一个比较
                    left += 1
                    right -= 1

        return res
