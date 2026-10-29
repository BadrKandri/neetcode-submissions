class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_list = list(set(nums))
        sorted_list.sort()
        list_of_sequences = []

        if len(sorted_list) > 0:
            sequence = 1
            for i in range(1, len(sorted_list)):
                if sorted_list[i] - sorted_list[i-1] == 1:
                    sequence += 1
                else :
                    list_of_sequences.append(sequence)
                    sequence = 1
            list_of_sequences.append(sequence)
            return max(list_of_sequences)
        else:
            return 0
        