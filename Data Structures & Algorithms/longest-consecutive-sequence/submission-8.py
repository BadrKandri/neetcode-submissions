class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_list = list(set(nums))
        sorted_list.sort()
        my_list = []

        if len(sorted_list) > 0:
            sequence = 1
            for i in range(1, len(sorted_list)):
                if sorted_list[i] - sorted_list[i-1] == 1:
                    sequence += 1
                else :
                    my_list.append(sequence)
                    sequence = 1
            my_list.append(sequence)
            return max(my_list)
        else:
            return 0
        