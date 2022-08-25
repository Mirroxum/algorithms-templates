line = input()
stack = []
d = {
    '[': ']',
    '(': ')',
    '{': '}'
}
for char in line:
    if char in d:
        stack.append(char)
    elif stack != [] and char == d[stack[-1]]:
        stack.pop()
    else:
        stack.append(char)
        break
if not stack:
    print(True)
else:
    print(False)