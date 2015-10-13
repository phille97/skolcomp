# -*- encoding: utf-8 -*-
#
# Vecka 42 Uppgift 1
#
# Skriv tre funktioner som beräknar summan av tal i en lista som använder en
# for-loop, en while-loop och rekursion.
#


def for_sum(sumdis):
    total = 0
    for num in sumdis:
        total += num
    return total


def while_sum(sumdis):
    total = 0
    while len(sumdis):
        total += sumdis[0]
        sumdis = sumdis[1:]
    return total


def recursive_sum(sumdis, total=0):
    if len(sumdis):
        total += sumdis[0]
        return recursive_sum(sumdis[1:], total)
    return total


numbers = range(1, 100)


print("numbers to sum is: {}\n".format(str(numbers)))

print("for loop:          {}".format(str(for_sum(numbers))))
print("while loop:        {}".format(str(while_sum(numbers))))
print("recursive loop:    {}".format(str(recursive_sum(numbers))))
print("using sum():       {}".format(str(sum(numbers))))
