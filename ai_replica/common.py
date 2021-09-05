import ai_replica.skills as skills
from ai_replica.skills import *  # noqa

"""Here, we put together the logic from the engine and the skills.

The end result is served by the get_answer() func.
"""

skill_modules = dict()
for name in skills.__all__:
    module = locals()[name]
    skill_modules[name] = module


def get_skills():
    skills_relevance_funcs = dict()
    skills_result_funcs = dict()
    for name, module in skill_modules.items():
        skills_relevance_funcs[name] = getattr(module, "is_skill_relevant")
        skills_result_funcs[name] = getattr(module, "get_skill_result")
    return skills_relevance_funcs, skills_result_funcs


skill_funcs = get_skills()


def select_skill(user_input, skill_funcs):
    skills_relevance_funcs, skills_result_funcs = skill_funcs
    res = None
    for skill_name, func in skills_relevance_funcs.items():
        relevant7 = skills_relevance_funcs[skill_name](user_input)
        if relevant7:
            res = skill_name
            break
    return res


def ask_skill(user_input, skill_name, skill_funcs):
    skills_relevance_funcs, skills_result_funcs = skill_funcs
    if skill_name in skills_result_funcs:
        res = skills_result_funcs[skill_name](user_input)
    else:
        res = None
    return res


def get_answer(user_input):
    """
    >>> get_answer("what is the current price of bitcoin?")
    'The price of 1 Bitcoin is exactly 1 Bitcoin. No more, no less.'
    >>> get_answer("How is Potato in Russian?")
    "Dude, ask Google or something. I'm not a translator!"
    >>> get_answer("Do you like anime?")
    "You wrote: 'Do you like anime?'. Currently, I'm too stupid to give you a better answer"
    """
    skill_name = select_skill(user_input, skill_funcs)
    res = ask_skill(user_input, skill_name, skill_funcs)
    if res is None:
        res = f"You wrote: '{user_input}'. Currently, I'm too stupid to give you a better answer"
    return res

