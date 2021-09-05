"""Tools for Natural Language Processing"""


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
