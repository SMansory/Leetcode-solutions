"""

Question: Calculate the difference between the product and sum of digits of an integer

Summary: Given an integer 'n', find the difference between the product of its digits and the sum of its digits.

Method: Convert the integer to a string, then to a list of its digits. 
Calculate the sum and product of the digits, and return their difference.

Time complexity: O(d), where d is the number of digits in 'n'
Space complexity: O(1)
"""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
         # Convert the integer to a string, then to a list of its digits
         my_str = str(n)
         my_list = list(my_str)

         # Initialize the sum and product of digits
         sum_of_digits = 0
         product_of_digits = 1

         # Calculate the sum and product of digits
         for number in my_list:
            num = int(number)
            sum_of_digits += num
            product_of_digits *= num
            # Store the difference between the product and sum in a variable, then return it
            result = product_of_digits - sum_of_digits
           
         return result


# Example usage
result = Solution().subtractProductAndSum(234)
print(result)  # Output: 15
