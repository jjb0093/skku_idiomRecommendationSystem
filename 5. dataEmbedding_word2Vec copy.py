import pickle
with open('dataPickle/morphs.pkl', 'rb') as f:
    morphs = pickle.load(f)

from gensim.models import Word2Vec

trainData = []
meanCount = []
for morph in morphs:
  meanCount.append(len(morph))
  for i in range(len(morph)):
    trainData.append(morph[i].split())

model = Word2Vec(trainData, vector_size = 500, window = 8, min_count = 1, sg = 1, epochs = 10)
wordVec = model.wv

result = []
count = 0
for i in range(len(meanCount)):
  embeded_row = []
  for j in range(meanCount[i]):
    embeded_column = []
    for w in trainData[count]:
      embeded_column.append(wordVec[w])
    count += 1
    embeded_row.append(embeded_column)
  result.append(embeded_row)

with open('embedModel/model.pkl', 'wb') as f:
    pickle.dump(morphs, f)
with open('embedModel/meanVector.pkl', 'wb') as f:
    pickle.dump(result, f)