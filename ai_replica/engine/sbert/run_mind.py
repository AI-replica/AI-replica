import logging
import os
import random
import numpy as np
from sentence_transformers import SentenceTransformer

from ai_replica.utils.files import PERSONAL_DATA_DIR, read_json

logger = logging.getLogger(__name__)
embeddings_file = os.path.abspath(os.path.dirname(__file__) + "/embeddings.json")


def cosine(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))


def load_model(load_path):
    loaded_model = read_json(load_path)
    return loaded_model


global_model = load_model(embeddings_file)


def get_model_answer(user_input, seed=None, custom_model=None):
    random.seed(seed)

    # TODO: think about naming as in bag_of_words engine model is what here called 'embeddings_data'
    embeddings_data = global_model if custom_model is None else custom_model
    print(embeddings_data[0][0], len(embeddings_data))
    model = SentenceTransformer("bert-base-nli-mean-tokens")

    sentences = list(
        map(
            lambda i: (embeddings_data[i][0]),
            range(len(embeddings_data)),
        )
    )
    sentence_embeddings = list(
        map(
            lambda i: (embeddings_data[i][1]),
            range(len(embeddings_data)),
        )
    )

    query = user_input
    query_vec = model.encode([query])[0]

    def get_similarity(sentence_embedding):
        return cosine(query_vec, sentence_embedding)

    similarities = list(map(get_similarity, sentence_embeddings))

    def get_similarity_sort_key(val):
        return val[1]

    sentences_info = list(
        map(
            lambda i: (sentences[i], similarities[i], sentence_embeddings[i]),
            range(len(sentences)),
        )
    )
    sentences_info_sorted = sorted(
        sentences_info, key=get_similarity_sort_key, reverse=True
    )
    # sentences_top5 = sentences_info_sorted[0:5]
    best_match = sentences_info_sorted[0]
    if best_match == None:
        return "I have nothing to say. Probably, it makes sense to google."

    best_match_sentence = best_match[0]
    print(best_match)

    return best_match_sentence
