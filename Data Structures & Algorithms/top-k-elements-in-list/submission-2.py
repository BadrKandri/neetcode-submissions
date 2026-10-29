class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = dict(Counter(nums))
        sorted_by_value = dict(sorted(dic.items(), key=lambda item: item[1]))
        sorted_keys_list = list(sorted_by_value.keys())
        sorted_keys_list.reverse()
        return sorted_keys_list[:k]
