indexa = []
indexb = []
tfidfa = []
tfidfb = []
a = 0
b = 0
cs = 0

f4= open('output/tt0105695.txt') #讀入檔案
numa = int(f4.readline())
empty = f4.readline()
for i in range(numa):    
    s4 = f4.readline() 
    indexa.append(s4.split()[0]) #doc1的index
    tfidfa.append(s4.split()[1]) #doc1的tfidf
f4.close

f5= open('output/tt1204975.txt') #讀入檔案
numb = int(f5.readline())
empty = f5.readline()
for i in range(numb):    
    s5 = f5.readline() 
    indexb.append(s5.split()[0]) #doc2的index
    tfidfb.append(s5.split()[1]) #doc2的tfidf
f5.close

for j in range(numa+numb):
    if(a>=numa) or (b>=numb):
        break
    if(indexa[a] == indexb[b]):
        cs = cs + (float(tfidfa[a])*float(tfidfb[b])) #若兩份文件都有相同的term 就相乘
        b = b+1 #window往下一格
    elif(int(indexa[a])<int(indexb[b])):
        a = a+1 #window往下一格
    elif(int(indexa[a])>int(indexb[b])):
        b = b+1 #window往下一格

print('cosine similarity:' + str(cs))