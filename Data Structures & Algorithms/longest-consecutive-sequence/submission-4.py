class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number_set = set(nums)
        longest_length = 0
        for nums in number_set:
            if (nums - 1) not in number_set:
                current_length = 1 
                current_num = nums 
                while (current_num + 1) in number_set:
                    current_length += 1
                    current_num += 1
                longest_length = max(longest_length, current_length)
                
        return longest_length 
                     