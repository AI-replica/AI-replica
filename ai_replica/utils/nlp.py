"""Tools for Natural Language Processing"""

import string


def is_some_keyword_in_text(text, keywords):
    """
    >>> test_text = "What is the current price of Ethereum"
    >>> is_some_keyword_in_text(test_text, keywords=["price", "buy"])
    True
    >>> is_some_keyword_in_text(test_text, keywords=["potato"])
    False
    """
    res = False
    lowered_text = text.lower()
    for keyword in keywords:
        lowered_keyword = keyword.lower()
        if lowered_keyword in lowered_text:
            res = True
            break
    return res


def tokenize(text):
    """
    TODO: aslo remove non-English punctiation, as in “Proposals.”
    >>> txt = "Junto furnished a part; the next was to write a pamphlet! And we wrote the thing."
    >>> tokenize(txt)
    ['junto', 'furnished', 'a', 'part', 'the', 'next', 'was', 'to', 'write', 'a', 'pamphlet', 'and', 'we', 'wrote', 'the', 'thing']
    """
    # common_punctuation = ".,:-“。，！？：×“”〟"
    almost_no_punctuation = text.translate(str.maketrans("", "", string.punctuation))
    lowered = almost_no_punctuation.lower()
    tokens = lowered.split()
    return tokens


def get_bag_of_words(text):
    """
    >>> txt = "Junto furnished a part; the next was to write a pamphlet! And we wrote the thing."
    >>> get_bag_of_words(txt)
    ['a', 'and', 'furnished', 'junto', 'next', 'pamphlet', 'part', 'the', 'thing', 'to', 'was', 'we', 'write', 'wrote']
    """
    tokens = tokenize(text)
    unique_words = set(tokens)
    sorted_list = sorted(list(unique_words))  # to make the results deterministic
    return sorted_list


def similarity_score_of_word_bags(bag1, bag2):
    """A dummy similarity metric. Simply counts the common words in the two bags.

    >>> similarity_score_of_word_bags(["apple", "orange", "duck"], ["orange", "duck"])
    2
    """
    intersect = set(bag1).intersection(set(bag2))
    return len(intersect)
