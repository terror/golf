"""sum all even numbers in a list"""
def sum_even(l): return sum(list(filter(lambda x: x & 1 == 0, l)))

"""sum all odd numbers in a list"""
def sum_odd(l): return sum(list(filter(lambda x: x & 1, l)))
