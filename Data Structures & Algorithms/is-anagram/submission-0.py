class Solution:
    def word_count(self, word: str) -> dict:
        dic = {}
        for c in word:
            dic[c] = dic.get(c, 0) +1
        return dic

    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = self.word_count(s)
        t_dic = self.word_count(t)

        return s_dic == t_dic