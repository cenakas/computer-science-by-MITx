# problem 4
# Implement a function that meets the specifications below:

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    L.reverse()
    for i in L:
        i.reverse()

# problem 5
# Write a Python function that returns a list of keys in aDict with the value target. The list of keys you return should be sorted in increasing order.
# The keys and values in aDict are both integers. (If aDict does not contain the value target, you should return an empty list.)
# This function takes in a dictionary and an integer and returns a list.
def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    keys = []
    for key, value in aDict.items():
        if value == target:
            keys.append(key)
    keys_sorted = sorted(keys)
    return keys_sorted

# problem 6
# Write a recursive Python function, given a non-negative integer N, to calculate and return the sum of its digits.
# Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6), while doing integer division by 10 removes the rightmost digit (126 // 10 is 12).
# This function has to be recursive; you may not use loops!
# This function takes in one integer and returns one integer.
def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    if N < 10:
        return N
    else:
        return sumDigits(N % 10) + sumDigits(N // 10)

# problem 7
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    L_copy = L[:]
    for i in L_copy:
        if f(i) is not True:
            L.remove(i)
    return len(L)

run_satisfiesF(L, satisfiesF)
