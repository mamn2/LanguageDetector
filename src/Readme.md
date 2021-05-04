# Indicate the name of the program

Naïve Bayes Language Classifier

# Give a short description of the problem solved

This program is designed to identify a language based on a given textual input.

# Give a short description on how to run your code

In order to run this, first select which model you want to run. The options are: a letter bigram, a word bigram, and a word bigram that uses Good Turing Smoothing rather than Laplace. You can find these programs in the form of Jupyter Notebooks in src/Code. Each program contains several parts that you need to run: 1) the trainer 2) the classifer. The trainer trains the data that is fed to it which you can edit in the trainClassifier function. The classifier uses the probabilities calculated by the trainer to determine which language it likely belongs to.