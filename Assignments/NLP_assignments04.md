> 1. Can you think of a few applications for a sequence-to-sequence RNN? What about a sequence-to-vector RNN? And a vector-to-sequence RNN?

  **Applications of seq-to-seq RNN**

  1. Machine translation
  2. video captioning
  3. Speech to text
  4. Music generation

  **Applications of seq-to-vec RNN**
   1. Classify music samples by music genre
   2. Analyzing the sentiment of a book review
   3. Predicting the probability that a user will want to watch a movie based on their watch history

  **Applications of vec-to-seq RNN**
  1. Image captioning
  2. A music playlist based on an embedding of the current artist.
  3. Generating a melody based on a set of parameters
  4. Locating pedestriants in a picture.

> 2. Why do people use encoder–decoder RNNs rather than plain sequence-to-sequence RNNs for automatic translation?

In general, if you translate a sentence one word at a time, the result will be terrible. For example, the French sentence `Je vous en prie` means `You are welcome` but if you translate it one word at a time, you get `I you in pray.`

It is much better to read the whole sentence first and then translate it.A plain sequence-tosequence RNN would start translating a sentence immediately after reading the first word,
While an **_Encoder–Decoder RNN will first read the whole sentence and then translate it_**. That said, one could imagine a plain sequence-to-sequence RNN that would output silence whenever it is unsure about what to say next (just like human translators do when they must translate a live broadcast).

> 3. How could you combine a convolutional neural network with an RNN to classify videos?

A video consists of an ordered sequence of frames. Each _frame contains spatial information_, and the _sequence of those frames contains temporal information_.To model both of these aspects we use a hybrid architecture that consists of convolutions(for spatial processing) as well as recurrent layers(for temporal processing). Speciafically, we'll **use a CNN and RNN** consisting. This kind of hybrid architecture is popularly is popularly known as a CNN-RNN.

> 4. What are the advantages of building an RNN using dynamic_rnn() rather than static_rnn()?

Internally, static_rnn() creates an unrolled graph for a fixed RNN length. That means, if you call tf.nn.rnn with inputs having 200 time steps you are creating a static graph with 200 RNN steps. _First, graph creation is slow. Second, you're unable to pass in longer sequences._ Whereas dynamic_rnn() solves this. It uses a tf.While loop to dynamically construct the graph when it is executed. That means graph creation is faster and you can feed batches of variable size.

> 5. How can you deal with variable-length input sequences? What about variable-length output sequences?

Variable-length input sequences can be handled by padding the shorter sequences so that all sequences in a batch have the same length, and using masking to ensure the RNN ignores the padding token. For better performance, you many also want to create batches containing sequences of similar size.

Regarding variable-length output sequence, if the length of the output-sequene is known in advance, then you just need to configure the loss function so that it ignores tokens that come after the end of the sequence. Similarly, the code that will use the model should ignore tokens beyond the end of the sequence. But generally the length of the output sequence is not known ahead of time, so the solution is to train the model so that it outputs and end-of-sequence token at the end of each sequence.
