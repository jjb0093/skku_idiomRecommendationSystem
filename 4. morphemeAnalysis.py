import pickle
from konlpy.tag import Okt

okt = Okt()
stop_words = set([
                   '은', '는', '이', '가', '아', '하', '들', '것', '의', '있', '되', '수', '보', '주', '등', '한',
                   '에', '으로는', '데', '된', '되어', '를' ,'될', '됨', '된다', '하며', '만큼', '내', '제', '있음', 
                   '하면서', '하게', '있어', '거나'
                ])

with open('meaningProcess.pkl', 'rb') as f:
    meanProcess = pickle.load(f)

morphs = []
for i in range(len(meanProcess)):
    print(i)
    finalPos = []
    for k in range(len(meanProcess[i])):
        data = meanProcess[i][k]
        pos = okt.pos(data)

        truePos = []
        for p in pos:
            if(((p[1] == 'Verb') or (p[1] == 'Noun') or (p[1] == 'Adjective')) and (p[0] not in stop_words)):
                if(p[0][-1] == '을'): truePos.append(p[0][:-1])
                elif(p[0][0] == '없'): truePos.append('없')
                elif(p[0][0] == '않'): truePos.append('않')
                else: truePos.append(p[0])
        if(len(truePos) != 0): finalPos.append(' '.join(truePos))
    if(len(finalPos) != 0): morphs.append(finalPos)


with open('morphs.pkl', 'wb') as f:
    pickle.dump(morphs, f)

with open('dataTxt/morphs.txt', encoding='utf-8', mode='w') as f:
    for m in morphs:
        f.write(str(m) + "\n")