"""

Question: Reformat date

Summary: Given a date string in the format “Day Month Year”, where:
Day is in the set {“1st”, “2nd”, “3rd”, …, “30th”, “31st”}.
Month is in the set {“Jan”, “Feb”, “Mar”, …, “Nov”, “Dec”}.
Year is in the range [1900, 2100].
Convert the date string to the format YYYY-MM-DD.

Method: Split the date string into its components, convert the month to its numeric representation,
and format the day and month to ensure they are two digits.

Time complexity: O(1)
Space complexity: O(1)
"""

class Solution:
    def reformatDate(self, date: str) -> str:
        # Dictionary to convert month abbreviations to numeric format
        converted_month = {'Jan': '01', 'Feb': '02', 
                     'Mar': '03', 'Apr': '04', 
                     'May': '05', 'Jun': '06', 
                     'Jul': '07', 'Aug': '08', 
                     'Sep': '09', 'Oct': '10', 
                     'Nov': '11', 'Dec': '12'}

        # Split the date string into day, month, and year
        arr = date.split()
        day = arr[0][:-2]  # Remove the suffix from the day
        month = arr[1]
        year = arr[2]

        # Ensure the day is two digits
        if int(day) < 10:
            day = "0" + day

        # Return the formatted date string
        return (f"{year}-{converted_month[month]}-{day}")


# Example usage
result = Solution().reformatDate("20th Oct 2052")
print(result)  # Output: "2052-10-20"
