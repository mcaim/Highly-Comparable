__author__ = 'Aidan McRitchie, mcaim@live.unc.edu, Onyen = mcaim'

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,67,71,73,79,83,89,97]
MAXN = 10 ** 27

possible_hcn = []


def gen_possible_hcn(exponents):
    l = len(exponents)

    if l == len(primes):
        return

    n = 1
    div = 1
    for i in range(l):
        n *= pow(primes[i], exponents[i])
        div *= exponents[i] + 1

    if n > MAXN:
        return

    possible_hcn.append([n, div, exponents])

    MAXE = 60
    if l >= 1:
        MAXE = exponents[l - 1]

    for e in range(1, MAXE + 1):
        exponents_new = exponents.copy()
        exponents_new.append(e)
        gen_possible_hcn(exponents_new)


gen_possible_hcn([])
print("Number of candidates for being highly composite is", len(possible_hcn), "\n")

# Selecting hcn from possible_hcn
possible_hcn.sort()
hcn = [[1, 1, []]]

for i in range(1, len(possible_hcn)):
    if possible_hcn[i][1] > hcn[-1][1]:
        hcn.append(possible_hcn[i])

# Printing hcn
print("Number of highly composite numbers less than", MAXN, "is", len(hcn), "\n")


def PrintWithCorrectSpaces(a, b, c):
    aspace = 30
    bspace = 25
    assert (len(a) < aspace)
    assert (len(b) < bspace)

    print(a, " " * (aspace - len(a)), b, " " * (bspace - len(b)), c)


PrintWithCorrectSpaces("number", "divisors", "factorization")

for el in hcn:
    factorization = "*".join(
        [str(primes[i]) + ("^" + str(el[2][i]) if el[2][i] > 1 else "") for i in range(len(el[2]))])

    PrintWithCorrectSpaces(str(el[0]), str(el[1]), factorization)