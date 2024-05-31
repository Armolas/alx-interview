#!/usr/bin/python3
"""
    This module contains the pascal triangle function
    """


def pascal_triangle(n):
    """This fuction returns an array of arrays \
    that represents a pascal triangle"""
    triangle = []
    i = 1
    while (i <= n):
        array = []
        j = 0
        while j < i:
            if (j == 0) or (j == i - 1):
                array.append(1)
            else:
                num = triangle[i - 2][j - 1] + triangle[i - 2][j]
                array.append(num)
            j += 1
        triangle.append(array)
        i += 1
    return triangle
