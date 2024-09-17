"""

Question: Sort array by parity

Summary: Given an integer array 'nums', 
rearrange the array so that all even integers appear at the beginning followed by all odd integers. 
Return any array that satisfies this condition.

Method: Use two separate lists to collect even and odd integers, then concatenate these lists.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
      
        for i in nums:
            if i % 2 == 0:
                arr1.append(i)
            else:
                arr2.append(i)
              
        return arr1 + arr2


# Example usage
result = Solution().sortArrayByParity([3, 1, 2, 4])
print(result)  # Output: [2, 4, 3, 1]
