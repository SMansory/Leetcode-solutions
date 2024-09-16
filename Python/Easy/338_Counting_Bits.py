"""

Question: Counting bits

Summary: Given an integer 'n', return an array 'ans' of length 'n + 1' 
where each element 'ans[i]' represents the number of 1’s in the binary representation of 'i' for all 'i' from 0 to 'n'.

Method: Create an array of integers from 0 to 'n', convert each integer to its binary representation,
and count the number of 1’s in each binary string.

Time complexity: O(n * log n)
Space complexity: O(n)
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [i for i in range(0, n + 1)]
        result = [bin(i).count("1") for i in arr]
        return result


# Example usage
result = Solution().countBits(2)
print(result)  # Output: [0, 1, 1]
