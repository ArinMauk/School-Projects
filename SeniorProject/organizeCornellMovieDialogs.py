#clean dataset - get it in the form of just sentences that are groped together.
#create an object.
import re
class cleanDataSet(object):
    def __init__(self, conversationSize_):
        self.conversationSize = conversationSize_;
        self.conversations = [[] for x in xrange(conversationSize_)];
        self.movieNum = re.compile('m[0-9]+');
        self.usersNames = re.compile('u[0-9]+');
        self.conversationData = re.compile('\'(.*?)\'');
    def getConversationSize(self):
        return self.conversationSize;

    def getMovies(self, conversationIndex):
        return self.movieNum.findall(conversationIndex);
   

    def getUsers(self, conversationIndex):
        return self.usersNames.findall(conversationIndex);

    def getConversationData(self, conversationIndex):
        return self.conversationData.findall(conversationIndex);

    def printConversationsMatrix(self):
        print "CONVERSATION STRUCTURE: "
        for i in range(0, self.conversationSize):
            print self.conversations[i];

    #Open and read in N lines; ie: N = conersationSize.
    #use methods: getMovie, getusers, and get ConversationData and store
    #in conversations array.
    def organizeConversationData(self):
        line = '';
        movie = '';
        users = [];
        conversation = [];
        f = open('./cornell_movie_dialogs_corpus/cornell movie-dialogs corpus/movie_conversations.txt', 'r')
        for i in range(0, self.conversationSize):
            line = f.readline();
            movie = self.getMovies(line);
            users = self.getUsers(line);
            conversation = self.getConversationData(line);
            
            self.conversations[i].append(movie);
            self.conversations[i].append(users);
            self.conversations[i].append(conversation);
            #self.conversations[i].append = f.readline();
        f.close();
        
        #print self.conversations[0];
