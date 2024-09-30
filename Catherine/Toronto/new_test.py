def longer(word1,word2):
    """
    return longest word
    :param word1: str
    :param word2: str
    :return: str

    >>>longer("cat","dog")
    "same"
    >>>longer("fuck","dog")
    "same"
    >>>longer("dog","fuck")
    "fuck"
    """
    if len(word1.lower())>len(word2.lower()):
        return word1
    elif len(word1.lower()) == len(word2.lower()):
        return "same"
    else:
        return word2