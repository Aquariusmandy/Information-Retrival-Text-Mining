import numpy as np
import math
import pandas as pd
from pathlib import Path
import csv

C = 0 #總class數
N = 0 #總文章數
T = 3787 #dictionary中的字數
count_c = 0 #每個class中的文章數 
classnow = 0
empty = []
num_c = []


f1= open('training.txt') #讀入檔案
lines1 = f1.readlines()
for line in lines1:    
    
    num_c_temp = [] #每個class有的文章編號暫存
    classnow = int(line.split()[0]) #class編號先丟掉
    num_c_temp = line.split()[1:16] #class中的文章編號放進去
    num_c.append(num_c_temp)
    count_c = 0

    for j in num_c_temp:
        count_c = count_c + 1
        N = N + 1
    C = C + 1

prior = [0]*(C+1)

for line in lines1:    
    
    classnow = int(line.split()[0]) #class編號先丟掉
    empty = line.split()[1:16] #class中的文章編號放進去
    num_c_temp = line.split()[1:16] #class中的文章編號放進去
    count_c = 0

    for j in num_c_temp:
        count_c = count_c + 1
    prior[classnow] = (count_c)/N

f1.close

print(N,C,count_c)
#print(prior)

features = [] #500個選完的字

f6 = open('selected.txt')
lines6 = f6.readlines()
for line in lines6:
    features.append(line.split(',')[0])

features_token = [] #暫存字元用
times_ct = {} #在此class中此term出現次數
condprob = {}
f6.close

y = 0
for i in features: 
    features_token = []    
    x = 0
    
    for j in i: #j是單字中每個字元
        features_token.append(j) #把字串拆成字元
        x = x+1
    features_token[0]=''
    features[y]= ''.join(features_token)
    z = int(features[y])
    times_ct[z] = 0
    condprob[z] = [0]*13
    y = y+1
        
#print(features)
condprob2 = pd.DataFrame(condprob)
classnow = 0
num_c_better = []

for j in num_c: #class
    
    totalterms = 0 #class中的總terms數
    for m in j: #document
        terms_in_doc = []
        ontopic = 0
        filename ='doc' + str(m) + '.txt'
        f4 = open('output/'+filename,'r')
        num_t_d = int(f4.readline())
        empty = f4.readline()
        for k in range(num_t_d):
            line4 = f4.readline()
            terms_in_doc.append(int(line4.split()[0])) #文章裡面有的字的編號 
        
        for k in terms_in_doc: #terms
            
            is_terms = 0 #當下的字有沒有在500字裡面
            
            for l in features:
                if (k==int(l)):
                    is_terms = 1
            
            if(is_terms==1): #如果這篇文章的這個字有在字典裡，那就記錄
                times_ct[k] = times_ct[k] + 1 #這個字在這個class中出現的次數加一
                totalterms = totalterms + 1 #此class總字數加一
        f4.close
        num_c_better.append(m)

    #print(totalterms) 
    z = 0
    for m in features:
        k = int(m)
        condprob2.iat[classnow,z] = ((times_ct[k]+1)/(totalterms+500))
        z =z + 1
    classnow = classnow +1
condprob2.to_csv('testcond.csv')

#開始testing

M = 0 #總data文件數(扣掉training)
is_trainingdata = 0
#先把分類結果存到dictionary再寫入csv
result = {}
with open('classification.csv', 'w',newline = '') as f8:
    writer = csv.writer(f8)
    writer.writerow(['Id','Value'])
    for i in Path('output/').iterdir():
        terms_in_doc = []
        is_trainingdata = 0
        pathname = i.name
        pathname2 = []
        x = 0
        if(pathname[0] == '.'):
            continue
        for j in pathname: #處理一下檔案名稱
            if(x>2):
                if(j == '.'):
                    break
                pathname2.append(j)
            x =x+1
        pathname = ''.join(pathname2)
        for j in num_c_better:
            if(pathname == str(j)): #忽略training data
                is_trainingdata = 1
                continue
        if (is_trainingdata == 0):
            score = [0]*C
            M = M+1 
            print(pathname) #看有沒有成功打開
            f7 = open(i, encoding='utf-8',errors='ignore') #讀入檔案
            num_t_d = int(f7.readline())
            empty = f7.readline()
            for k in range(num_t_d):
                line7 = f7.readline()
                terms_in_doc.append(int(line7.split()[0])) #文章裡面有的字的編號 
            
            for k in range(C): #開始計算此篇文章每個class的分數
                score[k] = score[k] + math.log(prior[k+1]) #先加上prior的分數
                for m in terms_in_doc: #terms
                    is_terms = 0 #當下的字有沒有在500字裡面
                    z = 0
                    for l in features:
                        if (m==int(l)):
                            is_terms = 1
                            break
                        z = z +1
                    if(is_terms==1): #如果有在字典裡就查表然後加起來
                        score[k] = score[k] + math.log(condprob2.iat[k,z])
            #print(score)
            final = np.argmax(score)+1
            writer.writerow([pathname,final])
            f7.close


#with open('classification.csv', 'w',newline = '') as f8:
    #writer = csv.writer(f8)
    #writer.writerow(['Id','value'])
    #writer.writerow([pathname,final])
f8.close
    

                
                       

        
