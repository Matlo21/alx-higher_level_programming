#!/usr/bin/python3
"""Defines a text-indentation function"""


def text_indentation(text):
    """Function puts in a new line if it detects a . or ? or :
    Args:
        text: the string to look through
    Return:
        Nothing
    """
    flag = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if flag == 1 and i is ' ':
            print('', end='')
            flag = 0
            continue
        if i is '.' or i is '?' or i is ':':
            print("{}\n".format(i))
            flag = 1
        else:
            print(i, end='')
            flag = 0
