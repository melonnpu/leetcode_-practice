class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (right-left) // 2 + left  # =(right+left) // 2 防止内存溢出
            num = nums[mid]
            if num > target:
                right = mid-1
            elif num < target:
                left = mid + 1
            else:
                return mid
        return -1


if __name__ == '__main__':
    S = Solution()
    print(S.search([-1, 0, 3, 5, 9, 12], 9))
    print(S.search([-1, 0, 3, 5, 9, 12], 2))
