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
        self.findLineId = re.compile('L[0-9]*');
        self.findLineTextGarbage = re.compile('.*\+\+\+\$\+\+\+\s');
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
        for i in range(0, len(self.conversations)):
            print "======================================================================="
            print "Conversation " + str(i);
            for j in range(len(self.conversations[i])):
                if j == 0:
                    print "Movie Number: " + str(self.conversations[i][j]);
                elif j == 1:
                    print "User IDs: " + str(self.conversations[i][j]);
                elif j == 2:
                    print "Conversation Data: "
                    for k in range(len(self.conversations[i][j])):
                        print "LINE" + str(k) + ": " + self.conversations[i][j][k];

    def findLineText(self, lineID):
        textFound = False;
        lineText = "";
        f = open('./cornell_movie_dialogs_corpus/cornell movie-dialogs corpus/movie_lines.txt', 'r');
        while textFound == False:
            line = f.readline();
            currentLineNum = self.findLineId.findall(line);
            if currentLineNum[0] == lineID:
                textFound = True;
                lineTextGarbage = self.findLineTextGarbage.findall(line);
                lineText = line.replace(lineTextGarbage[0], "");
                lineText = lineText.replace('\n', "");
        
        f.close();
        return lineText;

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
            
        f.close();
        

    def fillInConversationData(self):

        #for each individual conversation
        for i in range(len(self.conversations)):

            #for each conversation lineID
            for j in range(len(self.conversations[i][2])):
                #print self.conversations[i][2][j];
                self.conversations[i][2][j] = self.findLineText(self.conversations[i][2][j]);

    
