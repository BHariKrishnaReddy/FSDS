1. Explain One-Hot Encoding

   To keep it simple it is like assigning categorical value ot the binary (encoded) vaules. It depends upon the no.of categorical variables.numbers are replaced by 1s and 0s. Depending on which column has what value.
   

2. Explain Bag of Words

   Bag of words is a Natural Language Processing technique of text modelling. In technical terms, we can say that it is a method of feature extraction with text data. This approach is a simple and flexible way of extracting features from documents.  
  
  
3. Explain Bag of N-Grams
   
   Used to convert text data into numerical vectors.It functions by dividing the text into contiguous groups of N words, or "N-grams," and then keeping track of how frequently each N-gram appears in the text.

   Ex: It is what it is .
   If n=1 vector is `{It: 2, is: 2, what: 1}`
   If n=2 vector is `{It is: 2, is what: 1, what it: 1}`

   
4. Explain TF-IDF

   Term Frequency-Inverse Document Frequency (TF)(IDF)
   The basic idea is that a word is important in a document if it appears frequently in that document but rarely in other documents.

   TF = Number of times term "t" in document / Toatl number of terms in document

   IDF = log_e(Total number of documents / Number of documents containing "t").

   
   ```
   from sklearn.feature_extraction.text import TfidfVectorizer
   vec = TfidfVectorizer()
   tfidf_matrix = vectorizer.fit_transform(docs)
   feature_names = vectorizer.get_feature_names()
   print(tfidf_matrix.toarray(),feature_names)
   ```
   
   
5. What is OOV problem?

   Out-Of-Vocabulary problem refers to words or phrases that are not present in a given vocabulary or corpus.It can be challenging for models that rely on pre-defined vocabularies or statistical patterns to predict outcomes.

   
6. What are word embeddings?

   These are used to represent words as numeric vectors in a high-dimensional space.Idea behind word embeddings is to capture the meaning of a word by analyzing its usage in a large corpus of text.

   
7. Explain Continuous bag of words (CBOW)

   Continuous bag of words is a type of word embedding used to represent words as high-dimensional vectors, it works like predicting a target word based on its surrounding context words within a fixed window size

   
8. Explain SkipGram

   The model functions by extracting each word from a vast corpus of literature and turning it into a vector representation, where each member of the vector stands for a distinct aspect of the word, such as its usage, meaning, and context. The SkipGram model then uses these vector representations to learn the probability distribution of the context words given a target word.

   
9. Explain Glove Embeddings.

   Utilizing the co-occurrence statistics of words in a corpus to generate word embeddings is the core concept behind GloVe. A co-occurrence matrix, which counts the number of times each word appears in the context of every other word in the corpus, is constructed specifically by the method. The weighted average of the vector differences between pairs of words is then calculated using this matrix, so words that frequently occur together will have similar embeddings.