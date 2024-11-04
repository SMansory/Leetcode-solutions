"""

Question: Convert integer to the sum of two no-zero integers

Summary: Given an integer 'n', return a list of two integers [a, b] where 'a' and 'b' are positive integers 
without any zeros in their decimal representation,
and their sum equals 'n'.

Method: Iterate from 1 to n-1, and for each integer 'i', 
check if both 'i' and n-i do not contain any zeros in their decimal representation. 
Return the pair [i, n-i] when such a pair is found.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n): 
            A = i
            B = n - i

            # Check if both 'A' and 'B' do not contain any zeros
            if "0" not in str(B) and "0" not in str(A):
                return [A, B]


# Example usage
result = Solution().getNoZeroIntegers(2)
print(result)  # Output: [1, 1]
