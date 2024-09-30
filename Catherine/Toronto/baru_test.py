import doctest

def longer(word1:str,word2:str)->str:

    """
    return longest word
    >>> longer("cat","dog")
    'same'
    >>> longer("fuck","dog")
    'fuck'
    >>> longer("dog","fuck")
    'fuck'
    """

    if len(word1.lower())>len(word2.lower()):
        return word1
    elif len(word1.lower()) == len(word2.lower()):
        return "same"
    else:
        return word2