def isValid(s):
    bracket_map = {')': '(', '}': '{', ']': '['}

    stack = []

    for char in s:
        if char in bracket_map:
            top_elem = stack.pop() if stack else '#'
            if bracket_map[char] != top_elem:
                return False
        else:
            stack.append(char)

    return not stack


print(isValid('{}{}'))