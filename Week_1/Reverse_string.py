from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    def reverse(self, input_str: str) -> None:
        s = list(input_str)
        self.reverseString(s)
        reversed_string = ''.join(s)
        print(f"Original String: {input_str}")
        print(f"Reversed String: {reversed_string}")
input_string = input("Enter a string: ")
solution = Solution()
solution.reverse(input_string)
