"""

Question: Contains duplicates


Summary: You are given an integer array 'nums', 
return true if any value appears at least twice in the array, and false if every element is distinct.


Method: Use a set to track seen elements. Iterate through the array, and if an element is already in the set, return true.
If the loop completes without finding duplicates, return false.


Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Initialize an empty set to track seen elements
      
        for num in nums:

            # Check if the current element is already in the set
            if str(num) in seen:
                return True  # Duplicate found
              
            seen.add(str(num))  # Add the current element to the set
          
        return False  # No duplicates found


# Example usage
result = Solution().containsDuplicate([1, 2, 3, 1])
print(result)  # Output: true
        
