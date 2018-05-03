from gensim.models import Word2Vec
# define training data
sentences = [['Brocolli', 'is', 'good', 'to', 'eat', 'My', 'brother', 'likes', 'to', 'eat', 'good', 'brocolli', 'but', 'not', 'my', 'mother'],
			['My', 'mother', 'spends', 'a', 'lot', 'of', 'time', 'driving', 'my', 'brother', 'around', 'to', 'baseball', 'practice'],
			['Some', 'health', 'experts', 'suggest', 'that', 'driving', 'may', 'cause', 'increased', 'tension', 'and', 'blood', 'pressure'],
			['I', 'often', 'feel', 'pressure', 'to', 'perform', 'well', 'at', 'school', 'but', 'my', 'mother', 'never', 'seems', 'to', 'drive', 'my', 'brother', 'to', 'do', 'better'],
			['Health', 'professionals', 'say', 'that', 'brocolli', 'is', 'good', 'for', 'your', 'health']]
# train model
model = Word2Vec(sentences, min_count=1)
# summarize the loaded model
print(model)
# summarize vocabulary
words = list(model.wv.vocab)
print(words)
# access vector for one word
print(model['brother'])
# save model
model.save('model.bin')
# load model
new_model = Word2Vec.load('model.bin')
print(new_model)
