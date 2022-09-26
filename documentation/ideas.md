# Use a better personal data search engine

Currently, bag of words approach is used to search bot's personal data for answers. The approach works to some extent but has certain limitations. E.g. synonims and typos are not taken into account. Potentially, makes sense to try to use pre-trained embeddings, e.g. SpaCy. Though they have the limitation that the context is not taken into account, so in some cases the meaning of the words can be detected incorrectly, e.g. some words can represent different semantics, e.g. bank as financial organization and bank as a part of a river. To mitigate this limitation, potentially, it makes sense to use sentence embeddings. Also, it makes sense to investigate whether there is any pre-trained models tht allow performing QnA on free text data. Probably, there are such models that can be fine-tuned in unspurvised mode with minimal efforts.

## free text QnA engine

Is there any free text QnA engine available?

## sbert sentence embeddings
Introductory article into sentence embeddings: https://www.analyticsvidhya.com/blog/2020/08/top-4-sentence-embedding-techniques-using-python/.

### BERT

https://arxiv.org/pdf/1810.04805.pdf

## msmarco models for asymmetric semantic search
https://www.sbert.netdocs/pretrained-models/msmarco-v3.html

https://medium.com/mlearning-ai/semantic-search-with-s-bert-is-all-you-need-951bc710e160

## GPT-3 fine-tuning

## BLOOM fine-tuning
BLOOM - An open-source large language model

https://huggingface.co/bigscience/bloom
https://github.com/bigscience-workshop/Megatron-DeepSpeed


## GRP-NeoX fine-tuning

https://github.com/EleutherAI/gpt-neox/

Open-source Large Languange Model.

>  Additionally, we hope to train and open source a 175B parameter GPT-3 replication along the way. 

## LaMBDA fine-tuning
https://ai.googleblog.com/2022/01/lamda-towards-safe-grounded-and-high.html

LaMDA is a family of Transformer-based neural language models specialized for dialog, which have up to 137B parameters and are pre-trained on 1.56T words of public dialog data and web text.

LaMDA: Language Models for Dialog Applications: https://arxiv.org/abs/2201.08239

https://github.com/conceptofmind/LaMDA-pytorch

## Long-Form Question Ansering

https://arxiv.org/pdf/2103.06332.pdf

The task of long-form question answering (LFQA) involves retrieving documents relevant to a given question and using them to generate a paragraph-length answer

## TF-IDF from sklearn

https://stackoverflow.com/questions/55677314/using-sklearn-how-do-i-calculate-the-tf-idf-cosine-similarity-between-documents/55682395#55682395
 
# Language detection

Try to determine whether a user is speaking in a  non-English language and ask to switch to English. The fllowing classifoer can be used as an example or re-used completely: https://github.com/RasaHQ/rasa-nlu-examples/tree/0.2.8

# Multi-language support

Try Rasa's LanguageModelFeaturizer with rasa/LaBSE model based on language-agnostic BERT: https://rasa.com/docs/rasa/components/#languagemodelfeaturizer
It should provide support for user inputs in multiple languages.
