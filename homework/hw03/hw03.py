HW_SOURCE_FILE = __file__


def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
    if pos == 8:
        return 1
    elif pos // 10 == 0:
        return 0
    return 1+num_eights(pos//10) if pos % 10 == 8 else num_eights(pos//10)

    # alternative solution (more clearer)
    if pos % 10 == 8:
        return 1 + num_eights(pos // 10)
    elif pos < 10:
        return 0
    else:
        return num_eights(pos // 10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
    # alternative solution - From beginning to end
    def helper(result, i, step):
        if i == n:
            return result
        elif i % 8 == 0 or num_eights(i) > 0:
            return helper(result - step, i + 1, -step)
        else:
            return helper(result + step, i + 1, step)
    return helper(1, 1, 1)

    # MY DUMB SOLUTION - reversed
    def count8(n):
        if n < 8:
            return 0
        if n == 8:
            return 1
        return 1+count8(n-1) if n % 8 == 0 or num_eights(n) else count8(n-1)

    def swap_order(n, order):
        if n % 8 == 0 or num_eights(n) > 0:
            return abs(order-1)
        return order

    def func(n, order):
        if n <= 8:
            return n
        if swap_order(n, order) == 1:
            return func(n-1, 1) + 1
        else:
            return func(n-1, 0) - 1
    return func(n, abs(count8(n) % 2-1))


def get_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> get_larger_coin(1)
    5
    >>> get_larger_coin(5)
    10
    >>> get_larger_coin(10)
    25
    >>> get_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def get_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> get_smaller_coin(25)
    10
    >>> get_smaller_coin(10)
    5
    >>> get_smaller_coin(5)
    1
    >>> get_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def devide(change, largest_coin):
        if change < 0:
            return 0
        if change < 5 or largest_coin == 1:
            return 1
        return devide(change-largest_coin, largest_coin)+devide(change, get_smaller_coin(largest_coin))
    return devide(change, 25)
    # not necessary to discuss
    if change >= 25:
        return devide(change, 25)
    elif change >= 10:
        return devide(change, 10)
    elif change >= 5:
        return devide(change, 5)
    return 1

    # alternative solution by counting up

    def constrained_count(change, smallest_coin):
        if change == 0:
            return 1
        if change < 0:
            return 0
        if smallest_coin == None:
            return 0
        without_coin = constrained_count(
            change, get_larger_coin(smallest_coin))
        with_coin = constrained_count(change - smallest_coin, smallest_coin)
        return without_coin + with_coin
    return constrained_count(change, 1)

# optional


def collapse(n):
    """Fall 2017 MT1 Q4a: Digital"""

    """For non-negative N, the result of removing all digits that are equal
    to the digit on their right, so that no adjacent digits are the same.
    >>> collapse(1234)
    1234
    >>> collapse(12234441)
    12341
    >>> collapse(0)
    0
    >>> collapse(3)
    3
    >>> collapse(11200000013333)
    12013
    """
    left, last = n // 10, n % 10
    if n < 10:
        return last
    elif left % 10 == last:
        return collapse(left)
    else:
        return collapse(left) * 10 + last


def repeat_digits(n):
    """Summer 2018 MT1 Q5a: Won't You Be My Neighbor?"""

    """Given a positive integer N, returns a number with each digit repeated.
    >>> repeat_digits(1234)
    11223344
    """
    last, rest = n % 10*11, n//10
    if n < 10:
        return n
    return repeat_digits(rest)*100+last


def contains(a, b):
    """Fall 2019 Final Q6b: Palindromes

    Implement contains, which takes non-negative integers a and b. It returns whether all of the
    digits of a also appear in order among the digits of b.

    Important: You may not write str, repr, list, tuple, [, or ]"""

    """Return whether the digits of a are contained in the digits of b.
    >>> contains(357, 12345678)
    True
    >>> contains(753, 12345678)
    False
    >>> contains(357, 37)
    False
    """
    if a == b:
        return True
    if a > b:
        return False
    if a % 10 == b % 10:
        return contains(a//10, b//10)
    else:
        return contains(a, b//10)