"""

Question: Sort integers by the power value

Summary: Determine the k-th integer in the range [lo, hi] sorted by the power value, 
which represents the number of steps needed to transform the integer into 1 using specific rules for even and odd integers.

Method: Calculate the power value for each integer in the given range [lo, hi] by iterating through the range and 
counting the steps needed to transform each integer into 1. Use these power values to sort the integers.

Time complexity: O(n log n)
Space complexity: O(n)
"""

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        count = 0
        lst = []
        lst1 = [x for x in range(lo, hi+1)]
      
        for x in range(lo, hi+1):
            count = 0
            while x > 1:
                if x % 2 == 0:
                    x //= 2
                else:
                    x = 3 * x + 1
                count += 1
            lst.append(count)
          
        return [x for _, x in sorted(zip(lst, lst1))][k-1]


# Example usage
result = Solution().getKth(12, 15, 2)
print(result)  # Output: 13
