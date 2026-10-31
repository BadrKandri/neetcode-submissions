class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            temp_result = numbers[left] + numbers[right]

            if temp_result > target:
                right -=1
            elif temp_result < target:
                left +=1
            else:
                output = [left+1, right+1]
                return output