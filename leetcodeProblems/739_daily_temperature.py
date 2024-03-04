def dailyTemperatures(temperatures):
    stack = []
    res = [0] * len(temperatures)
    for i in range(len(temperatures)):
        if not stack:
            stack.append(i)
        else:
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
    return res
    