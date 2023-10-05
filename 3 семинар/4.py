a=list(input().split())
n=int(a[0])
s=a[1]
def tre(size, symb):
    for i in range(1, size+1):
        print(symb*min(i, size - i +1))
tre(n, s)