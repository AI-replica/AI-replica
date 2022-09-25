import os
import sys

# TODO: find a better way to run custom bot from Rasa's "bot" folder
# Need to append path to the "ai_repilca" folder to be able to make imports from the modules in that folder
ai_replica_dir_path = os.path.abspath(os.path.dirname(__file__) + "/../..")
sys.path.append(ai_replica_dir_path)

import datetime
import logging

import re
import numpy as np
from ai_replica.utils.files import read_json, write_to_json
from sentence_transformers import SentenceTransformer

sample_bio_file = "personal_data/raw_mind_data/sample_bio.txt"
embeddings_file = os.path.abspath(os.path.dirname(__file__) + "/embeddings.json")

logger = logging.getLogger(__name__)
model = SentenceTransformer("bert-base-nli-mean-tokens")


def cosine(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))


def get_embeddings(path):
    if os.path.exists(path):
        return read_json(path)


def save_embeddings(path, embeddings_data):
    if not os.path.exists(path):
        write_to_json(path, embeddings_data)


def build_model(embeddings_file, source_path):
    content = ""
    with open(source_path) as f:
        content = f.read().replace("\n", "")

    sentences = re.split("[\.\!\?]", content)

    print(f"bio file stats: chars: {len(content)}, sentences: {len(sentences)}")

    logger.info(
        f"[{datetime.datetime.now():%Y-%m-%d.%H:%M:%S}] Sentences embeddings calculation started"
    )
    print(
        f"[{datetime.datetime.now():%Y-%m-%d.%H:%M:%S}] Sentences embeddings calculation started"
    )
    sentence_embeddings = model.encode(sentences).tolist()

    print(
        f"[{datetime.datetime.now():%Y-%m-%d.%H:%M:%S}] Sentences embeddings calculated"
    )
    logger.info(f"[{datetime.datetime.now():%Y-%m-%d}] Sentences embeddings calculated")
    sentences_data = list(
        map(
            lambda i: (sentences[i], sentence_embeddings[i]),
            range(len(sentences)),
        )
    )
    save_embeddings(embeddings_file, sentences_data)


def main():
    embeddings_data = get_embeddings(embeddings_file)
    if embeddings_data == None:
        # TODO: process large files (1GB+ in batches
        build_model(embeddings_file, sample_bio_file)
        embeddings_data = get_embeddings(embeddings_file)

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

    query = "What do you think about England?"
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
    sentences_top5 = sentences_info_sorted[0:5]

    for i in range(len(sentences_top5)):
        print(
            "Sentence = ", sentences_top5[i][0], "; similarity = ", sentences_top5[i][1]
        )


if __name__ == "__main__":
    main()
