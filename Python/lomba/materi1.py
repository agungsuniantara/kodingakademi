import doctest

def square(x: int) -> int:
    """
    Returns the square of x.
    
    >>> square(2)
    4
    >>> square(-3)
    9
    """
    return x ** 2

doctest.testmod(verbose=True)