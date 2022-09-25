"""Runs inference on the model that was build by reconstruct_mind.py."""
import random

from ai_replica.utils.files import read_json, PERSONAL_DATA_DIR
from ai_replica.utils.nlp import get_bag_of_words, similarity_score_of_word_bags


def load_model(load_path):
    """
    >>> res0 = load_model("ai_replica/resources/mock_data/mock_personal_data/reconstructed_mind_models/model.txt")
    >>> len(res0["thoughts"])
    567
    >>> res0["thoughts"][0]["words_bag"]
    ['ancestors', 'anecdotes', 'any', 'ever', 'had', 'have', 'i', 'in', 'little', 'my', 'obtaining', 'of', 'pleasure']
    """
    loaded_model = read_json(load_path)
    return loaded_model


global_model = load_model(f"{PERSONAL_DATA_DIR}/reconstructed_mind_models/model.txt")


def get_model_answer(user_input, seed=None, custom_model=None):
    """
    >>> test_model = load_model("ai_replica/resources/mock_data/mock_personal_data/reconstructed_mind_models/model.txt")
    >>> answer0 = get_model_answer(user_input="love", custom_model=test_model, seed=42)
    >>> "my mother’s love" in answer0
    True
    """
    random.seed(seed)

    input_bag = get_bag_of_words(user_input)

    model = global_model if custom_model is None else custom_model

    highest_score = 0
    closest_thought = model["thoughts"][0]
    for thought in model["thoughts"]:
        thought_bag = thought["words_bag"]
        score = similarity_score_of_word_bags(input_bag, thought_bag)
        if score > highest_score:
            highest_score = score
            closest_thought = thought
        if score == highest_score:
            if random.random() > 0.5:
                highest_score = score
                closest_thought = thought

    # no answer found among the thoughts
    if highest_score == 0:
        return "I have nothing to say. Probably, it makes sense to google."

    return closest_thought["answer"].strip()
