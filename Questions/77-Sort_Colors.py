# Question : 75. Sort Colors
# Complexity : Time = O(n), Space = O(1)
# Topic/Category : Array,Two Pointers,Sorting,Quicksort,Bubble Sort
# Difficulty : Medium

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sum0,sum1,sum2 = 0,0,0
        for i in range(len(nums)):
            if nums[i] == 0:
                sum0 += 1
            elif nums[i] == 1:
                sum1 += 1
            else:
                sum2 += 1

        for i in range(len(nums)):
            if sum0 > 0:
                nums[i] = 0
                sum0 -= 1
            elif sum1 > 0:
                nums[i] = 1
                sum1 -= 1
            else:
                nums[i] = 2
                sum2 -= 1
        return nums

p = Solution()
print(p.sortZeroOneTwo([1, 0, 2, 1, 0]))