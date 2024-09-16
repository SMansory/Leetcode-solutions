"""

Question: Number of senior citizens

Summary: Given a 0-indexed array of strings 'details', 
where each element is a compressed string of length 15 representing a passenger’s information,
return the number of passengers who are strictly more than 60 years old. The string format is as follows:
1. The first 10 characters are the passenger’s phone number.
2. The 11th character denotes the gender.
3. The 12th and 13th characters indicate the age.
4. The last 2 characters determine the seat allotted.

Method: Iterate through the details array, extract the age from each string, and count how many passengers are older than 60.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
      
        for i in range(len(details)):
            # Extract the age from the string
            age = details[i][11] + details[i][12]
          
            if int(age) > 60:
                count += 1
              
        return count


# Example usage
result = Solution().countSeniors(["7868190130M7522", "5303914400F9211", "9273338290F4010"])
print(result)  # output: 2
