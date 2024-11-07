"""

Question: Beautiful array

Summary: Given an integer 'n', return a beautiful array of length 'n' that satisfies two conditions: 
it is a permutation of the integers in the range [1, n], and for every '0 <= i < j < n', 
there is no index 'k' with 'i < k < j' where '2 * nums[k] == nums[i] + nums[j]'.

Method: Build the beautiful array by iteratively constructing a new array of even and odd indexed elements from 
the current array until the desired length is reached.

Time complexity: O(n log n)
Space complexity: O(n)
"""

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        arr = [1]
      
        while len(arr) < n:
            even = [2 * i for i in arr]
            odd = [2 * i - 1 for i in arr]
            arr = even + odd
          
        return [i for i in arr if i <= n]   


# Example usage
result = Solution().beautifulArray(4)
print(result)  # Output: [4, 2, 3, 1]
