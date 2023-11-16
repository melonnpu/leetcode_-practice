"""
977. 有序数组的平方
"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # 1.双指针法，两边向中间靠拢，先定义好指定长度存储的列表
        n = len(nums)
        left_index = 0
        right_index = n-1
        cur_pos = n-1
        res = [0]*n

        while left_index <= right_index:
            if nums[left_index]*nums[left_index] < nums[right_index]*nums[right_index]:
                res[cur_pos] = nums[right_index]*nums[right_index]
                cur_pos -= 1
                right_index -= 1
            else:
                res[cur_pos] = nums[left_index]*nums[left_index]
                cur_pos -= 1
                left_index += 1
        return res

        # 2.先求平方后排序
        # return sorted([num*num for num in nums])
