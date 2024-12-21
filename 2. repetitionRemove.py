import pickle
with open('dataPickle/hanja.pkl', 'rb') as f:
    hanja = pickle.load(f)
with open('dataPickle/kor.pkl', 'rb') as f:
    kor = pickle.load(f)
with open('dataPickle/meaning.pkl', 'rb') as f:
    meaning = pickle.load(f)
with open('dataPickle/url.pkl', 'rb') as f:
    url = pickle.load(f)

was = []
repeat = []
for i in range(len(kor)):
    if kor[i] not in was: was.append(kor[i])
    else: repeat.append(i)

for i in range(len(repeat)-1, -1, -1):
    del hanja[repeat[i]]
    del kor[repeat[i]]
    del meaning[repeat[i]]
    del url[repeat[i]]

with open('dataPickle/hanja.pkl', 'wb') as f:
    pickle.dump(hanja, f)
with open('dataPickle/kor.pkl', 'wb') as f:
    pickle.dump(kor, f)
with open('dataPickle/meaning.pkl', 'wb') as f:
    pickle.dump(meaning, f)
with open('dataPickle/url.pkl', 'wb') as f:
    pickle.dump(url, f)