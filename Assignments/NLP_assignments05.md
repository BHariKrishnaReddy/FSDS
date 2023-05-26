1. What are Sequence-to-sequence models?
A Seq2Seq model is a model that takes a sequence of items(words, letters, time series, etc) and outputs another sequence of items.

2. What are the Problem with Vanilla RNNs?
Recurrent neural network is a type of network architecture that accepts variable inputs and variable outputs, which contrasts with the vanilla feed-forward neural networks.

3. What is Gradient clipping?
Gradient clipping is a technique to deal with exploding gradients problem is to clip the gradients during backpropagation so that they never exceed some threhsold.

This technique is most often used in recurrent neural network, as Batch Normalization is tricky to use in RNN

The Gradient Clipping is just a matter of setting the clipvalue or clipnorm argument when creating an optimizer.

This optimizer will clip every component of the gradient vector to a value between -1.0 and 1.0.This threshold is a hyperparameter you can tune.

4. Explain Attention mechanism
The idea behind the attention mechanism was to permit the decoder to utilize the most relevant parts of the input sequence in a flexible manner, by a weighted combination of all of the encoded input vectors, with the most relevant vectors being attributed the highest weights.

The attention mechanism was introduced to address the bottleneck problem that arises with the use of a fixed-length encoding vector, where the decoder would have limited access to the information provided by the input.

This is thought to become especially problematic for long and/or complex sequences, where the dimensionality of their representation would be forced to be the same as for shorter or simpler sequences

5. Explain Conditional random fields (CRFs)
Conditional Random Fields are a discriminative model, used for predicting sequences. They use contextual information from previous labels, thus increasing the amount of information the model has to make a good prediction

6. Explain self-attention
Self attention, also called intra Attentionm is an attention mechanism relating different positions of a single sequence in order to compute a representation of the same sequence.

It has been shown to be very useful in machine reading, abstractive summarization, or image description generation

7. What is Bahdanau Attention?
The Bahdanau attention mechanism has inherited its name from the first author of the paper

Bahdanau argue that this encoding of a variable-length input into a fixed-length vector squashes the information of the source sentence, irrespective of its length, causing the performance of a basic encoder-decoder model to deteriorate rapidly with an increasing length of the input sentences.

The approach they propose, on the other hand, replaces the fixed-length vector with a variable-length one, to improve the translation performance of the basic encoder-decoder model.

8. What is a Language Model?
A language model is a probablity distribution over sequence of words. Given such a sequence of length m, a language model assigns a probability to the whole sequence. Language models generate probability by training on text corpora in one or many languages.

9. What is Multi-Head Attention?
The most important layer in the Transformer architecture is the Multi-Head Attention layer. It is at the core of language models such as BERT and GPT-2. Its purpose is to allow the model to identify which words are most aligned with each other, and then improve each word's representation using these contextual clues.

10. What is Bilingual Evaluation Understudy (BLEU)
BLEU (bilingual evaluation understudy) is an algorithm for evaluating the quality of text which has been machine-translated from one natural language to another.

BLEU's output is always a number between 0 and 1. This value indicates how similar the candidate text is to the reference texts, with values closer to 1 representing more similar texts.
