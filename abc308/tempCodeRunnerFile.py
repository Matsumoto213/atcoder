def remove_parentheses(s):
    stack_parentheses = []
    stack_result = []

    for i, c in enumerate(s):
        if c == '(':
            stack_parentheses.append(i)
            stack_result.append((c, i))
        elif c == ')':
            if stack_parentheses:
                start = stack_parentheses.pop()
                while stack_result and stack_result[-1][1] >= start:
                    stack_result.pop()
                if not stack_result or stack_result[-1][1] < start:
                    stack_result.append((c, i))
        else:
            stack_result.append((c, i))

    return ''.join(c for c, _ in stack_result)

N = int(input())
S = input()
print(remove_parentheses(S))
