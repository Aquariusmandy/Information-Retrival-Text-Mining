import csv
import numpy as np
import pandas as pd

N = 1096 # 0
simmatrix = np.zeros((N,N))

for i in range(N-1):
    
    pathnamea = 'doc'+ str(i+1) + '.txt' 
    indexa = []
    indexb = []
    tfidfa = []
    tfidfb = []
    
    f1= open('output/'+ pathnamea) #讀入檔案
    numa = int(f1.readline())
    empty = f1.readline()
    for k in range(numa):    
        s1 = f1.readline() 
        indexa.append(s1.split()[0]) #doc1的index
        tfidfa.append(s1.split()[1]) #doc1的tfidf
    f1.close
    
    #跟同一群做計算
    for j in range(N-1):
        indexb = []
        tfidfb = []
        a = 0
        b = 0
        cs = 0

        pathnameb = 'doc' + str(j+1) +'.txt'
        f2= open('output/' + pathnameb) #讀入檔案
        numb = int(f2.readline())
        empty = f2.readline()
        for k in range(numb):    
            s2 = f2.readline() 
            indexb.append(s2.split()[0]) #doc2的index
            tfidfb.append(s2.split()[1]) #doc2的tfidf
        f2.close

        #print(indexb)

        for k in range(numa+numb):
            if(a>=numa) or (b>=numb):
                break
            if(indexa[a] == indexb[b]):
                cs = cs + (float(tfidfa[a])*float(tfidfb[b])) #若兩份文件都有相同的term 就相乘
                b = b+1 #window往下一格
            elif(int(indexa[a])<int(indexb[b])):
                a = a+1 #window往下一格
            elif(int(indexa[a])>int(indexb[b])):
                b = b+1 #window往下一格
        
        simmatrix[i+1][j+1] = cs
        print(j)

pd.DataFrame(simmatrix).to_csv('cs_matrix.csv')

