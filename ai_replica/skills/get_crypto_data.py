from ai_replica.utils.nlp import is_some_keyword_in_text

"""A skill that allows the replica to get the current cryptocurrencies data."""
""" 
    The skill is available as Rasa action. See action_price_of_thing. 
    TODO: remove this skill? 
"""


def is_skill_relevant(user_input):
    """
    >>> is_skill_relevant("What is the current bitcoin price?")
    True
    >>> is_skill_relevant("Will it rain today?")
    False
    """
    keywords = ["Bitcoin", "Ethereum", "Doge"]
    relevant7 = is_some_keyword_in_text(user_input, keywords)
    return relevant7


def get_skill_result(user_input):
    """
    >>> get_skill_result("price of Bitcoin?")
    'The price of 1 Bitcoin is exactly 1 Bitcoin. No more, no less.'
    >>> get_skill_result("Which shitcoins would you recommend?")
    'May I interest you in buying some bitcoins instead?'
    """
    if "bitcoin" in user_input.lower():
        res = "The price of 1 Bitcoin is exactly 1 Bitcoin. No more, no less."
    else:
        res = "May I interest you in buying some bitcoins instead?"
    return res
