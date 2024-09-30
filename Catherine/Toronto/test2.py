def amount_of_pizzas(adult, child, teen):

    """
    >>> amount_of_pizzas(2,1,1)
    1.0
    """

    result = (adult * 2 + teen * 3 + child * 1) / 8
    return result