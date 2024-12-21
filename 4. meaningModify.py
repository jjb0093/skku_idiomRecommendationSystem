import pickle
with open('dataPickle/meaning.pkl', 'rb') as f:
    meaning = pickle.load(f)

meaningProcess = []
reference = []
for i in range(len(meaning)):
    meaningList = []
    referenceData = None
    for k in range(len(meaning[i])):
        m = meaning[i][k]
        
        stopWords = ["또는", "즉,", "즉 ", "흔히", "줄여서", "따위"]

        # 제거 반복
        for word in stopWords:
            if word in m:
                m = m.replace(word, '')

        if "뜻으로" in m:
            m_split = m.split("뜻으로")
            if '‘' in m_split[0]: meaningList.append(m_split[0][m_split[0].find('‘') + 1 : m_split[0].find('’')])
            elif '.' in m_split[0]: meaningList.append(m_split[0].split('.')[0])
            else: meaningList.append(m_split[0])

            m_split[1] = m_split[1].lstrip(',').strip(' ')
            for l in range(2, len(m_split)):
                m_split[1] += m_split[l]

            mPoint = m_split[1].split('.')
            del mPoint[len(mPoint) - 1]
            #print(mPoint)

            for mp in mPoint:
                mp = mp.strip(' ')
                if(len(mp) == 0): break          
                length = len(mp)
                
                if "에 나오는" in mp: referenceData = mp[: mp.find("에 나오는")]
                elif "에서 나온" in mp: referenceData = mp[: mp.find("에서 나온")]
                elif "유래" in mp: referenceData = mp[: mp.find("유래")]
                elif "논어" in mp: referenceData = "논어"
                elif "비유" in mp: meaningList.append(mp[: mp.find("비유")])
                elif "이르" in mp: meaningList.append(mp[: mp.find("이르")])
                elif "이른" in mp: meaningList.append(mp[: mp.find("이른")])
                elif mp[-1] == '말': meaningList.append(mp[: -2])
                elif mp[length-2:length] == '말임': meaningList.append(mp[: -4])
                elif mp[length-2:length] == '말함': meaningList.append(mp[: -4])
                elif mp[-1] == '뜻': meaningList.append(mp[: -2])
                elif mp[length-2:length] == '뜻함': meaningList.append(mp[: -3])
                else: meaningList.append(mp)

        else: 
            m_split = m.split('.')
            if '‘' in m_split[0]: meaningList.append(m_split[0][m_split[0].find('‘') + 1 : m_split[0].find('’')])
            elif '.' in m_split[0]: meaningList.append(m_split[0].split('.')[0])
            elif "비유" in m_split[0]: meaningList.append(m_split[0][: m_split[0].find("비유")])
            elif "이르" in m_split[0]: meaningList.append(m_split[0][: m_split[0].find("이르")])
            elif "이른" in m_split[0]: meaningList.append(m_split[0][: m_split[0].find("이른")])
            else: meaningList.append(m_split[0])

            del m_split[len(m_split) - 1]
            if(len(m_split) == 2):
                m_split[1] = m_split[1].lstrip(' ')
                if "에 나오는" in m_split[1]: referenceData = m_split[1][0 : m_split[1].find("에 나오는")]
                elif "에서 나온" in m_split[1]: referenceData = m_split[1][0 : m_split[1].find("에서 나온")]
                elif "유래" in m_split[1]: referenceData = m_split[1][0 : m_split[1].find("유래")]
                elif "논어" in m_split[1]: referenceData = "논어"
                elif "비유" in m_split[1]: meaningList.append(m_split[1][0 : m_split[1].find("비유")])
                elif "이르" in m_split[1]: meaningList.append(m_split[1][0 : m_split[1].find("이르")])
                elif "이른" in m_split[1]: meaningList.append(m_split[1][0 : m_split[1].find("이른")])
                else: meaningList.append(m_split[1])
            elif(len(m_split) > 2):
                length = len(m_split) - 1

                m_split[length] = m_split[length].strip(' ')
                if "에 나오는" in m_split[length]: referenceData = m_split[length][0 : m_split[length].find("에 나오는")]
                elif "에서 나온" in m_split[length]: referenceData = m_split[length][0 : m_split[length].find("에서 나온")]
                elif "유래" in m_split[length]: referenceData = m_split[length][0 : m_split[length].find("유래")]
                elif "논어" in m_split[length]: referenceData = "논어"
                elif "비유" in m_split[length]: meaningList.append(m_split[length][0 : m_split[length].find("비유")])
                elif "이르" in m_split[length]: meaningList.append(m_split[length][0 : m_split[length].find("이르")])
                elif "이른" in m_split[length]: meaningList.append(m_split[length][0 : m_split[length].find("이른")])
                elif (m_split[length][0] != '그' and m_split[length][0] != '다' and m_split[length][0] != '’' 
                      and m_split[length][0] != '는' and ' ,' not in m_split[length] and len(m_split[length]) >= 5):
                    meaningList.append(m_split[length])

    meaningProcess.append(meaningList)
    reference.append(referenceData)

with open('dataPickle/meaningProcess.pkl', 'wb') as f:
    pickle.dump(meaningProcess, f)
with open('dataPickle/reference.pkl', 'wb') as f:
    pickle.dump(reference, f)

with open('dataTxt/meanP.txt', encoding='utf-8', mode='w') as f:
    for m in meaningProcess:
        f.write(str(m) + "\n")
with open('dataTxt/reference.txt', encoding='utf-8', mode='w') as f:
    for m in reference:
        f.write(str(m) + "\n")