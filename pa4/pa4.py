import csv
import numpy as np
import pandas as pd

N = 1096 
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

#初始化
N = 1096
A = [] #每次merge的紀錄
I = [1]*N #cluster是不是活的
m = 0
n = 0
#先把similarity的分數抓回matrix
#simmatrix = np.zeros((N,N))
"""
fp = open('cs_matrix.csv','r',encoding='utf-8')
csv_reader = csv.reader(fp)
simmatrix = list(csv_reader)
fp.close
simmatrix.pop(0)
for i in range(N):
    simmatrix[i].pop(0)

for i in range(N):
    for j in range(N):
        simmatrix[i][j]=float(simmatrix[i][j])
"""

#每次掃一輪 matrix 找當下最大值，且略過 i=j
for k in range(N-1): #merge 群數從這邊調
    maxsim = 0.0
    maxpair_i = 0
    maxpair_j = 0
    for i in range(1,N):
        if(I[i] == 0): #死掉的跳過
            continue
        for j in range(1,N): #i=j跳過
            if(i == j):
                continue
            if(I[j]==0):
                continue
            if( simmatrix[i][j] > maxsim ): #找最大的sim
                maxsim = simmatrix[i][j]
                maxpair_i = i
                maxpair_j = j
    A.append([maxpair_i,maxpair_j]) #紀錄這次合併誰
    #print(A)
    # 把Ｊ併進Ｉ然後更新表格

    for m in range(1,N):
        #complete link 偷改一點
        if(simmatrix[maxpair_i][m]==0):
            simmatrix[maxpair_i][m] = simmatrix[maxpair_j][m]
        elif(simmatrix[maxpair_j][m]==0):
            simmatrix[maxpair_i][m] = simmatrix[maxpair_i][m]
        else:
            simmatrix[maxpair_i][m] = min(simmatrix[maxpair_i][m],simmatrix[maxpair_j][m])
        
        if(simmatrix[m][maxpair_i]==0):
            simmatrix[m][maxpair_i] = simmatrix[m][maxpair_j]
        elif(simmatrix[m][maxpair_j]):
            simmatrix[m][maxpair_i] = simmatrix[m][maxpair_i]    
        else:
            simmatrix[m][maxpair_i] = min(simmatrix[m][maxpair_i],simmatrix[m][maxpair_j])

    I[maxpair_j] = 0
    
    #看一下現在幾群
    alive = []
    count = 0
    for i in range(1,N):
        if(I[i] == 1):
            count = count +1
            alive.append(i)
    if(count == 8): #群數在這邊改
        break
    
    print(k)

#用 Queue 輔助輸出答案
Queue = []
a = 0
b = 0

f3 = open('8.txt','a')

for k in alive:
    Queue.append(k)
    while(len(Queue) != 0): #當Queue不為空
        for i in A:
            a = i[0]
            b = i[1]
            if (a == Queue[0]):
                Queue.append(b)
        f3.write(str(Queue[0]))
        f3.write('\n')
        Queue.pop(0) #把寫入的刪掉
    
    f3.write('\n') #換群中間空一行

f3.close

