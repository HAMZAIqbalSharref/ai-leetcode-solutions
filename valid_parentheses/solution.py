def isValid(s: str) -> bool:
    stack = []
    # Mapping of closing brackets to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map.values():  # If it's one of '(', '{', '['
            stack.append(char)
        elif char in bracket_map.keys():  # If it's one of ')', '}', ']'
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()  # Pop the last opened bracket
        else:
            return False  # Invalid character
    
    return not stack  # If stack is empty, return True; otherwise, return False