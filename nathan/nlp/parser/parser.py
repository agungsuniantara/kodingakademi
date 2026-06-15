import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP | S Conj S
NP -> N | Det N | Det AdjP N | NP PP | AdjP N | Det N N | N N
VP -> V | V NP | V PP | V NP PP | V NP NP | Adv VP | VP Adv | VP Conj VP
PP -> P NP
AdjP -> Adj | Adj AdjP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():
    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    # Tokenize the sentence using NLTK's word_tokenize
    words = nltk.word_tokenize(sentence)

    # Convert to lowercase and filter out non-alphabetic tokens
    processed_words = []
    for word in words:
        # Convert to lowercase
        word_lower = word.lower()
        # Check if word contains at least one alphabetic character
        if any(char.isalpha() for char in word_lower):
            processed_words.append(word_lower)

    return processed_words


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    np_chunks = []

    # Iterate through all subtrees in the parse tree
    for subtree in tree.subtrees():
        # Check if the subtree is labeled as NP
        if subtree.label() == "NP":
            # Check if this NP contains any other NPs
            contains_np = False
            for child in subtree.subtrees():
                # Skip the subtree itself
                if child == subtree:
                    continue
                # Check if any child is also an NP
                if child.label() == "NP":
                    contains_np = True
                    break

            # If this NP doesn't contain other NPs, it's a chunk
            if not contains_np:
                np_chunks.append(subtree)

    return np_chunks


if __name__ == "__main__":
    main()
