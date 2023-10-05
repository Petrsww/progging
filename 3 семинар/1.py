def fib(n, fibs):
    if n==1:
        fibs[0]=0
        return 0
    if n==2:
        fibs[1]=1
        return 1
    if fibs[n-1]!=0:
        return fibs[n-1]
    fibs[n-1]=fib(n-1, fibs)+fib(n-2, fibs)
    return fibs[n-1]
N=int(input())
fibs = [0 for i in range(N)]
print(fib(N, fibs))