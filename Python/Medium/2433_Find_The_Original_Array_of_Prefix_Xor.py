"""

Question: Find the original array of prefix xor

Summary: Given an integer array pref of size 'n', 
return the array 'arr' of size 'n' such that pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]. The bitwise-xor operation ^ is used.

Method: Initialize the result array with the first element of 'pref'. 
Iterate through the 'pref' array starting from the second element and 
compute each element of 'arr' using the bitwise-xor operation with the previous element of 'pref'.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # Initialize the result array with the first element of 'pref'
        arr = [pref[0]]

        # Iterate through the 'pref' array to compute each element of 'arr'
        for i in range(1, len(pref)):
            arr.append(pref[i] ^ pref[i - 1])
          
        return arr


# Example usage
result = Solution().findArray([5, 2, 0, 3, 1])
print(result)  # Output: [5, 7, 2, 3, 2]
