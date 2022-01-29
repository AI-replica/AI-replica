"""builds the mind's model from the raw mind data.

For this iteration, we use a simple bag-of-words model.
The model consists of chunks of texts, accompanies by the corresponding bags of words.
"""
from ai_replica.utils.files import find_files, write_to_json, PERSONAL_DATA_DIR
from ai_replica.utils.nlp import get_bag_of_words

min_answer_len = 50
max_answer_len = 2000


def build_model(custom_data_path=None):
    """
    >>> test_model = build_model(custom_data_path="ai_replica/resources/mock_data/mock_personal_data/raw_mind_data/")
    >>> thoughts = test_model["thoughts"]
    >>> len(thoughts)
    567
    >>> thoughts[100]["answer"]
    'I liked it much better than that of my father, but still had a hankering for the sea'
    """
    if isinstance(custom_data_path, str):
        data_path = custom_data_path
    else:
        data_path = f"{PERSONAL_DATA_DIR}/raw_mind_data/"

    raw_data_files = find_files(
        path=data_path,
        file_type=".txt",
        exclude=["README.md"],
        only_filenames7=False,
    )

    all_text = ""
    for path in raw_data_files:
        with open(path) as f:
            lines = f.readlines()
        for line in lines:
            all_text += line + " "

    text_by_sentence = all_text.split(".")

    model = {"thoughts": []}
    for line in text_by_sentence:
        stripped = line.strip()
        if len(stripped) > min_answer_len:
            answer = stripped[:max_answer_len]
            words_bag = get_bag_of_words(stripped)
            thought = {"words_bag": words_bag, "answer": answer}
            model["thoughts"].append(thought)

    return model


def reconstruct(custom_save_path=None, custom_data_path=None):
    """
    >>> import os
    >>> test_save_path = "ai_replica/resources/mock_data/mock_models/test_model.txt"
    >>> test_data_path = "ai_replica/resources/mock_data/mock_personal_data/raw_mind_data/"
    >>> if os.path.exists(test_save_path):
    ...     os.remove(test_save_path)
    >>> reconstruct(custom_save_path=test_save_path, custom_data_path=test_data_path)
    >>> os.path.exists(test_save_path)
    True
    """

    save_path = (
        f"{PERSONAL_DATA_DIR}/reconstructed_mind_models/model.txt"
        if custom_save_path is None
        else custom_save_path
    )

    model = build_model(custom_data_path=custom_data_path)
    write_to_json(save_path, data_dict=model)
