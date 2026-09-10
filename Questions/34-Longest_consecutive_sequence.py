# Question : 128. Longest Consecutive Sequence
# Complexity : Time: O(N), Space: O(N)
# Topic/Category : Arrays & Hashing
# Difficulty : Medium
class Solution:
    def longestConsecutive(self, nums):
        s = set(nums)   # converting the list into a set for the O(1) look up speed
        longest = 0
        for num in s:
            if num - 1 not in s:    # This basically checks it the previous number doesn't exists else, the sequence is starting from somewhere else
                next_num = num + 1  
                length  = 1     # we start at 1 because, the above conditions will be executed when we have found the number that starts the sequence.
                while next_num in s:
                    length += 1
                    next_num += 1
                    longest = max(longest,length) 
        return longest


p = Solution()
print(p.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(p.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(p.longestConsecutive( [1, 9, 3, 10, 4, 20, 2]))
