str = input()
lifo = []
str_out = ''

for i in range(len(str) - 1, -1, -1):
    if str[i] not in '+-*/()':
        str_out = str_out + ' ' + str[i]

    elif str[i] == ")":
        lifo.append(str[i])

    elif str[i] == "(":
        while len(lifo) > 0 and lifo[-1] != ")":
            str_out = str_out + ' ' + lifo[-1]
            lifo.pop(-1)
        lifo.pop(-1)

    elif str[i] in "*/":
        if len(lifo) == 0 or lifo[-1] == ")":
            lifo.append(str[i])
        else:
            if lifo[-1] in "+-":
                lifo.append(str[i])
            else:
                while len(lifo) > 0 and lifo[-1] not in "+-)":
                    str_out = str_out + ' ' + lifo[-1]
                    lifo.pop()
                lifo.append(str[i])

    elif str[i] in "+-":
        if len(lifo) == 0 or lifo[-1] == ")":
            lifo.append(str[i])
        else:
            while len(lifo) > 0 and lifo[-1] != ')':
                str_out = str_out + ' ' + lifo[-1]
                lifo.pop(-1)
            lifo.append(str[i])

if len(lifo) != 0:
    for i in range(1, len(lifo) + 1):
        str_out = str_out + ' ' + lifo[-i]

str_out = str_out[::-1]
print('прямая польская нотация', str_out)
str_out2 = ''
lifo2 = []
for i in range(len(str)):

    if str[0] not in '+-*/()':
        str_out2 = str_out2 + ' ' + str[0]
        str = str[1:]

    elif str[0] in '*/':
        lifo2.append(str[0])
        str = str[1:]

    elif str[0] == '+':
        while (len(lifo2) > 0 and lifo2[-1] in '*/'):
            str_out2 = str_out2 + ' ' + lifo2[-1]
            lifo2.pop(-1)
        lifo2.append(str[0])
        str = str[1:]

    elif str[0] == '-':
        while (len(lifo2) > 0 and lifo2[-1] in '*/+'):
            str_out2 = str_out2 + ' ' + lifo2[-1]
            lifo.pop(-1)
        lifo2.append(str[0])
        str = str[1:]

    elif str[0] == '(':
        lifo2.append(str[0])
        str = str[1:]

    elif str[0] == ')':
        while lifo2[-1] != '(':
            str_out2 = str_out2 + ' ' + lifo2[-1]
            lifo2.pop(-1)
        lifo2 = lifo2[:-1]
        str = str[1:]

lifo2.reverse()
for i in range(len(lifo2)):
    str_out2 = str_out2 + ' ' + lifo2[i]

print('обратная польская нотация', str_out2)
