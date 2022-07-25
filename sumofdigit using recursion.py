# 2022-02-22 01:10:44.972670
# sum of digits example 12 = 1+ 2 = 3

def sumofdigits(n):

    if n == 0:
        return 0
    else:
        return int(n % 10) + sumofdigits(n / 10)


print(sumofdigits(123))
