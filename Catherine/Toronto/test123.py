def longest(a, b):
    """
    >>> longest("aku", "kamu")
    'kamu'
    """
    if len(a) > len(b):
        return a
    else:
        return b
