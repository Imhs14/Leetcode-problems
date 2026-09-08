# Question : 31. Next Permutation
# Complexity : Time = O(n), Space = O(1)
# Topic/Category : Array, Two Pointers
# Difficulty : Medium
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot = n
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                pivot = i                    # This for the pivot point finding, if we find the number i that is smaller then i+1. then that i is our pivot tells us that ki the arr breaks the descending order here.
                for j in range(n-1,pivot-1,-1):      # This will swap that pivot with the number which is greater but the smallest , which is on right side of the pivot number in the array.
                    if nums[j] > nums[pivot]:
                        nums[j],nums[pivot] = nums[pivot],nums[j]
                        break
                break
        
        if pivot == n:       # what if the array is in descending order, in that case we just need to start swapping from the 0th index till n/2 index
            pivot = 0
        elif pivot < n:      # what if we do find the pivot and swap the number in the inner for loop, we have to reverse the number after the pivot till the end of the array. That's why we are using strr + 1
            pivot += 1

        p,q = pivot ,n - 1
        while p < q:
            nums[p],nums[q] = nums[q],nums[p]
            p+=1
            q-=1
        
        return nums