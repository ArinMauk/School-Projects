#testing cleanDataset object functionality.
from organizeCornellMovieDialogs import *

x = cleanDataSet(10);
print "Hello";
print x.getConversationSize();
print x.organizeConversationData();
#print x.getMovies('u0 +++$+++ u2 +++$+++ m9564 +++$+++ [\'L194\', \'L195\', \'L196\', \'L197\']')
#print x.getUsers('u0 +++$+++ u2 +++$+++ m9564 +++$+++ [\'L194\', \'L195\', \'L196\', \'L197\']')
#print x.getConversationData('u0 +++$+++ u2 +++$+++ m9564 +++$+++ [\'L194\', \'L195\', \'L196\', \'L197\']')
#print x.printConversationsMatrix();
x.fillInConversationData();
x.printConversationsMatrix();
