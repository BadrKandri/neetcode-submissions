class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m
        p2 = 0

        for i in range(n):
            nums1[p1] = nums2[p2]
            p1 +=1
            p2 +=1
        nums1.sort()
        