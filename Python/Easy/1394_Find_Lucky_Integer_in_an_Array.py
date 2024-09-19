"""

Question: Find lucky integer in an array

Summary: Given an array of integers 'arr',
a lucky integer is said to be an integer that has a frequency in the array equal to its value.
Return the largest lucky integer in the array. If there is no lucky integer, return -1.

Method: Iterate through the array to count the frequency of each integer. 
If the frequency matches the integer’s value, consider it a lucky integer. Track the largest lucky integer found.

Time complexity: O(n^2) (due to the use of count in a loop)
Space complexity: O(n)
"""

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        result = []
      
        for i in arr:
            # Check if the frequency of the integer matches its value
            if arr.count(i) == i:
                result.append(i)
            # Append -1 to handle the case where no lucky integer is found 
            result.append(-1)

        # Return the largest lucky integer or -1 if none are found
        return max(result)


# Example usage
result = Solution().findLucky([2, 2, 3, 4])
print(result)  # Output: 2
