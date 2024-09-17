"""

Question: Relative sort array

Summary: Given two arrays 'arr1' and 'arr2',
where the elements of 'arr2' are distinct and all elements in 'arr2' are also in 'arr1',
sort the elements of 'arr1' such that the relative ordering of items in 'arr1' matches 'arr2'.
Elements not in 'arr2' should be placed at the end of 'arr1' in ascending order.

Method: Use nested loops to append elements from 'arr1' that are in 'arr2' to the result list, marking them as processed.
Then, sort the remaining elements of 'arr1' and append them to the result list.

Time complexity: O(n log n)
Space complexity: O(n)
"""

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
      
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j] == arr2[i]:
                    result.append(arr1[j])
                    arr1[j] = -1
                  
        arr1.sort()
      
        for i in arr1:
            if i != -1:
                result.append(i)
              
        return result


# Example usage
result = Solution().relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6])
print(result)  # Output: [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
