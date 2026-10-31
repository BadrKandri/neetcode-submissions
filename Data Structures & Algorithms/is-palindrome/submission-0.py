class Solution:
    def isPalindrome(self, s: str) -> bool:
        my_list = [char.lower() for char in s if char.isalnum()]

        left = 0
        right = len(my_list)-1

        while left < right:
            if my_list[left] != my_list[right]:
                return False
            else:
                left +=1
                right -=1

        return True
