The following are some of my 'collection' of NLP things that I have used or meant to try out.

## Courses
- [The classic NLP course from Stanford](http://web.stanford.edu/class/cs224n/) (good for those who are up for a challenge, goes deep into the fundamentals)
- [Huggingface NLP](https://huggingface.co/course/chapter1/1) -- good introductory course, also handy for getting familiar with the Huggingface library
- [Fast.ai course](https://course.fast.ai/Lessons/lesson4.html) (it covers NLP, amongst other things. Jeremy Howard is also one of the first people to propose you can finetune language models)

## Blogs
- [illustrated transformer](http://jalammar.github.io/illustrated-transformer/): very clear explanation of one of the most important architectures in modern NLP. (Well, all of [Jay's other posts](http://jalammar.github.io/) are very good as well)
- [The annotated transformer](http://nlp.seas.harvard.edu/annotated-transformer/)-- deep dive into the code behind the transfomer model

## Libraries
- [Spacy](https://spacy.io/)-- Handles a lot of different NLP tasks (tokenization, Lemmatisation, model training etc), good for productionisation (nice thing is that it got both 'traditional' stuff like part of speech tagging etc as well as recent transformer models)
- [Docquery](https://github.com/impira/docquery)-- apparently you can 'query' text documents using natural sentences using this (they based their tool on the [Layout LM model](https://arxiv.org/abs/1912.13318))
- Huggingface: they have built up a family of user friendly libraries that support NLP tasks, and making it easy to use open source pretrained models (e.g. [tokenizers](https://github.com/huggingface/tokenizers), [transformers](https://github.com/huggingface/transformers), [Accelerate](https://github.com/huggingface/accelerate))


## Honarable mentions
- ElasticSearch (it is really, really good at doing text search, but do need a lot of devops know how if you need to maintain it...!)
- [BERTopic example](https://github.com/MaartenGr/BERTopic)
