str_input = input()
s = list(str_input.split())
res = []

for i in range(len(s)):
    if s[i] not in '+-*/':
        res.append(int(s[i]))
    elif s[i] == '+':
        a = res.pop()
        b = res.pop()
        res.append(a + b)
    elif s[i] == '-':
        a = res.pop()
        b = res.pop()
        res.append(b - a)
    elif s[i] == '*':
        a = res.pop()
        b = res.pop()
        res.append(a * b)
    elif s[i] == '/':
        a = res.pop()
        b = res.pop()
        res.append(b / a)

print(res[0])
