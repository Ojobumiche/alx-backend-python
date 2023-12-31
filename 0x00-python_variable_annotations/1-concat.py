#!/usr/bin/env python3


'''This module concatenates two strings'''


def concat(str1: str, str2: str) -> str:
    '''A function that concatenates 2 strings'''
    return str1 + str2


if __name__ == '__main__':

    str1 = 'Joshua'
    str2 = 'Monday'

    print(concat(str1, str2) == "{}{}".format(str1, str2))
    print(concat.__annotations__)
