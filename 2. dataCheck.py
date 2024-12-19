import pickle
with open('dataPickle/hanja.pkl', 'rb') as f:
    hanja = pickle.load(f)
with open('dataPickle/kor.pkl', 'rb') as f:
    kor = pickle.load(f)
with open('dataPickle/meaning.pkl', 'rb') as f:
    meaning = pickle.load(f)
with open('dataPickle/url.pkl', 'rb') as f:
    url = pickle.load(f)
with open('dataPickle/reference.pkl', 'rb') as f:
    refernce = pickle.load(f)
with open('dataPickle/meaningProcess.pkl', 'rb') as f:
    meaningProcess = pickle.load(f)

print(len(hanja), len(kor), len(meaning), len(url), len(meaningProcess))

#with open('dataTxt/meanP.txt', encoding='utf-8', mode='w') as f:
#    for m in meaningProcess:
#        f.write(str(m) + "\n")

with open('dataTxt/hanja.txt', encoding='utf-8', mode='w') as f:
    for m in hanja:
        f.write(str(m) + "\n")

#with open('dataTxt/reference.txt', encoding='utf-8', mode='w') as f:
#    for m in refernce:
#        f.write(str(m) + "\n")