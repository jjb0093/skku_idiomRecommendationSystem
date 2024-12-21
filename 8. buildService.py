import subprocess
import numpy as np
from numpy import dot
from numpy.linalg import norm
import streamlit as st
from konlpy.tag import Okt
import pickle

subprocess.run(['apt-get', 'update'])
subprocess.run(['apt-get', 'install', 'g++', 'openjdk-8-jdk', 'python-dev', 'python3-dev'])
subprocess.run(['pip3', 'install', 'JPype1-py3'])
subprocess.run(['pip3', 'install', 'konlpy'])
subprocess.run(['bash', '-c', 'export JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"'])

with open('embedModel/model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('embedModel/meanVector.pkl', 'rb') as f:
    meanVector = pickle.load(f)

with open('dataPickle/hanja.pkl', 'rb') as f:
    hanja = pickle.load(f)
with open('dataPickle/kor.pkl', 'rb') as f:
    kor = pickle.load(f)
with open('dataPickle/meaning.pkl', 'rb') as f:
    meaning = pickle.load(f)
with open('dataPickle/url.pkl', 'rb') as f:
    url = pickle.load(f)

okt = Okt()

stop_words = set([
    '은', '는', '이', '가', '아', '하', '들', '것', '의', '있', '되', '수', '보', '주', '등', '한',
    '에', '으로는', '데', '된', '되어', '를', '될', '됨', '된다', '하며', '만큼', '내', '제', '있음',
    '하면서', '하게', '있어', '거나'
])

def cos_sim(A, B):
    return dot(A, B) / (norm(A) * norm(B))

def average_vector(vectors):
    return np.mean(vectors, axis=0)

def getVector(keyword, model):
    result = []

    pos = okt.pos(keyword)
    for p in pos:
        if ((p[1] == 'Verb') or (p[1] == 'Noun') or (p[1] == 'Adjective')) and (p[0] not in stop_words):
            if p[0][-1] == '을':
                result.append(model[p[0][:-1]])
            elif p[0][0] == '없':
                result.append(model['없'])
            elif p[0][0] == '않':
                result.append(model['않'])
            else:
                result.append(model[p[0]])

    return average_vector(result)

def getDistance(vector, meanVector):
    distance = []
    for i in range(len(meanVector)):
        max = 0
        for m in meanVector[i]:
            d = cos_sim(vector, m)
            if d > max:
                max = d
        distance.append(max)

    return distance

st.title('Idiom Recommendation System')

keyword = st.text_input("검색할 단어 혹은 문장을 입력하세요:", "")

if keyword:
    vector = getVector(keyword, model)

    distance = getDistance(vector, meanVector)

    dis_copy = distance.copy()
    dis_copy.sort()

    top = dis_copy[-5:]
    top_index = []
    for t in top:
        n = distance.index(t)
        top_index.append(n)
        distance[n] = 0

    st.write("Top 5 Results:")
    for i in range(len(top_index)):
        st.write(f"{hanja[top_index[i]]} ({kor[top_index[i]]}): {meaning[top_index[i]]}")
        st.write(f"URL: https://hanja.dict.naver.com/#/entry/ccko/{url[top_index[i]]}")
