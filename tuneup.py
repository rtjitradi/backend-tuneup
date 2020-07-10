#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = "Reggy Tjitradi guided by Daniel's yesterday study hall (July 8th), Ramon Hamilton, and Howard Post"

import cProfile
import pstats
import functools
from collections import Counter


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    # Be sure to review the lesson material on decorators.
    # You need to understand how they are constructed and used.
    # For the syntax below refer to https://docs.python.org/3/library/profile.html and to help understanding tutorial video of cProfile https://www.youtube.com/watch?v=8qEnExGLZfY&t=412s
    def profile_func(*args, **kwargs):  # creating decorator (function that passed another function for more functionalities)
        pr = cProfile.Profile()
        #  try/except/else/finally, refer to this doc https://docs.python.org/3/tutorial/errors.html (8.6)
        try:
            pr.enable()
            result = func(*args, **kwargs)
            pr.disable()
            return result
        finally:
            ps = pstats.Stats(pr).sort_stats(pstats.SortKey.CUMULATIVE)
            ps.print_stats()
    return profile_func


def read_movies(src):
    """Returns a list of movie titles."""
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Returns True if title is within movies list."""
    for movie in movies:
        if movie == title:
            return True
    return False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    duplicates = Counter()
    for movie in movies:
        duplicates[movie] += 1
    return duplicates


def timeit_helper(func):
    """Part A: Obtain some profiling measurements using timeit."""
    #  Refer to https://docs.python.org/3/library/timeit.html
    t = timeit.Timer(stmt=func)
    result = t.repeat(repeat=7, number=4)
    min_value = min([result/3 for result in results])
    print("best time across 7 repeats of 4 runs per repeat: ", min_value)


def main():
    """Computes a list of duplicate movie entries."""
    duplicates = []
    result = find_duplicate_movies('movies.txt')
    for keys, values in result.items():
        if values > 1:
            duplicates.append(keys)
    print(f'Found {len(duplicates)} duplicate movies:')
    print('\n'.join(result))


if __name__ == '__main__':
    main()
