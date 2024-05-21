import sys
import random
import string


def write_stuf_to_file_for_perf_test():
    target = open('tgt.txt', 'w')
    for i in range(4000000):
        target.write(f'{str(i)}\n')
        # print(i)


# b = 'A'
# for i in range(100):
#     b += random.choice(string.ascii_letters)
#     print(b)
#     print(f'size: {sys.getsizeof(b)}')
# for i in dir(a):
#     print(i)
# print(ord('c'))

# import functools
# def m_f(some_l):
#     return some_l+1
#
#
# m_l = [1, 2, 3, 4, 5, 6, 7]
# # print(list(filter(m_f, m_l)))
# print(help(filter))
# print('********************************************************************************************************************************************************************************************************')
#
# print(help(map))
# print('********************************************************************************************************************************************************************************************************')
#
# print(help(functools.reduce))
from typing import Sequence


def seq_printer(seq: Sequence):
    for i in seq:
        print(i)


def generator_for_matrix_print():
    pepes = ['Pepega', 'Pepe', 'PepePls']
    sizes = ['Large', 'Medium', 'Small', 'Microscopic']
    shackles = ['round', 'square', 'ellipsoidal']

    some_l = [(size, pepe, shackle) for pepe in pepes for shackle in shackles for size in sizes]
    # some_l = [(size, pepe, shackle) for shackle in shackles for size in sizes for pepe in pepes]
    # some_l = [(size, pepe, shackle) for shackle in shackles for pepe in pepes  for size in sizes]
    for i in some_l:
        print(i)
    print(some_l)


def some_match_case_destructuring():
    from dataclasses import dataclass
    from random import uniform

    @dataclass
    class Pepe:
        id: int
        name: str
        some_metadata: list
        internal_value: float

    list_of_pepes = []
    for i in range(10):
        list_of_pepes.append(Pepe(id=i, name=f"Pepe #{i}", some_metadata=[("p_cnt" + '_')*i],
                                  internal_value=i+round(uniform(1, 100), 3)))

    seq_printer(list_of_pepes)

    for pepe in list_of_pepes:
        match pepe:
            case Pepe(p_id, p_internal_value, _) if p_id > 3:
                print(pepe)
                print(p_id, p_internal_value)

def counter(symbol_to_count):
    # Define the string
    my_string = "Hello, World! How are you?"

    # Define the symbol to count

    # Count the occurrences of the symbol in the string
    count = my_string.count(symbol_to_count)

    # Print the count
    print(f"The symbol '{symbol_to_count}' appears in the string '{my_string}' {count} times.")

import random

from pprint import pprint
def tuple_spawn():
    table = tuple(tuple(random.randint(1000, 10_000) for _ in range(10)) for _ in range(5))
    pprint(table)


if __name__ == "__main__":
    tuple_spawn()
    # some_match_case_destructuring()
    #print(len('https___storage.yandexcloud.net_log-reposts-alpha-prod_'))
