class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # 双指针:快慢指针   保持原有元素顺序
        slow = 0
        fast = 0
        size = len(nums)
        while fast < size:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
            else:
                fast += 1
        return slow

    # def removeElement(self, nums: list[int], val: int) -> int:
    #     # 双指针:快慢指针 一头一尾  改变原有顺序
    #     slow = 0
    #     fast = len(nums) - 1
    #     while slow <= fast:
    #         if nums[slow] == val:
    #             nums[slow] = nums[fast]
    #             fast -= 1
    #         else:
    #             slow += 1
    #     return slow


if __name__ == '__main__':
    S = Solution()
    print(S.removeElement([3, 2, 2, 3], 3))
    print(S.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
