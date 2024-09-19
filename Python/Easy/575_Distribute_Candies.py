"""

Question: Distribute candies

Summary: Alice has 'n' candies, each of a certain type given by the array 'candyType'. 
The doctor advised her to eat only 'n / 2' candies. 
Alice wants to eat the maximum number of different types of candies while following this advice. Given the array 'candyType',
return the maximum number of different types of candies she can eat if she only eats 'n / 2' of them.

Method: Calculate the minimum between half the total number of candies and the number of unique candy types.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # Return the minimum of unique candy types and max candies Alice can eat
        return min(len(candyType)//2, len(list(set((candyType)))))


# Example usage
result = Solution().distributeCandies([1, 1, 2, 2, 3, 3])
print(result)  # Output: 3
