def remove_parentheses(s):
    stack = []
    removed = []

    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if stack:
                start = stack.pop()
                removed.extend(range(start, i + 1))
                print(start,removed,i)
    removed = set(removed)
    return ''.join(c for i, c in enumerate(s) if i not in removed)

N = int(input())
S = input()
print(remove_parentheses(S))
