#!/usr/bin/env python3


'''a module that takes a float as argument and returns a string'''


def to_str(n: float) -> str:
    '''This a function that returns the string quivalent of any float argument'''
    return str(n)
    
    print(f'to_str(3.142)')
    print(f'to_str(0.00)')


if __name__ == '__main__':

    print(to_str.__annotations__)
