import datetime
import logging
import os
import re
from sentence_transformers import SentenceTransformer
from ai_replica.utils.files import find_files, write_to_json, PERSONAL_DATA_DIR

logger = logging.getLogger(__name__)
embeddings_file = os.path.abspath(os.path.dirname(__file__) + "/embeddings.json")


def save_embeddings(path, embeddings_data):
    # if not os.path.exists(path):
    print(f"Saving model to: {path}")
    write_to_json(path, embeddings_data)


def build_model(custom_data_path=None):
    model = SentenceTransformer("msmarco-distilbert-base-v4")

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
            content = f.read().replace("\n", "")
            all_text += content + ". "

    sentences = re.split("[\.\!\?]", all_text)

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
    return sentences_data


def reconstruct(custom_save_path=None, custom_data_path=None):
    # save_path = (
    #     f"{PERSONAL_DATA_DIR}/reconstructed_mind_models/model.txt"
    #     if custom_save_path is None
    #     else custom_save_path
    # )

    # model = build_model(custom_data_path=custom_data_path)
    # write_to_json(save_path, data_dict=model)

    if not os.path.exists(embeddings_file):
        model = build_model(custom_data_path=custom_data_path)
        save_embeddings(embeddings_file, model)
    else:
        print(f"The model already exists at: {embeddings_file}")
