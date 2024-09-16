"""

Question: Separate the digits in an array

Summary: Given an array of positive integers 'nums', 
create a new array 'answer' that contains the digits of each integer in 'nums' in the same order they appear.
For instance, the integer 10921 would be separated into [1, 0, 9, 2, 1].

Method: Use a list comprehension to iterate through each integer in nums, 
convert it to a string, and then iterate through each character of the string to convert it back to an integer.

Time complexity: O(n * m), where n is the number of integers in 'nums' and m is the average number of digits in each integer.
Space complexity: O(n * m)
"""

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(digit) for i in nums for digit in str(i)]


# Example usage
result = Solution().separateDigits([13, 25, 83, 77])
print(result)  # Output: [1, 3, 2, 5, 8, 3, 7, 7]
