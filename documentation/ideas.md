# Use a better personal data search engine

Currently, bag of words approach is used to search bot's personal data for answers. The approach works to some extent but has certain limitations. E.g. synonims and typos are not taken into account. Potentially, makes sense to try to use pre-trained embeddings, e.g. SpaCy. Though they have the limitation that the context is not taken into account, so in some cases the meaning of the words can be detected incorrectly, e.g. some words can represent different semantics, e.g. bank as financial organization and bank as a part of a river. To mitigate this limitation, potentially, it makes sense to use sentence embeddings. Also, it makes sense to investigate whether there is any pre-trained models tht allow performing QnA on free text data. Probably, there are such models that can be fine-tuned in unspurvised mode with minimal efforts.

## free text QnA engine

Is there any free text QnA engine available?

## sbert sentence embeddings
Introductory article into sentence embeddings: https://www.analyticsvidhya.com/blog/2020/08/top-4-sentence-embedding-techniques-using-python/.

## TF-IDF from sklearn

https://stackoverflow.com/questions/55677314/using-sklearn-how-do-i-calculate-the-tf-idf-cosine-similarity-between-documents/55682395#55682395
 
# Language detection

Try to determine whether a user is speaking in a  non-English language and ask to switch to English. The fllowing classifoer can be used as an example or re-used completely: https://github.com/RasaHQ/rasa-nlu-examples/tree/0.2.8

# Multi-language support

Try Rasa's LanguageModelFeaturizer with rasa/LaBSE model based on language-agnostic BERT: https://rasa.com/docs/rasa/components/#languagemodelfeaturizer
It should provide support for user inputs in multiple languages.
