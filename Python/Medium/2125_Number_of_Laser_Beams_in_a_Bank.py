"""

Question: Number of laser beams in a bank

Summary: Given a 0-indexed binary string array 'bank' representing the floor plan of a bank, 
return the total number of laser beams between security devices. 
A laser beam is formed between two devices located on different rows with no devices in between.

Method: Iterate through each row of the matrix, count the number of security devices in each row,
and calculate the number of laser beams based on the counts of devices in adjacent rows.

Time complexity: O(m * n) - where 'm' is the number of rows and 'n' is the number of columns.
Space complexity: O(1)
"""

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans, res = 0, 0

        # Iterate through each row of the matrix
        for i in bank:
            # Count the number of security devices in the row
            count = i.count("1")
          
            if count:
                # Calculate the number of laser beams
                ans += res * count
                res = count
              
        return ans


# Example usage
result = Solution().numberOfBeams(["011001", "000000", "010100", "001000"])
print(result)  # Output: 8
