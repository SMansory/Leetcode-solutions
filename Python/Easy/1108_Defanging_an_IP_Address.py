"""
Problem: Defang an IP address
Summary: Given a valid IPv4 address, return a modified version where every period "." is replaced with "[.]".
Method: String replacement - Use the 'replace' method to substitute all periods with "[.]".
Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


# Example usage
result = Solution().defangIPaddr("1.1.1.1")
print(result)  # Output: "1[.]1[.]1[.]1"
