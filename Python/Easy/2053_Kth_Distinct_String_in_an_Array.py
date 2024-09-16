"""

Question: Kth distinct string in an array

Summary: Given an array of strings 'arr' and an integer 'k', return the k-th distinct string in the array.
A distinct string is one that appears only once in the array. If there are fewer than 'k' distinct strings, return an empty string. 
The strings are considered in the order they appear in the array.

Method: Iterate through the array, count the occurrences of each string, and collect the distinct strings.
Return the k-th distinct string if it exists.

Time complexity: O(n^2), where n is the length of the array, due to the use of count() in a loop.
Space complexity: O(n)
"""

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ans = []

        # Iterate through the array to find distinct strings
        for i in arr:
            if arr.count(i) == 1:
                ans.append(i)

        # Return the k-th distinct string if it exists
        return "" if k > len(ans) else ans[k - 1]


# Example usage
result = Solution().kthDistinct(["d", "b", "c", "b", "c", "a"], 2)
print(result)  # Output: "a"
