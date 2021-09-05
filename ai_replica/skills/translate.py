from ai_replica.utils.nlp import is_some_keyword_in_text

"""A skill that allows the replica to translate texts."""


def is_skill_relevant(user_input):
    """
    >>> is_skill_relevant("Can you translate Колобок from Russian?")
    True
    >>> is_skill_relevant("Will it rain today?")
    False
    """
    keywords = ["translate", "Russian"]
    relevant7 = is_some_keyword_in_text(user_input, keywords)
    return relevant7


def get_skill_result(user_input):
    """
    >>> res = get_skill_result("How do you say potato in Russian?")
    >>> "Dude" in res
    True
    """
    return "Dude, ask Google or something. I'm not a translator!"
