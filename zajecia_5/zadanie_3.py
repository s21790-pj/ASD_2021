A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = [7, 8, 9, 10]
C = 'siemanko'


def head(A):
    return A[0]


def tail(A):
    return A[1:]


def isEmpty(A):
    if not A:
        return True
    else:
        return False


def reversWord(word):
    if len(word) == 0:
        return word
    else:
        return reversWord(word[1:]) + head(word)


def sameElements(A, B):
    if not (isEmpty(A) or isEmpty(B)):
        if head(A) < head(B):
            sameElements(B, A)
        else:
            if head(A) == head(B):
                print(head(A))
                sameElements(tail(A), tail(B))
            else:
                if head(A) in tail(B):
                    print(head(A))
                sameElements(tail(A), tail(B))
    else:
        return False


sameElements([], [])
