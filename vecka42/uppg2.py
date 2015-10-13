# -*- encoding: utf-8 -*-
#
# Vecka 42 Uppgift 2
#
# Givet en lista med icke-negativa heltal, arrangera talen så att de formar ett
# så stort tal som möjligt. Exempel, [50,1,2,9] ger det största talet 95021.
#

import functools


def arrange_largest(numbers):

    def comp(x, y):
        return int('{1}{0}'.format(x, y)) - int('{0}{1}'.format(x, y))

    arranged = sorted(numbers, key=functools.cmp_to_key(comp))
    return ''.join(str(x) for x in arranged)


numbers = [50, 1, 2, 9]
largest_num = arrange_largest(numbers)


print("List of Numbers: " + str(numbers))
print("Largest number:  " + largest_num)
