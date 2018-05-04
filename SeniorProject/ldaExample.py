from organizeCornellMovieDialogs import *
from gensim import corpora, models
from nltk.tokenize import RegexpTokenizer
import gensim
from nltk.stem.porter import PorterStemmer
from stop_words import get_stop_words

def lda(cornellData_, iterations_):
    for iteration in range(0, iterations_):
        # Create stop words list: get a collection of words like: for, or, the, etc.
        # Create stemmer object that puts words to their root meaning.
        # Store the conversation lines in an array.
        conversationData = cornellData_.getConversation(iteration);
        stopWords = get_stop_words('en')
        stemWords = PorterStemmer()
        texts = []
        separateIntoWords = RegexpTokenizer(r'\w+')

        # loop through parts of conversation.
        for i in conversationData:
            raw = i.lower()
            separatedWords = separateIntoWords.tokenize(raw)
            stoppedWords = [i for i in separatedWords if not i in stopWords]
            stemmedWords = [stemWords.stem(i) for i in stoppedWords]
            texts.append(stemmedWords)

        dictionary = corpora.Dictionary(texts)
        corpus = [dictionary.doc2bow(text) for text in texts]

        # generate LDA model
        ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word = dictionary, passes=500)
        print(ldamodel.print_topics(num_topics=1, num_words=2))
    
def main():
    amtConversations = int(raw_input("How many conversations do you want to test?"));
    cornellData = cleanDataSet(amtConversations);
    cornellData.organizeConversationData();
    cornellData.fillInConversationData();

    print "Here is the data we are working with:"
    cornellData.printConversationsMatrix();
    
    lda(cornellData, amtConversations);
main();
