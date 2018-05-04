# Arin Mauk - Capstone Project: Analyzing Conversational Data
## Describtion:
the purpose of the project is to take in conversational data between 3-5 people and analyze the data after ‘x’ messages and then analyze the data again after ‘y’ messages. The program is then meant to decipher whether or not the conversation has stayed on topic. After researching I found that there were 3 methods that are ideal for implementing topic modeling: LDA, NMF, and word2vec.

## Set up:
you will need the following packages:
 - NLTK
 - stop_words
 - gensim
### Here are the download commands for each package:
(make sure you have pip installed, if not, follow [these download instructions](https://pip.pypa.io/en/stable/installing/): 
```
$ sudo pip install -U nltk
$ sudo pip install stop-words
$ sudo pip install gensim
```

## Running the program
Simply open up a linux/unix terminal and run the following command:
```
python ldaWord2VecNMF.py
```
and the program should run.