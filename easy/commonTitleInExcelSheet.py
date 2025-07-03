class Solution(object):
    def convertToTitle(self, columnNumber):
        result = ""
        while columnNumber > 0:
            columnNumber -= 1  # Adjust to 0-based indexing
            remainder = columnNumber % 26
            result = chr(65 + remainder) + result  # chr(65) = 'A'
            columnNumber //= 26
        return result
