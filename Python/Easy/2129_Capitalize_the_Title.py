"""

Question: Capitalize the title


Summary: Given a string 'title' consisting of one or more words separated by a single space, 
capitalize the string by changing the capitalization of each word such that:

1. If the length of the word is 1 or 2 letters, change all letters to lowercase.
2. Otherwise, change the first letter to uppercase and the remaining letters to lowercase.

Return the capitalized title.


Method: Split the string into words, process each word based on its length, 
and then join the words back into a single string.


Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        # Split the title into words
        title = title.split()
      
        for i in range(len(title)):

            # If the word length is less than 3, convert it to lowercase
            if len(title[i]) < 3:
                title[i] = title[i].lower()
              
            else:
                # Otherwise, capitalize the first letter and lowercase the rest
                title[i] = title[i].title()

        # Join the words back into a single string
        return " ".join(title)


# Example usage
result = Solution().capitalizeTitle("capiTalIze tHe titLe")
print(result)  # Output: "Capitalize The Title"
