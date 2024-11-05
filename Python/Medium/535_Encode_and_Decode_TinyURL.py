"""

Question: Encode and decode tinyURL

Summary: Design a class to encode a URL and decode a tiny URL. 
Ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Method: Initialize the system. Use the encode method to return a tiny URL for the given long URL.
Use the decode method to return the original long URL for the given tiny URL.

Time complexity: O(1)
Space complexity: O(1)
"""

class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        return longUrl


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return shortUrl

      
# Example usage
# Instantiate the Codec object 
codec = Codec() 

# Example of long URL 
long_url = "https://leetcode.com/problems/design-tinyurl" 

# Encode the long URL to a shortened URL 
short_url = codec.encode(long_url) 
print(f"Encoded URL: {short_url}")  # Output: Encoded URL: https://leetcode.com/problems/design-tinyurl

# Decode the shortened URL back to the original long URL 
decoded_url = codec.decode(short_url) 
print(f"Decoded URL: {decoded_url}")  # Output: Decoded URL: https://leetcode.com/problems/design-tinyurl
