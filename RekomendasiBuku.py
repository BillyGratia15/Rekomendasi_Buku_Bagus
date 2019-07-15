import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv('books.csv')
data2 = pd.read_csv('ratings.csv')

def gabung(i):
    return str(i['authors'])+' '+str(i['original_title'])+' '+str(i['title'])+' '+str(i['language_code'])
data1['Features'] = data1.apply(gabung,axis='columns')

# Count Vectorizer
from sklearn.feature_extraction.text import CountVectorizer
model = CountVectorizer(tokenizer=lambda x:x.split(' '))
matrixFeature = model.fit_transform(data1['Features'])
features = model.get_feature_names()
jumlahFeatures = len(features)

# Cosine similarity
from sklearn.metrics.pairwise import cosine_similarity
score = cosine_similarity(matrixFeature)

Andi1 = data1[data1['original_title']=='The Hunger Games']['book_id'].tolist()[0]-1 
Andi2 = data1[data1['original_title']=='Catching Fire']['book_id'].tolist()[0]-1 
Andi3 = data1[data1['original_title']=='Mockingjay']['book_id'].tolist()[0]-1 
Andi4 = data1[data1['original_title']=='The Hobbit or There and Back Again']['book_id'].tolist()[0]-1 
fav1 = [Andi1,Andi2,Andi3,Andi4]

Budi1 = data1[data1['original_title']=='Harry Potter and the Philosopher\'s Stone']['book_id'].tolist()[0]-1 
Budi2 = data1[data1['original_title']=='Harry Potter and the Chamber of Secrets']['book_id'].tolist()[0]-1 
Budi3 = data1[data1['original_title']=='Harry Potter and the Prisoner of Azkaban']['book_id'].tolist()[0]-1 
fav2 = [Budi1,Budi2,Budi3]

Ciko1 = data1[data1['original_title']=='Robots and Empire']['book_id'].tolist()[0]-1 
fav3 = [Ciko1]

Dedi1 = data1[data1['original_title']=='Nine Parts of Desire: The Hidden World of Islamic Women']['book_id'].tolist()[0]-1 
Dedi2 = data1[data1['original_title']=='A History of God: The 4,000-Year Quest of Judaism, Christianity, and Islam']['book_id'].tolist()[0]-1 
Dedi3 = data1[data1['original_title']=='No god but God: The Origins, Evolution, and Future of Islam']['book_id'].tolist()[0]-1 
fav4 = [Dedi1,Dedi2,Dedi3]

Ello1 = data1[data1['original_title']=='Doctor Sleep']['book_id'].tolist()[0]-1 
Ello2 = data1[data1['original_title']=='The Story of Doctor Dolittle']['book_id'].tolist()[0]-1 
Ello3 = data1[data1['title']=='Bridget Jones\'s Diary (Bridget Jones, #1)']['book_id'].tolist()[0]-1 
fav5 = [Ello1,Ello2,Ello3]

listscoreA1 = list(enumerate(score[Andi1]))
listscoreA2 = list(enumerate(score[Andi2]))
listscoreA3 = list(enumerate(score[Andi3]))
listscoreA4 = list(enumerate(score[Andi4]))

listscoreB1 = list(enumerate(score[Budi1]))
listscoreB2 = list(enumerate(score[Budi2]))
listscoreB3 = list(enumerate(score[Budi3]))

listscoreCiko = list(enumerate(score[Ciko1]))

listscoreD1 = list(enumerate(score[Dedi1]))
listscoreD2 = list(enumerate(score[Dedi2]))
listscoreD3 = list(enumerate(score[Dedi3]))

listscoreE1 = list(enumerate(score[Ello1]))
listscoreE2 = list(enumerate(score[Ello2]))
listscoreE3 = list(enumerate(score[Ello3]))

listscoreAndi = []
for i in listscoreA1:
    listscoreAndi.append((i[0],0.25*(listscoreA1[i[0]][1]+listscoreA2[i[0]][1]+listscoreA3[i[0]][1]+listscoreA4[i[0]][1])))
listscoreBudi = []
for i in listscoreA1:
    listscoreBudi.append((i[0],(listscoreB1[i[0]][1]+listscoreB2[i[0]][1]+listscoreB3[i[0]][1])/3))
listscoreDedi = []
for i in listscoreA1:
    listscoreDedi.append((i[0],(listscoreD1[i[0]][1]+listscoreD2[i[0]][1]+listscoreD3[i[0]][1])/3))
listscoreEllo = []
for i in listscoreA1:
    listscoreEllo.append((i[0],(listscoreE1[i[0]][1]+listscoreE2[i[0]][1]+listscoreE3[i[0]][1])/3))
# print(listscoreAndi[0][1])

listscoresortedAndi = sorted(listscoreAndi,key=lambda j:j[1],reverse=True)
listscoresortedBudi=sorted(listscoreBudi,key=lambda j:j[1],reverse=True)
listscoresortedCiko=sorted(listscoreCiko,key=lambda j:j[1],reverse=True)
listscoresortedDedi = sorted(listscoreDedi,key=lambda j:j[1],reverse=True)
listscoresortedEllo = sorted(listscoreEllo,key=lambda j:j[1],reverse=True)
# print(listscoresorted)
# print(listscoresorted[:5])
# print(listscoresorted[:5][0])

# Reccomend top 5
samaAndi = []
for i in listscoresortedAndi:
    if i[1]>0:
        samaAndi.append(i)
samaBudi = []
for i in listscoresortedBudi:
    if i[1]>0:
        samaBudi.append(i)
samaCiko = []
for i in listscoresortedCiko:
    if i[1]>0:
        samaCiko.append(i)
samaDedi = []
for i in listscoresortedDedi:
    if i[1]>0:
        samaDedi.append(i)
samaEllo = []
for i in listscoresortedEllo:
    if i[1]>0:
        samaEllo.append(i)

print('1. Buku bagus untuk Andi:')
for i in range(0,5):
    if samaAndi[i][0] not in fav1:
        print('-',data1['original_title'].iloc[samaAndi[i][0]])
    else:
        i += 5
        print('-',data1['original_title'].iloc[samaAndi[i][0]])

print(' ')
print('2. Buku bagus untuk Budi:')
for i in range(0,5):
    if samaBudi[i][0] not in fav2:
        print('-',data1['original_title'].iloc[samaBudi[i][0]])
    else:
        i += 5
        print('-',data1['original_title'].iloc[samaBudi[i][0]])

print(' ')
print('3. Buku bagus untuk Ciko:')
for i in range(0,5):
    if samaCiko[i][0] not in fav3:
        print('-',data1['original_title'].iloc[samaCiko[i][0]])
    else:
        i += 5
        print('-',data1['original_title'].iloc[samaCiko[i][0]])

print(' ')
print('4. Buku bagus untuk Dedi:')
for i in range(0,5):
    if samaDedi[i][0] not in fav4:
        print('-',data1['original_title'].iloc[samaDedi[i][0]])
    else:
        i += 5
        print('-',data1['original_title'].iloc[samaDedi[i][0]])

print(' ')
print('5. Buku bagus untuk Ello:')
for i in range(0,5):
    if samaEllo[i][0] not in fav5:
        if str(data1['original_title'].iloc[samaEllo[i][0]])=='nan':
            print('-',data1['title'].iloc[samaEllo[i][0]])
        else:
            print('-',data1['original_title'].iloc[samaEllo[i][0]])  
    else:
        i += 5
        if str(data1['original_title'].iloc[samaEllo[i][0]])=='nan':
            print('-',data1['title'].iloc[samaEllo[i][0]])
        else:
            print('-',data1['original_title'].iloc[samaEllo[i][0]])  