def valid_parentheses(s):
    stack = []
    if len(s) % 2 != 0:
        return False
    if len(s) == 0:
        return True
    if s[0] in ")]}":
        return False
    for c in s:
        if c in "([{":
            stack.append(c)
        else:
            if not stack:
                return False
            if c == ")" and stack[-1] != "(":
                return False
            if c == "]" and stack[-1] != "[":
                return False
            if c == "}" and stack[-1] != "{":
                return False
            stack.pop()
    return not stack
