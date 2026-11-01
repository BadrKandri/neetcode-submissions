class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        seen=set([s[0]])
        l = 0
        max_sub = 0
        
        for r in range(1, len(s)):
            if s[r] not in seen:
                seen.add(s[r])
            else:
                max_sub = max(max_sub, len(seen))
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l+=1

                seen.remove(s[l])
                l+=1
                seen.add(s[r])

        max_sub = max(max_sub, len(seen))
        return max_sub       