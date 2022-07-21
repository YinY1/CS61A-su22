# Q1
class Pet():
    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)


class Cat(Pet):

    def __init__(self, name, owner, lives=9):
        "*** YOUR CODE HERE ***"
        super().__init__(name, owner)
        self.lives = lives

    def talk(self):
        """Print out a cat's greeting.

        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        "*** YOUR CODE HERE ***"
        print(self.name + ' says meow!')

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero,
        is_alive becomes False. If this is called after lives has
        reached zero, print 'This cat has no more lives to lose.'
        """
        "*** YOUR CODE HERE ***"
        if self.is_alive == False:
            print('This cat has no more lives to lose.')
        elif self.lives > 1:
            self.lives -= 1
        elif self.lives == 1:
            self.lives = 0
            self.is_alive = False

# Q2


class NoisyCat(Cat):  # Fill me in!
    """A Cat that repeats things twice."""
    """
    def __init__(self, name, owner, lives=9):
        # Is this method necessary? Why or why not?
        "*** YOUR CODE HERE ***"  
    """

    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        "*** YOUR CODE HERE ***"
        super().talk()
        super().talk()


# Q3
def best_k_segmenter(k, score):
    """
    >>> largest_digit_getter = best_k_segmenter(1, lambda x: x)
    >>> largest_digit_getter(12345)
    5
    >>> largest_digit_getter(245351)
    5
    >>> largest_pair_getter = best_k_segmenter(2, lambda x: x)
    >>> largest_pair_getter(12345)
    45
    >>> largest_pair_getter(245351)
    53
    >>> best_k_segmenter(1, lambda x: -x)(12345)
    1
    >>> best_k_segmenter(3, lambda x: (x // 10) % 10)(192837465)
    192
    """
    def partitioner(x): return (x//(10**k), x % (10**k))

    def best_getter(n):
        assert n > 0
        best_seg = None
        while n > 0:
            n, seg = partitioner(n)
            if best_seg == None or score(seg) > score(best_seg):
                best_seg = seg
        return best_seg
    return best_getter


# Q4
"""no assignment statements"""


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.
    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return 0
    return count_digit(n//10, 10-n % 10) + ten_pairs(n//10)


def count_digit(n, digit):
    """Return how many times digit appears in n.
    >>> count_digit(55055, 5)
    4
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return 1 if n == digit else 0
    return (1 if n % 10 == digit else 0) + count_digit(n//10, digit)
# Q5


def make_onion(f, g):
    """
    Write a function make_onion that takes in two one-argument 
    functions, F and G, and returns a function that will take in 
    X, Y, and LIMIT and return True if it is possible to reach Y 
    from X in LIMIT steps or less, via only repeated applications 
    of F and G, and False otherwise.

    >>> add_one = lambda x: x + 1
    >>> mul_by_two = lambda y: y * 2
    >>> can_reach = make_onion(add_one, mul_by_two)
    >>> can_reach(0, 5, 4)      # 5 = add_one(mul_by_two(mul_by_two(add_one(0))))
    True
    >>> can_reach(0, 5, 3)      # Not possible
    False
    >>> can_reach(1, 1, 0)      # 1 = 1
    True
    >>> add_ing = lambda x: x + "ing"
    >>> add_end = lambda y: y + "end"
    >>> can_reach_string = make_onion(add_ing, add_end)
    >>> can_reach_string("cry", "crying", 1)      # "crying" = add_ing("cry")
    True
    >>> can_reach_string("un", "unending", 3)      # "unending" = add_ing(add_end("un"))
    True
    >>> can_reach_string("peach", "folding", 4)      # Not possible
    False
    """
    def can_reach(x, y, limit):
        if x == y:
            return True
        elif limit <= 0:
            return False
        else:
            return can_reach(f(x), y, limit-1) or can_reach(g(x), y, limit-1)
    return can_reach

# Q6


def paths(x, y):
    """Return a list of ways to reach y from x by repeated
    incrementing or doubling.
    >>> paths(3, 5)
    [[3, 4, 5]]
    >>> sorted(paths(3, 6))
    [[3, 4, 5, 6], [3, 6]]
    >>> sorted(paths(3, 9))
    [[3, 4, 5, 6, 7, 8, 9], [3, 4, 8, 9], [3, 6, 7, 8, 9]]
    >>> paths(3, 3) # No calls is a valid path
    [[3]]
    >>> paths(5, 3) # There is no valid path from x to y
    []
    """
    # alternative solution
    if x > y:
        return []
    elif x == y:
        return [[x]]
    else:
        a = paths(x + 1, y)
        b = paths(x * 2, y)
        return [[x] + subpath for subpath in a + b]

    # my solution
    if x > y:
        return []
    elif x == y:
        return [[x]]
    else:
        a = [([x] + elem) for elem in paths(x+1, y)]
        b = [([x] + elem) for elem in paths(x*2, y)]
        return a+b if x*2 <= y else a
        #          ↑ if statement is unnecessary

# Q7


def knapsack(weights, values, c):
    """
    >>> w = [2, 6, 3, 3]
    >>> v = [1, 5, 3, 3]
    >>> knapsack(w, v, 6)
    6
    """
    "*** YOUR CODE HERE ***"
    # solution
    if weights == [] or c <= 0:
        return 0
    else:
        with_first = values[0] + \
            knapsack(weights[1:], values[1:], c-weights[0])
        without_first = knapsack(weights[1:], values[1:], c)
        if weights[0] <= c:
            return max(with_first, without_first)
        return without_first

    # MY WRONG SOLUTION
    if c <= 0:
        return 0

    if weights[0]/values[0] > weights[1]/values[1]:
        return values[0]+knapsack(weights[1:], values[1:], c-weights[0])
    else:
        return values[1]+knapsack(weights[2:], values[2:], c-weights[1])
