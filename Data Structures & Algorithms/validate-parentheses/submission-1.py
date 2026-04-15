class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            print(stack, "stack")
            if char in mapping:
                top = stack.pop() if stack else '#'
                print(char,"======", top)
                if mapping[char] != top:
                    return False
            else:
                print(char, "---")
                stack.append(char)

        return not stack