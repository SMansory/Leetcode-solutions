"""

Question: Minimum number game

Summary: Given a 0-indexed integer array 'nums' of even length and an empty array 'arr',
simulate a game where Alice and Bob alternately remove the smallest element from 'nums' and append it to 'arr'. 
Alice removes the smallest element first, followed by Bob. Bob appends his removed element to 'arr' first, followed by Alice.
Continue until 'nums' is empty. Return the resulting array 'arr'.

Method: Sort the array 'nums' and use list comprehension to simulate the game by iterating through the sorted array, 
appending elements to 'arr' in the specified order.

Time complexity: O(n log n)
Space complexity: O(n)
"""

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        # Use list comprehension to simulate the game
        return [nums[i + 1] if i % 2 == 0 else nums[i - 1] for i in range(len(nums))]


# Example usage
result = Solution().numberGame([5, 4, 2, 3])
print(result)  # Output: [3 ,2, 5, 4]
