import pickle
with open('dataPickle/morphs.pkl', 'rb') as f:
    morphs = pickle.load(f)

from gensim.models import FastText
import numpy as np

def average_vector(vectors):
    return np.mean(vectors, axis=0)

trainData = []
meanCount = []
for morph in morphs:
  meanCount.append(len(morph))
  for i in range(len(morph)):
    trainData.append(morph[i].split())

model = FastText(trainData, vector_size = 300, window = 5, min_count = 1, sg = 1, workers = 4)
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

for i in range(len(result)):
   if(len(result[i]) > 1):
      for k in range(len(result[i])):
         result[i][k] = average_vector(result[i][k])
   else: result[i] = average_vector(result[i])

with open('embedModel/model.pkl', 'wb') as f:
    pickle.dump(wordVec, f)
with open('embedModel/meanVector.pkl', 'wb') as f:
    pickle.dump(result, f)