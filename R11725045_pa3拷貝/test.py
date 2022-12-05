import numpy as np
import pandas as pd

features = [] #500個選完的字

f6 = open('selected.txt')
lines6 = f6.readlines()
for line in lines6:
    features.append(line.split(',')[0])

features_token = [] #暫存字元用
times_ct = {} #在此class中此term出現次數
condprob = {}

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
    condprob[z] = [0]*14
    y = y+1
        
#print(condprob)

condprob2 = pd.DataFrame(condprob)
print(condprob2)