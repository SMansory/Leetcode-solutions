"""
Problem: Convert temperature
Summary: Given a non-negative floating point number 'celsius' rounded to two decimal places, 
convert it to Kelvin and Fahrenheit and return the results as an array 'ans = [kelvin, fahrenheit]'.
Method: Direct conversion - Use the formulas for converting Celsius to Kelvin and Fahrenheit.
Time complexity: O(1)
Space complexity: O(1)
"""

class Solution:

    def convertTemperature(self, celsius):
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        ans = [float(f"{kelvin:.5f}"), float(f"{fahrenheit:.5f}")]
      
        return ans


# Example usage
result = Solution().convertTemperature(36.50)
print(result)  # Output: [309.65000, 97.70000]
