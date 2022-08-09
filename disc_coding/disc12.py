# Q3: Maximum Subsequence
def max_subseq(n, t):
    """
    Return the maximum subsequence of length at most t that can be found in the given number n.
    For example, for n = 2012 and t = 2, we have that the subsequences are
        2
        0
        1
        2
        20
        21
        22
        01
        02
        12
    and of these, the maxumum number is 22, so our answer is 22.

    >>> max_subseq(2012, 2)
    22
    >>> max_subseq(25432, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    >>> from construct_check import check
    >>> # ban usage of str
    >>> check(LAB_SOURCE_FILE, 'max_subseq', ['Str', 'Slice'])
    True
    """
    "*** YOUR CODE HERE ***"
    # solution
    if n == 0 or t == 0:
        return 0
    with_last = max_subseq(n // 10, t - 1) * 10 + n % 10
    without_last = max_subseq(n // 10, t)
    return max(with_last, without_last)


#Q4: Reverse
def reverse(lst):
    """Reverses lst using mutation.

    >>> original_list = [5, -1, 29, 0]
    >>> reverse(original_list)
    >>> original_list
    [0, 29, -1, 5]
    >>> odd_list = [42, 72, -8]
    >>> reverse(odd_list)
    >>> odd_list
    [-8, 72, 42]
    """
    "*** YOUR CODE HERE ***"
    l = len(lst)
    for i in range(l//2):
        tmp = lst[i]
        lst[i] = lst[l-i-1]
        lst[l-i-1] = tmp
    """ withou tmp
    for i in range(l//2):
        lst[i], lst[last - i] = lst[last - i], lst[i] """


# Q6: Level Mutation
def level_mutation(t, funcs):
    """Mutates t using the functions in the list funcs.

    >>> t = Tree(1, [Tree(2, [Tree(3)])])
    >>> funcs = [lambda x: x + 1, lambda y: y * 5, lambda z: z ** 2]
    >>> level_mutation(t, funcs)
    >>> t                               # funcs[0] was applied to the label 1, funcs[1] to the label 2, etc.
    Tree(2, [Tree(10, [Tree(9)])])
    >>> t2 = Tree(1, [Tree(2), Tree(3, [Tree(4)])])
    >>> level_mutation(t2, funcs)
    >>> t2                              # (2 * 5) ** 2 = 100
    Tree(2, [Tree(100), Tree(15, [Tree(16)])])
    >>> t3 = Tree(1, [Tree(2)])
    >>> level_mutation(t3, funcs)
    >>> t3
    Tree(2, [Tree(100)])
    """
    if len(funcs) == 0:
        return
    t.label = funcs[0](t.label)
    remaining = len(funcs)
    if t.is_leaf() and remaining:
        for i in range(1, remaining):
            t.label = funcs[i](t.label)
    for b in t.branches:
        level_mutation(b, funcs[1:])
# extra: if t is LINK list
def level_mutation_link(t, funcs):
    if not funcs.rest:
        return
    t.label = funcs.first(t.label)
    remaining = funcs.rest
    if t.is_leaf() and remaining:
        while remaining:
            t.label = remaining.first(t.label)
            remaining = remaining.rest
    for b in t.branches:
        level_mutation_link(b, remaining)


# Q7: Multiply Links
def multiply_lnks(lst_of_lnks):
    """
     a = Link(2, Link(3, Link(5)))
     b = Link(6, Link(4, Link(2)))
     c = Link(4, Link(1, Link(0, Link(2))))
     p = multiply_lnks([a, b, c])
     p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # Implementation Note: you might not need all lines in this skeleton code
    p = Link(1)
    for i in range(len(lst_of_lnks)):
        if not lst_of_lnks[i]:
            return Link.empty
        lst_of_lnks[i], p.first = lst_of_lnks[i].rest, p.first * \
            lst_of_lnks[i].first
    p.rest = multiply_lnks(lst_of_lnks)
    return p

    # Alternate iterative approach
    import operator
    from functools import reduce

    def prod(factors):
        return reduce(operator.mul, factors, 1)

    head = Link.empty
    tail = head
    while Link.empty not in lst_of_lnks:
        all_prod = prod([l.first for l in lst_of_lnks])
        if head is Link.empty:
            head = Link(all_prod)
            tail = head
        else:
            tail.rest = Link(all_prod)
            tail = tail.rest
        lst_of_lnks = [l.rest for l in lst_of_lnks]
    return head


#Q10: Greetings
import re

def greetings(message):
    """
    Returns whether a string is a greeting. Greetings begin with either Hi, Hello, or
    Hey (first letter either capitalized or lowercase), and/or end with Bye (first letter 
    either capitalized or lowercase) optionally followed by an exclamation point or period.

    >>> greetings("Hi! Let's talk about our favorite submissions to the Scheme Art Contest")
    True
    >>> greetings("Hey I love Taco Bell")
    True
    >>> greetings("I'm going to watch the sun set from the top of the Campanile! Bye!")
    True
    >>> greetings("Bye Bye Birdie is one of my favorite musicals.")
    False
    >>> greetings("High in the hills of Berkeley lived a legendary creature. His name was Oski")
    False
    >>> greetings('Hi!')
    True
    >>> greetings("bye")
    True
    """
    return bool(re.search(r"(^([Hh](ey|i|ello)\b))|(\b[Bb]ye[!\.]?$)", message))

