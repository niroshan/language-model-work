# Building a Simple Language Model with N-Grams

This project builds a simple language model from scratch in python. The goal is to understand how computers can predict the next word in a sentence by learning patterns from text. This project uses a statistical approach based on counting patterns, which is an early example of how early language models worked.

## What is an N-Gram Model?

An n-gram model predicts the next word based on the prior words in the sentence. The value **n** represents the number of words (n-1) used to make a prediction and the word produced. <br>

For example:
> "The car is very fast"

A trigram model (n = 3) looks at the previous 2 words to predict the next word. <br>

For the above example:
> ("The", "car") --> "is" <br>
> ("car", "is") --> "very" <br>
> ("is", "very") --> "fast"<br>

The model counts how often these patterns appear in the training text, and the more often a pattern appears, the more likely it is to choose that word when generating text.

## How the model works

### 1. Tokenising the text <br>

Firstly, the text is split into tokens (words and punctuation). <br>
Example:
> "The cat is lazy." <br>
becomes: <br>
> ("The", "cat", "is", "lazy", "\<END\>")

### 2. Learning word patterns <br>

The program scans through the text and sees what words follow other words. <br>
Example (trigram):
> token ('the', 'car'): {'is': 2} <br>
> token ('car', 'is'): {'very': 1, 'coloured': 1} <br>

In this example 'is' follows 'the car' twice, while after 'car is', 'very' and 'coloured' are both called once. <br>

### 3. Generating New Sentences <br>

To generate text:

1. Start with a seed phrase that is of length n-1.
2. Look up what words commonly follow.
3. Choose the next word using wighted probability.
4. Repeat until sentence ends or maximum words generated.

## Running the Program

To run the program:
> python ngram_cli.py

Here is an example of the program working:

```bash
=== N-Gram Text Generator ===
1) Train model
2) Generate sentence
3) Show model info
4) Quit
Choose an option: 1
Choose n (2, 3, 4...): 3
Reading: data/alice-in-wonderland.txt
Tokenising...
Tokens: 31692
Building model...
States: 14917
Training complete.

=== N-Gram Text Generator ===
1) Train model
2) Generate sentence
3) Show model info
4) Quit
Choose an option: 3

--- Model info ---
n: 3
Tokens loaded: 31692
States: 14917
Example state: ('having', 'found')
Top next tokens:
  out -> 1

=== N-Gram Text Generator ===
1) Train model
2) Generate sentence
3) Show model info
4) Quit
Choose an option: 2
Enter seed word(s): having found
Max words (Enter for default 25): 25

Generated:
having found out a history of the evening beautiful soup <END>

=== N-Gram Text Generator ===
1) Train model
2) Generate sentence
3) Show model info
4) Quit
Choose an option: 2
Enter seed word(s): alice was
Max words (Enter for default 25): 25

Generated:
alice was rather glad there was no one else seemed inclined to say anything <END>

=== N-Gram Text Generator ===
1) Train model
2) Generate sentence
3) Show model info
4) Quit
Choose an option: 4
Goodbye.
```