    1. What are Corpora?

    A corpora is a collection of documents or paragraphs

    2. What are Tokens?

    Given a character sequence and a defined document unit, tokenization is the task of chopping into pieces called tokens

    Input: My name is krishna

    Ouput:{My, name, is, krishna}

    3. What are Unigrams, Bigrams, Trigrams?

    Example: "One of the best place to learn Data Science is iNeuron.ai"

    Unigram: It is a one-word sequence.

    Example: "One", "of", "the", "best", "place", "to", "learn", "Data", "Science", "is", "iNeuron.ai"
    Bigram: It is a two-word sequence of words

    Example: "One of", "the best", "place to", "learn Data", "Science is", "iNeuron.ai"
    Trigram:It is a three-word sequence of words

    Example: "One of the", "best place to", "learn Data Science", "is iNeuron.ai"

    4. How to generate n-grams from text?

    N-grams are continuous sequence of words or symbol or tokens in a document. In technical terms, they can be defined as the neighbouring sequence of items in a document.

    'n' is the possible number of words we can take.

    n=1 is unigram

    n=2 is bigram

    n=3 is trigram

    n...so

    5. Explain Lemmatization

    Lemmatization is used reduce some complex words into a simple meaningful words.It identifies the root based meaning of the word
    It is a dictionary-based approach,Lemmatization always gives the dictionary meaning word while converting into root-form.
    `Eg: 'troubled' -> 'troubled'  'studies' -> 'study'`

    6. Explain Stemming

    The process of reducing towards their root forms are called Stemming.The word has one root-base form but having different variations.

    It is a rule-based approach.
    When we convert any word into root-form then stemming may create the non-existence meaning of a word.
    Stemming is preferred when the meaning of the word is not important for analysis.
    Eg: 'Studies' -> 'Studi'

    7. Explain Part-of-speech (POS) tagging

    Parts-of-speech(POS) tagging may be defined as the process of convertinga sentence in the form of a list of words, into a list of tuples. Here, the tuples are in the form of(word, tag). We can also call POS tagging a process of assigning one of the parts of speech to the given word.

    In simple words, we can say that POS tagging is task of labelling each word in a sentence with its appropriate part of speech. We already know the parts of speech include nouns, verb, adverbs, adjectives, pronouns, conjuction and their sub-categories

    8. Explain Chunking or shallow parsing

    Chunking is somewhere between part of speech(POS) tagging and full language paring, hence the name shallow parsing. POS tagging is very fast but often doesn't provide a ton of utility for information extraction.
    It's helpful to know the POS tags, but when we try to derive information about our text we're still swimming within the unstructured soup of words in a sentence.

    9. Explain Noun Phrase (NP) chunking

    Text chunking is dividing sentences into non-overlapping phrases. Noun phrase chunking deals with extracting the noun phrases from a sentence. While NP chunking is much simpler than parsing, it is still a challenging task to build a accurate and very efficient NP chunker.The importance of NP chunking derives from the fact that it is used in many applications.

    10. Explain Named Entity Recognition
    
    Named entity recognition (NER) — sometimes referred to as entity chunking, extraction, or identification — is the task of identifying and categorizing key information (entities) in text. An entity can be any word or series of words that consistently refers to the same thing. Every detected entity is classified into a predetermined category.

    Eg: "I love eating apple" "I love using apple"

    Here 'apple' in the first sentence refers to fruit. But, in the next sentence 'apple' referse to a company

