"""

Question: Determine color of a chessboard square

Summary: Given a string 'coordinates' representing the coordinates of a square on a chessboard, 
return true if the square is white and false if the square is black. 
The coordinates will always be valid and follow the format where the letter comes first and the number second.

Method: Convert the letter to a number using a dictionary, then check if the sum of the letter’s number and the digit is even or odd. 
If the sum is even, the square is black; if odd, the square is white.

Time complexity: O(1)
Space complexity: O(1)
"""

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        dictionary = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6 , 'g':7, 'h':8}
      
        if dictionary[coordinates[0]] % 2 == int(coordinates[1]) % 2:
            return False
        return True


# Example usage
result = Solution().squareIsWhite("a1")
print(result)  # Output: false
