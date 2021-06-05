def A(n):
    if n == 1:
        return n
    else:
        return n * A(n - 1)


def B(n):
    if n>0:
        if not (n % 2 == 0):
            return n+B(n-1)
        return 0+B(n-1)
    return 0

def C(n):
    if n > 0:
        if (n % 3 == 0):
            return n + C(n - 1)
        return 0 + C(n - 1)
    return 0


def D(n):
    if (n == 0):
        return 0
    return 2 * D(n - 1) + 3


def E(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return 3 * E(n - 1) - E(n - 2)



print(B(6))
print(C(6))

