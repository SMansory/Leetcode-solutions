"""

Question: Count good triplets 

Summary: Given an array of integers 'arr', and three integers 'a', 'b', and 'c', find the number of good triplets.
A triplet '((arr[i], arr[j], arr[k]))' is considered good if the following conditions are met:
(0 <= i < j < k < arr.length)
1. (|arr[i] - arr[j]| <= a)
2. (|arr[j] - arr[k]| <= b)
3. (|arr[i] - arr[k]| <= c) Where (|x|) denotes the absolute value of (x).

Method: Use three nested loops to iterate through all possible triplets and count those that satisfy the given conditions.

Time complexity: O(n^3)
Space complexity: O(1)
"""

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
      
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                  
                    if abs(arr[i] - arr[j]) <= a and abs(arr[k] - arr[j]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1
                      
        return count


# Example usage
result = Solution().countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3)
print(result)  # Output: 4
