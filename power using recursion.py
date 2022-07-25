# power using recursion example x²

def power(base, expo):
    assert expo > -1 and int(expo) == expo, 'The power must be non-negative and integer'
    if expo in [0]:
        return base
    if expo in [1]:
        return base

    return base * power(base, expo - 1)


print(power(2, 0))
