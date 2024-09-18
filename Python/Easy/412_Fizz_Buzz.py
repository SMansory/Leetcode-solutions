"""

Question: Fizz buzz

Summary: Given an integer 'n', create a list of strings representing the numbers from 1 to 'n'. 
For multiples of 3, the string should be “Fizz”, for multiples of 5, the string should be “Buzz”, 
and for multiples of both 3 and 5, the string should be “FizzBuzz”. If a number is not a multiple of 3 or 5,
it should be represented by the number itself as a string.

Method: Loop through numbers from 1 to 'n', 
appending the appropriate string to the result list based on the divisibility rules.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]: 
        myList = []
      
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                myList.append("FizzBuzz")
            elif i % 3 == 0:
                myList.append("Fizz")
            elif i % 5 == 0:
                myList.append("Buzz")
            else:
                myList.append(str(i))
              
        return myList


# Example usage
result = Solution().fizzBuzz(3)
print(result)  # Output: ["1", "2", "Fizz"]
