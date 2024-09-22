"""

Question: Roman to integer


Summary: Given a Roman numeral string, convert it to an integer. 
Roman numerals are represented by seven different symbols: 'I', 'V', 'X', 'L', 'C', 'D', and 'M'.
The numeral for four is not 'IIII' but 'IV'.
The same principle applies to the numbers nine '(IX)', forty '(XL)', ninety '(XC)', four hundred '(CD)',
and nine hundred '(CM)'.


Method: Use a dictionary to map Roman numeral symbols to their integer values.
Iterate through the string, adding the value of each symbol to the result.
If a symbol is smaller than the next symbol, subtract its value instead.


Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary to map Roman numerals to their integer values
        romanInt = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # Convert the Roman numeral string to a list of integer values
        myList = [romanInt[i] for i in s]
        result = 0

        # Iterate through the list of values
        for i in range(len(myList) - 1):

            # If the current value is less than the next value, subtract it
            if myList[i] < myList[i + 1]:
                result -= myList[i]
              
            else:
                # Otherwise, add it to the result
                result += myList[i]

        # Add the last value to the result
        return result + myList[-1]


# Example usage
result = Solution().romanToInt("III")
print(result)  # Output: 3
