"""

Question: Find the XOR of numbers which appear twice 

Summary: Given an array 'nums' where each number appears either once or twice,
return the bitwise XOR of all the numbers that appear twice in the array. If no number appears twice, return 0.

Method: Use a counter to identify numbers that appear twice, then compute the bitwise XOR of these numbers.

Time complexity: O(n), where n is the length of the array.
Space complexity: O(n)
"""

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        # Count the occurences of each number
        counter = Counter(nums)
        # Identify the number that appear twice 
        arr = [key for key, value in counter.items() if value==2]
        xor_count = 0 

        # Compute the bitwise XOR of these numbers
        for num in arr:
            xor_count ^= num
          
        return xor_count


# Example usage
result = Solution().duplicateNumbersXOR([1, 2, 1, 3])
print(result)  # Output: 1
