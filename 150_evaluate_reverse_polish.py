def evalRPN(tokens):
    stack = []
    operators = set(['+', '-', '*', '/'])
    for token in tokens:
        if token in operators:
            b, a = stack.pop(), stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:
                stack.append(int(float(a) / b))
        else:
            stack.append(int(token))
    return stack.pop()

def main():
    print(evalRPN(["2", "1", "+", "3", "*"]))
    print(evalRPN(["4", "13", "5", "/", "+"]))
    print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

if __name__ == "__main__":
    main()