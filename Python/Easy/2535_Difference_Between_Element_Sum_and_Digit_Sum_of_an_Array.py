"""

Question: Difference between element sum and digit sum of an array

Summary: Given an array of positive integers 'nums', 
compute the absolute difference between the sum of all elements (element sum) and the sum of all digits in the elements (digit sum).
The absolute difference between two integers ( x ) and ( y ) is defined as ( |x - y| ).

Method: Convert each number to its digits, sum the digits, and subtract this sum from the sum of the elements. 
Return the absolute difference.

Time complexity: O(n), where n is the total number of digits in the array.
Space complexity: O(n)
"""

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        # Create a list of all digits in the array 'answer'
        answer = [int(digit) for num in nums for digit in str(num)] 
        # Calculate the absolute difference between element sum and digit sum
        result = sum(nums) - sum(answer)
      
        return result


# Example usage
result = Solution().differenceOfSum([1, 15, 6, 3])   
print(result)  # Output: 9
