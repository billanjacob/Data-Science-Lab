import nltk
from nltk import ngrams

text = "Steve has a cat called Tom. A mouse is always after a piece of cheese. Tom ate the mouse."

sentence = nltk.sent_tokenize(text)

for i in sentence:
    words = nltk.word_tokenize(i)
    tags = nltk.pos_tag(words)
    print("Tag: ",tags)
    N = ngrams(sequence=words, n=3)
    print("ngram: ")
    for i in N:
        print(i)

