#!/bin/python3
'''
Python provides built-in sort/sorted functions that use timsort internally.
You cannot use these built-in functions anywhere in this file.

Every function in this file takes a comparator `cmp` as input
which controls how the elements of the list should be
compared against each other:
If cmp(a, b) returns -1, then a < b;
if cmp(a, b) returns  1, then a > b;
if cmp(a, b) returns  0, then a == b.
'''

import random


def cmp_standard(a, b):
    '''
    used for sorting from lowest to highest

    >>> cmp_standard(125, 322)
    -1
    >>> cmp_standard(523, 322)
    1
    '''
    if a < b:
        return -1
    if b < a:
        return 1
    return 0


def cmp_reverse(a, b):
    '''
    used for sorting from highest to lowest

    >>> cmp_reverse(125, 322)
    1
    >>> cmp_reverse(523, 322)
    -1
    '''
    if a < b:
        return 1
    if b < a:
        return -1
    return 0


def cmp_last_digit(a, b):
    '''
    used for sorting based on the last digit only

    >>> cmp_last_digit(125, 322)
    1
    >>> cmp_last_digit(523, 322)
    1
    '''
    return cmp_standard(a % 10, b % 10)


def _merged(xs, ys, cmp=cmp_standard):
    '''
    Assumes that both xs and ys are sorted,
    and returns a new list containing the elements of both xs and ys.
    Runs in linear time.

    NOTE:
    In python, helper functions are
    frequently prepended with the _.
    This is a signal to users of a library that these
    functions are for "internal use only",
    and not part of the "public interface".

    This _merged function could be implemented as
    a local function within the merge_sorted scope
    rather than a global function.
    The downside of this is that the function
    can then not be tested on its own.
    Typically, you should only implement a
    function as a local function if it cannot function on its own
    (like the go functions from binary search).
    If it's possible to make a function stand-alone,
    then you probably should do that and write
    test cases for the stand-alone function.

    >>> _merged([1, 3, 5],[2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    '''
    i = z = 0
    final_list = []

    while i < len(xs) and z < len(ys):
        result = cmp(xs[i], ys[z])
        if result == -1:
            final_list.append(xs[i])
            i += 1
        if result == 1:
            final_list.append(ys[z])
            z += 1
        if result == 0:
            final_list.append(xs[i])
            final_list.append(ys[z])
            i += 1
            z += 1

    while i < len(xs):
        final_list.append(xs[i])
        i += 1
    while z < len(ys):
        final_list.append(ys[z])
        z += 1

    return final_list


def merge_sorted(xs, cmp=cmp_standard):
    '''
    Merge sort is the standard O(n log n) sorting algorithm.
    Recall that the merge sort pseudo code is:

        if xs has 1 element
            it is sorted, so return xs
        else
            divide the list into two halves left,right
            sort the left
            sort the right
            merge the two sorted halves

    You should return a sorted version of the input list xs.
    You should not modify the input list xs in any way.
    '''

    if len(xs) <= 1:
        return xs
    else:
        middle = len(xs) // 2
        left = xs[:middle]
        right = xs[middle:]
        left_sort = merge_sorted(left, cmp)
        right_sort = merge_sorted(right, cmp)
        return _merged(left_sort, right_sort, cmp)


def quick_sorted(xs, cmp=cmp_standard):
    '''
    Quicksort is like mergesort,
    but it uses a different strategy to split the list.
    Instead of splitting the list down the middle,
    a "pivot" value is randomly selected,
    and the list is split into a "less than"
    sublist and a "greater than" sublist.

    The pseudocode is:

        if xs has 1 element
            it is sorted, so return xs
        else
            select a pivot value p
            put all the values less than p in a list
            put all the values greater than p in a list
            put all the values equal to p in a list
            sort the greater/less than lists recursively
            return the concatenation of
            (less than, equal, greater than)

    and the list is split into a "less than"
    sublist and a "greater than" sublist.

    The pseudocode is:

        if xs has 1 element
            it is sorted, so return xs
        else
            select a pivot value p
            put all the values less than p in a list
            put all the values greater than p in a list
            put all the values equal to p in a list
            sort the greater/less than lists recursively
            return the concatenation of (less than, equal, greater than)

            sort the left
            sort the right
            merge the two sorted halves

    You should return a sorted version of the input list xs.
    You should not modify the input list xs in any way.
    '''
    if len(xs) <= 1:
        return xs
    else:
        pivot_index = random.randint(0, len(xs) - 1)
        pivot = xs[pivot_index]
        more = []
        less = []
        same = []

        for val in list(xs):
            test = cmp(val, pivot)
            if test == -1:
                less.append(val)
            if test == 1:
                more.append(val)
            if test == 0:
                same.append(val)

        less_sort = quick_sorted(less, cmp)
        more_sort = quick_sorted(more, cmp)
        final = less_sort + same + more_sort
        return (final)
