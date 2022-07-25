#2022-02-22 00:25:42.777953
#fibonacci

def fibonacii(n):
    assert n>=0 and  int(n)==n,'Fibonacci number cannot be negative or non integer.'
    if n in [0,1] :
        return n
    else:
        return fibonacii(n-1)+fibonacii(n-2)

print(fibonacii(50))
