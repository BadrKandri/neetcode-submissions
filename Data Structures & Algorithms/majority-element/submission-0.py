class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0)+1
        max_number = max(dict.values())
        inverted_dict = {value: key for key, value in dict.items()}
        majority_element = inverted_dict[max_number]
        return majority_element



        