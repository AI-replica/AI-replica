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

Semantic Search with S-BERT is all you need: https://medium.com/mlearning-ai/semantic-search-with-s-bert-is-all-you-need-951bc710e160

Models tuned for cosine-similarity will prefer the retrieval of shorter passages, while models for dot-product will prefer the retrieval of longer passages. Depending on your task, you might prefer the one or the other type of model. (https://www.sbert.net/docs/pretrained-models/msmarco-v3.html)

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
 
## Large Dialog/Chatbot Models

It makes sense to take some pretty big dialog model and fine-tune it in a custom text. Ideally, it should be a model that is able to extract knowledge from text, so that the fine-tuning data can be unsupervised. I.e. the data/knowledge provided in a free text should be incorporate dinto the model's knowledge and subsequently used in a dialog. Also this model should be able provide response of variable length, i.e. a one-one sentence, a multi-word sentence, a paragraph - whatever represents the best answer or a turn in a dialog.

### List
- [LaMBDA by Google](#lambda-by-google)
- [Sparrow by DeepMind](#sparrow-by-deepmind)
- [BlenderBot by Meta](#blenderbot-by-meta)
- ...

### BlenderBot by Meta
https://ai.facebook.com/blog/state-of-the-art-open-source-chatbot/

Open source open-domain chatbot.

Facebook AI has built and open-sourced BlenderBot, the largest-ever open-domain chatbot. It outperforms others in terms of engagement and also feels more human, according to human evaluators.

Chatbot recipe: Scale, blending skills, and generation strategies.

Common to other natural language processing research today, the first step in creating our chatbot was large-scale training. 
Further analysis via human evaluation underscored the importance of both blending skills and choosing a generation strategy that produces nonrepetitive, detailed responses.

Our latest model’s performance is nearly equal to human-level quality in this specific test setup.

Recipes for building an open-domain chatbot: https://arxiv.org/abs/2004.13637
Recipes for building an open-domain chatbot: https://parl.ai/projects/recipes/

We build variants of these recipes with 90M, 2.7B and 9.4B parameter neural models, and make our models and code publicly available.

### BlenderBot 2.0 by Meta

https://ai.facebook.com/blog/blender-bot-2-an-open-source-chatbot-that-builds-long-term-memory-and-searches-the-internet/
https://parl.ai/projects/blenderbot2/

Facebook AI Research has built and open-sourced BlenderBot 2.0, the first chatbot that can simultaneously build long-term memory it can continually access, search the internet for timely information, and have sophisticated conversations on nearly any topic.

The knowledge is stored separately for each person it speaks with, which ensures that no new information learned in one conversation is used in another.

That’s because it’s the first chatbot capable of generating internet search queries, using and building knowledge over time and referring back to previous ideas. During conversations, BlenderBot 2.0 can query the internet using any search engine for relevant new knowledge and can both read and write to its long-term local memory store. 

Finally, we look forward to a day soon when agents built to communicate and understand as humans do can see as well as talk, which we’ve explored with 
Multimodal BlenderBot
. That’s why some obvious next steps are to continue to try to blend these latest techniques together into a single AI system, which is the 
goal of our BlenderBot research
. We think that these improvements in chatbots can advance the state of the art in applications such as virtual assistants and digital friends. We hope this release and the corresponding data sets will help the community collectively make further progress in these and many other directions.

Minimal model size: BST+MSC+WizInt w/Switch3	400M	2.78	8.33	5.00	10.56 (as per https://parl.ai/projects/blenderbot2/)

Multi-Modal Open-Domain Dialogue: https://parl.ai/projects/multimodal_blenderbot/?fbclid=IwAR3T5sZo6-iO660CvgS_rCOZT6yyDT3Lh0E77EwzFadpN-imgdItEtuylpM

### BlenderBot 3 by Meta

https://ai.facebook.com/blog/blenderbot-3-a-175b-parameter-publicly-available-chatbot-that-improves-its-skills-and-safety-over-time/

BlenderBot 3: A 175B parameter, publicly available chatbot that improves its skills and safety over time

### Meena by Google
https://arxiv.org/abs/2001.09977

### LaMBDA by Google

### Sparrow by DeepMind


# Language detection

Try to determine whether a user is speaking in a  non-English language and ask to switch to English. The fllowing classifoer can be used as an example or re-used completely: https://github.com/RasaHQ/rasa-nlu-examples/tree/0.2.8

# Multi-language support

Try Rasa's LanguageModelFeaturizer with rasa/LaBSE model based on language-agnostic BERT: https://rasa.com/docs/rasa/components/#languagemodelfeaturizer
It should provide support for user inputs in multiple languages.
