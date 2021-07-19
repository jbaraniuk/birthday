#Justin Baraniuk 
#February 25, 2021

import random

def has_duplicates(t):
    """Determines if a list contains duplicate values.
    t: list
    returns: boolean
    """
    s = t[::]
    s.sort()

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False

def create_bday_list(n):
    """Returns a list of integers between 1 and 365, with length n.
    n: int
    returns: list of ints
    """
    t = []
    for i in range(n):
        t.append(random.randint(1,365))
    return t

def birthday_problem(n):
    """Takes the number of students and returns an approximation
    of two people having the same birthday.
    n: int
    returns: float
    """
    count = 0
    for i in range(1000):
        t = create_bday_list(n)
        if has_duplicates(t):
            count += 1
    return count / 1000.0