class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            w_sorted = ''.join(sorted(word))
            dic[w_sorted].append(word)
        return list(dic.values())