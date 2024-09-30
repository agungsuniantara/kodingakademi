# import doctest

def longer(word1,word2):

    if len(word1.lower())>len(word2.lower()):
        return word1
    elif len(word1.lower()) == len(word2.lower()):
        return "same"
    else:
        return word2

result = longer("cat", "dog")
print(result)