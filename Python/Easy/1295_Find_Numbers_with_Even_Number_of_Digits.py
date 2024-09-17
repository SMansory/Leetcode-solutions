"""

Question: Find numbers with even number number of digits

Summary: Given an array of integers 'nums', determine how many of the integers have an even number of digits.

Method: Iterate through each number in the array, count the digits, and check if the count is even.
Increment the count of even-digit numbers accordingly.

Time complexity: O(n * log m), where 'n' is the number of integers in the array 
and 'm' is the average number of digits in the integers.
Space complexity: O(1)
"""

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even = 0
      
        for num in nums:
          
            count = 0
            while num != 0:
                num //= 10
                count += 1
            if count % 2 == 0:
                even += 1
              
        return even

        
 # Example usage       
result = Solution().findNumbers([12, 345, 2, 6, 7896])   
print(result)  # Output: 2
