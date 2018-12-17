# problem 3
# McDonald’s sells Chicken McNuggets in packages of 6, 9 or 20 McNuggets. Thus, it is possible, for example, to buy exactly 15 McNuggets
# (with one package of 6 and a second package of 9), but it is not possible to buy exactly 16 McNuggets,
# since no non- negative integer combination of 6's, 9's and 20's add up to 16. To determine if it is possible to buy exactly n McNuggets,
# one has to find non-negative integer (can be 0) values of a, b, and c such that: y6a + 9b + 20c = n
# Write a function, called McNuggets that takes one argument, n, and returns True if it is possible to buy a combination of 6, 9
# and 20 pack units such that the total number of McNuggets equals n, and otherwise returns False. Hint: use a guess and check approach.
def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """

    if n == 0:
       return True
    if n < 0:
       return False

    return McNuggets(n-6) or McNuggets(n-9) or McNuggets(n-20)
    return False

# problem 4
# Write a Python function that takes in two lists and calculates whether they are permutations of each other.
# The lists can contain both integers and strings. We define a permutation as follows:
# the lists have the same number of elements
# list elements appear the same number of times in both lists
# If the lists are not permutations of each other, the function returns False.  If they are permutations of each other,
# the function returns a tuple consisting of the following elements: the element occuring the most times, how many times that element occurs,
# the type of the element that occurs the most times
# If both lists are empty return the tuple (None, None, None). If more than one element occurs the most number of times, you can return any of them.
def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    '''
    L1_copy = L1[:]
    try:
        for e in L2:
            L1.remove(e)
        if len(L1) != 0:
            return False
        elif len(L1_copy) == 0:
            return (None, None, None)
    except:
        return False
    else:
        D = {L1_copy.count(e): e for e in L1_copy}
        key = max([x for x in D.keys()])
        return (D[key], key, type(D[key]))

# problem 5
def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain
                          N unique lowercase letters.
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where
        each key is a letter in map_from at index i and the corresponding
        value is the letter in map_to at index i.
        decoded is a string that contains the decoded version
        of code using the key_code mapping. """
    key_code = {}
    decoded = ''
    for i in range(len(map_from)):
        key_code[map_from[i]] = map_to[i]

    for i in code:
        decoded += key_code[i]

    return (key_code,decoded)
