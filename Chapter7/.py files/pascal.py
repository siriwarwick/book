n = 30
mod = 2

def binom(n,k):
    a = 1
    for i in range(k):
        a = a*(n-i)//(i+1)        
    return a

def symb(u):
    if u==0:
        return "\u25A1"
    else:
        return "\u25A0"

for i in range(n+1):
    for j in range(0, n-i+1):
        print(' ', end='') 
    for j in range(i+1):
        u = binom(i,j) % mod
        s = symb(u)
        print(' ', s, sep='', end='') 
    print('')
