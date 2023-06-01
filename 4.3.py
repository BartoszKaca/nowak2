def f(n):
    if n == 2:
        return 2
    elif n>1:
        return 3*n + f(n-1)
    
def g(n):
    if n == 0 or n == 1:
        return 1
    elif n >1:
        return 2*g(n-2)-g(n-1)
def h(n):
    if n == 1:
        return 1
    elif n>1:
        return h(n-1)* (n-1)-n
def w(n, a):
    if n == 1:
        return 0
    elif n >1:
        return n *a + w(n-1,a)
def t(n,a,b):
    if n == 1:
        return 1
    elif n >1:
        return n *a -b +t(n-1,b,a)