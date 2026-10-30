class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_list = list(set(nums))
        sorted_list.sort()
        lista = []

        if len(sorted_list) > 0:
            sequence = 1
            for i in range(1, len(sorted_list)):
                if sorted_list[i] - sorted_list[i-1] == 1:
                    sequence += 1
                else :
                    lista.append(sequence)
                    sequence = 1
            lista.append(sequence)
            return max(lista)
        else:
            return 0
        