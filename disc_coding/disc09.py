class Pair:
    """Represents the built-in pair data structure in Scheme."""

    def __init__(self, first, rest):
        self.first = first
        if not scheme_valid_cdrp(rest):
            raise SchemeError(
                "cdr can only be a pair, nil, or a promise but was {}".format(rest))
        self.rest = rest

    def map(self, fn):
        """Maps fn to every element in a list, returning a new
        Pair.

        >>> Pair(1, Pair(2, Pair(3, nil))).map(lambda x: x * x)
        Pair(1, Pair(4, Pair(9, nil)))
        """
        assert isinstance(self.rest, Pair) or self.rest is nil, \
            "rest element in pair must be another pair or nil"
        return Pair(fn(self.first), self.rest.map(fn))

    def __repr__(self):
        return 'Pair({}, {})'.format(self.first, self.rest)


class nil:
    """Represents the special empty pair nil in Scheme."""

    def map(self, fn):
        return nil

    def __getitem__(self, i):
        raise IndexError('Index out of range')

    def __repr__(self):
        return 'nil'


nil = nil()  # this hides the nil class *forever*


bindings = {}


def calc_eval(exp):
    if isinstance(exp, Pair):
        # and expressions[paste your answer from the earlier]
        if exp.first == 'and':
            return eval_and(exp.rest)
        elif exp.first == 'define':  # define expressions
            return eval_define(exp.rest)

        else:                   # Call expressions
            return calc_apply(calc_eval(exp.first), exp.rest.map(calc_eval))
    elif exp in bindings:  # Looking up variables
        "*** YOUR CODE HERE ***"
        return bindings[exp]
    elif exp in OPERATORS:      # Looking up procedures
        return OPERATORS[exp]
    else:                       # Numbers
        return exp


# Q6: New Procedure
def floor_div(expr: Pair):
    """
    >>> calc_eval(Pair("//", Pair(10, Pair(10, nil))))
    1
    >>> calc_eval(Pair("//", Pair(20, Pair(2, Pair(5, nil)))))
    2
    >>> calc_eval(Pair("//", Pair(6, Pair(2, nil))))
    3
    """
    "*** YOUR CODE HERE ***"
    # alternative solution
    dividend = expr.first
    expr = expr.rest
    while expr != nil:
        divisor = expr.first
        dividend //= divisor
        expr = expr.rest
    return dividend

    # My recursion solution
    def helper(expr, sofar):
        if isinstance(expr.rest, Pair):
            return helper(expr.rest, sofar // expr.rest.first)
        return sofar
    return helper(expr, expr.first)


# Q7: New Form
def eval_and(operands):
    """
    >>> calc_eval(Pair("and", Pair(1, nil)))
    1
    >>> calc_eval(Pair("and", Pair(False, Pair("1", nil))))
    False
    """
    "*** YOUR CODE HERE ***"
    # alternative solution
    curr, val = operands, True
    while curr is not nil:
        val = calc_eval(curr.first)
        if val is False:
            return False
        curr = curr.rest
    return val

    # My solution with some mistakes
    left, right = operands.first, operands.rest
    while right != nil:
        if left is False:
            return False
        left = right.first
        right = right.rest
    return left


# Q8: Saving Values
def eval_define(expr):
    """
    >>> calc_eval(Pair("define", Pair("a", Pair(1, nil))))
    'a'
    >>> calc_eval("a")
    1
    """
    "*** YOUR CODE HERE ***"
    name, val = expr.first, calc_eval(expr.rest.first)
    bindings[name] = val
    return name


OPERATORS = {"//": floor_div}
