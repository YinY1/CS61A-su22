from json.encoder import INFINITY
from operator import add, mul
from os import stat


def square(x): return x * x


def identity(x): return x


def triple(x): return 3 * x


def increment(x): return x + 1


HW_SOURCE_FILE = __file__


def product(n, term):
    """Return the product of the first n terms in a sequence.

    n: a positive integer
    term:  a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    "*** YOUR CODE HERE ***"
    res = 1
    for i in range(1, n+1):
        res *= term(i)
    return res


def accumulate(merger, start, n, term):
    """Return the result of merging the first n terms in a sequence and start.
    The terms to be merged are term(1), term(2), ..., term(n). merger is a
    two-argument commutative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> # 2 + (1^2 + 1) + (2^2 + 1) + (3^2 + 1)
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    >>> # ((2 * 1^2 * 2) * 2^2 * 2) * 3^2 * 2
    >>> accumulate(lambda x, y: 2 * x * y, 2, 3, square)
    576
    >>> accumulate(lambda x, y: (x + y) % 17, 19, 20, square)
    16
    """
    "*** YOUR CODE HERE ***"
    res = start
    for i in range(1, n+1):
        res = merger(res, term(i))
    return res
# Alternative recursive solution using start to keep track of total


def accumulate3(merger, start, n, term):
    if n == 0:
        return start
    return accumulate3(merger, merger(start, term(n)), n-1, term)


def summation_using_accumulate(n, term):
    """Returns the sum: term(0) + ... + term(n), using accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    >>> # You aren't expected to understand the code of this test.
    >>> # Check that the bodies of the functions are just return statements.
    >>> # If this errors, make sure you have removed the "***YOUR CODE HERE***".
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(summation_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    return accumulate(add, 0, n, term)


def product_using_accumulate(n, term):
    """Returns the product: term(1) * ... * term(n), using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    >>> # You aren't expected to understand the code of this test.
    >>> # Check that the bodies of the functions are just return statements.
    >>> # If this errors, make sure you have removed the "***YOUR CODE HERE***".
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(product_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    return accumulate(mul, 1, n, term)


def filtered_accumulate(merger, start, cond, n, term):
    """Return the result of merging the terms in a sequence of N terms
    that satisfy the condition cond. merger is a two-argument function.
    If v1, v2, ..., vk are the values in term(1), term(2), ..., term(N)
    that satisfy cond, then the result is
         start merger v1 merger v2 ... merger vk
    (treating merger as if it were a binary operator, like +). The
    implementation uses accumulate.

    >>> filtered_accumulate(add, 0, lambda x: True, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> filtered_accumulate(add, 11, lambda x: False, 5, identity) # 11
    11
    >>> filtered_accumulate(add, 0, odd, 5, identity)   # 0 + 1 + 3 + 5
    9
    >>> filtered_accumulate(mul, 1, greater_than_5, 5, square)  # 1 * 9 * 16 * 25
    3600
    >>> # Do not use while/for loops or recursion
    >>> from construct_check import check
    >>> # ban iteration and recursion
    >>> check(HW_SOURCE_FILE, 'filtered_accumulate', ['While', 'For', 'Recursion'])
    True
    """
    def merge_if(x, y):
        "*** YOUR CODE HERE ***"
        if cond(y):
            return merger(x, y)
        else:
            return x
    return accumulate(merge_if, start, n, term)


def odd(x):
    return x % 2 == 1


def greater_than_5(x):
    return x > 5


def funception(func_a, start):
    """ Takes in a function (function A) and a start value.
    Returns a function (function B) that will find the product of
    function A applied to the range of numbers from
    start (inclusive) to stop (exclusive)

    >>> def func_a(num):
    ...     return num + 1
    >>> func_b1 = funception(func_a, 0)
    >>> func_b1(3)    # func_a(0) * func_a(1) * func_a(2) = 1 * 2 * 3 = 6
    6
    >>> func_b2 = funception(func_a, 1)
    >>> func_b2(4)    # func_a(1) * func_a(2) * func_a(3) = 2 * 3 * 4 = 24
    24
    >>> func_b3 = funception(func_a, 3)
    >>> func_b3(2)    # Returns func_a(3) since start > stop
    4
    >>> func_b4 = funception(func_a, -2)
    >>> func_b4(-3)    # Returns None since start < 0
    >>> func_b5 = funception(func_a, -1)
    >>> func_b5(4)    # Returns None since start < 0
    """
    "*** YOUR CODE HERE ***"
    def func_b(stop):
        if start < 0:
            return None
        if start > stop:
            return func_a(start)
        ret = 1
        cur = start
        while cur < stop:
            ret *= func_a(cur)
            cur += 1
        return ret
    return func_b


"""You Again"""

def parabola(x):
    """A parabola function (for testing the again function)."""
    return (x-3) * (x-6)


def vee(x):
    """A V-shaped function (for testing the again function)."""
    return abs(x-2)


def again(f):
    """Return the smallest non-negative integer n such that f(n) == f(m) for some m < n.
    >>> again(parabola) # parabola(4) == parabola(5)
    5
    >>> again(vee) # vee(1) == vee(3)
    3
    """
    n = 1
    while True:
        m = 0
        while m < n:
            if f(m) == f(n):
                return n
            m += 1
        n += 1


"""Domain onthe range"""
"""
    The domain of a function is the set of all possible argument values, while the range of a function is the set of
values that it can return. In this two part-question, you will implement higher-order functions to restrict the
domain and range of other functions.

    Implement restrict_domain, a function that accepts three parameters (f, low_d, high_d) and returns
a higher-order function that returns the same thing as f when given an argument between low_d and
high_d, inclusive, and otherwise returns float("-inf").
"""


def restrict_domain(f, low_d, high_d):
    """Returns a function that restricts the domain of F,
    a function that takes a single argument x.
    If x is not between LOW_D and HIGH_D (inclusive),
    it returns -Infinity, but otherwise returns F(x).
    >>> from math import sqrt
    >>> f = restrict_domain(sqrt, 1, 100)
    >>> f(25)
    5.0
    >>> f(-25)
    -inf
    >>> f(125)
    -inf
    >>> f(1)
    1.0
    >>> f(100)
    10.0
    """
    def foo(x):
        if x < low_d or x > high_d:
            return -INFINITY
        return f(x)
    return foo


"""
Implement restrict_range, a function that accepts three parameters (f, low_r, high_r) and returns a
higher-order function that returns the same thing as f when that result is between low_r and high_r
(inclusive), and otherwise returns float("-inf").
"""


def restrict_range(f, low_r, high_r):
    """Returns a function that restricts the range of F, a function
    that takes a single argument X. If the return value of F(X)
    is not between LOW_R and HIGH_R (inclusive), it returns -Infinity,
    but otherwise returns F(X).
    >>> cube = lambda x: x * x * x
    >>> f = restrict_range(cube, 1, 1000)
    >>> f(1)
    1
    >>> f(-5)
    -inf
    >>> f(5)
    125
    >>> f(10)
    1000
    >>> f(11)
    -inf
    """
    def foo(x):
        res = f(x)
        if res < low_r or res > high_r:
            return -INFINITY
        return res
    return foo


"""restrict_both
Now that you have those two functions defined, you’ll implement restrict_both, a higher-order function
that accepts a function f and four numeric arguments (low_d, high_d, low_r, high_r) and returns the
result of applying both restrict_domain and restrict_range on f.
"""


def restrict_both(f, low_d, high_d, low_r, high_r):
    """
    Returns a version of F with a domain restricted to (LOW_D, HIGH_D)
    and a range restricted to (LOW_R, HIGH_R).
    >>> diva = lambda x: (10000 // x) * 9
    >>> f = enforce_both(diva, 1, 1000, 100, 999)
    >>> f(0)
    -inf
    >>> f(10000)
    -inf
    >>> f(200)
    450
    >>> f(100)
    900
    >>> f(1000)
    -inf
    """
    return restrict_domain(f, low_d, high_d) or restrict_range(f, low_r, high_r)


"""The function tik takes an argument tok and returns a function insta that takes an argument gram. The
insta function prints tok and gram on the same line separated by a space and has no return statement.
Its implementation has been omitted intentionally."""


def tik(tok):
    """Returns a function that takes gram and prints tok and gram on a line.
    >>> tik(5)(6)
    5 6
    """
    def insta(gram):
        nonlocal tok
        print(tok, gram)
    return insta
