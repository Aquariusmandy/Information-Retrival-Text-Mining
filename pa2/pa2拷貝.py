from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
from pathlib import Path
import os
import math

f2 = open('stopwords.txt') #讀入檔案
s2 = f2.read() #將檔案內容放入s2
stopwords = s2.split() #以空白字符區分儲存

N = 0 #總data文件數

for i in Path('data/').iterdir():
    pathname = i.name
    if(pathname[0] == '.'):
        continue
    f = open(i, encoding='utf-8',errors='ignore') #讀入檔案
    s = f.read() #將檔案內容放入s
    text = s.split() #以空白字符區分儲存 token 到 text 裏面 
    #print(text) #測試一下text的內容
    N = N+1
    
    list_token = []
    term = {}
    term_fin = {}
    token = {}

    x = 0
    y = 0
    z = 0
    t = 1
    t2 = 1
    n = 0
    m = 0
    temp = 0
    temp2 = 0
    temp3 = 0

    for i in text: #i是文章中每個單字
        for j in i: #j是單字中每個字元
            list_token.append(j) #把字串拆成字元
            x = x+1 #計算此單字字元數
            #print(list_token)

        for k in range(x): #處理符號與大小寫
            if list_token[k] == ',':
                list_token[k] = ''
            elif list_token[k] == '\'':
                list_token[k] = ''
            elif list_token[k] == '\"':
                list_token[k] = ''
            elif list_token[k] == '\\':
                list_token[k] = ''
            elif list_token[k] == '/':
                list_token[k] = ''
            elif list_token[k] == '$':
                list_token[k] = ''
            elif list_token[k] == '`':
                list_token[k] = ''
            elif list_token[k] == '(':
                list_token[k] = ''
            elif list_token[k] == ')':
                list_token[k] = ''
            elif list_token[k] == '.':
                list_token[k] = ''
            elif list_token[k] == '-':
                list_token[k] = ''
            elif list_token[k] == '?':
                list_token[k] = ''    
            elif list_token[k] == '0':
                list_token[k] = ''    
            elif list_token[k] == '1':
                list_token[k] = ''
            elif list_token[k] == '2':
                list_token[k] = ''
            elif list_token[k] == '3':
                list_token[k] = ''
            elif list_token[k] == '4':
                list_token[k] = ''
            elif list_token[k] == '5':
                list_token[k] = ''
            elif list_token[k] == '6':
                list_token[k] = ''
            elif list_token[k] == '7':
                list_token[k] = ''
            elif list_token[k] == '8':
                list_token[k] = ''
            elif list_token[k] == '9':
                list_token[k] = ''
            elif list_token[k] == 'A':
                list_token[k] = 'a'
            elif list_token[k] == 'B':
                list_token[k] = 'b'
            elif list_token[k] == 'C':
                list_token[k] = 'c'
            elif list_token[k] == 'D':
                list_token[k] = 'd'
            elif list_token[k] == 'E':
                list_token[k] = 'e'
            elif list_token[k] == 'F':
                list_token[k] = 'f'
            elif list_token[k] == 'G':
                list_token[k] = 'g'
            elif list_token[k] == 'H':
                list_token[k] = 'h'
            elif list_token[k] == 'I':
                list_token[k] = 'i'
            elif list_token[k] == 'J':
                list_token[k] = 'j'
            elif list_token[k] == 'K':
                list_token[k] = 'k'
            elif list_token[k] == 'L':
                list_token[k] = 'l'
            elif list_token[k] == 'M':
                list_token[k] = 'm'
            elif list_token[k] == 'N':
                list_token[k] = 'n'
            elif list_token[k] == 'O':
                list_token[k] = 'o'
            elif list_token[k] == 'P':
                list_token[k] = 'p'
            elif list_token[k] == 'Q':
                list_token[k] = 'q'
            elif list_token[k] == 'R':
                list_token[k] = 'r'
            elif list_token[k] == 'S':
                list_token[k] = 's'
            elif list_token[k] == 'T':
                list_token[k] = 't'
            elif list_token[k] == 'U':
                list_token[k] = 'u'
            elif list_token[k] == 'V':
                list_token[k] = 'v'
            elif list_token[k] == 'W':
                list_token[k] = 'w'
            elif list_token[k] == 'X':
                list_token[k] = 'x'
            elif list_token[k] == 'Y':
                list_token[k] = 'y'
            elif list_token[k] == 'Z':
                list_token[k] = 'z'    

        token[y] = ''.join(list_token)

        #移除stopwords若為stopword則y不加一，下一輪覆蓋掉
        for l in stopwords:
            if token[y] == stopwords[temp]:
                t = 0 #控制此回合單字是否是stopword
                break
            else:
                temp = temp +1
        temp = 0

        if token[y] == '':
            t = 0 #不是stopword但為空也忽略
        elif len(token[y]) == 1:
            t = 0 #只剩一個字母也不要了

        if t == 1: #不是stopword就往下
            y = y+1
        else: #是stopword就覆蓋此單字並重置t
            t = 1
        x = 0
        list_token = []

    #print(token)

    #做stemming
    for i in token:
        term[temp2] = stemmer.stem(token[temp2])
        temp2 = temp2+1

    #print(term)

    #去掉重複的字

    for i in term: #z存目前檢查到第幾個原本的term
        for j in range(n): #n紀錄term_fin已經存幾個了
            if term[z] == term_fin[temp3]:
                t2 = 0
                break
            temp3 = temp3+1
        temp3 = 0
        
        if t2 == 1:
            term_fin[n] = term[z]
            n = n+1
            z = z+1
        else:
            t2 = 1

    #print(term_fin)

    fi = open('result.txt','a')
    for i in term_fin:
        fi.write(term_fin[m])
        fi.write('\n')
        m = m+1

    fi.close
f.close

#print(result)

# term normolization 結束
# term dictionary 建立開始
f = open('result.txt') #讀入檔案
s = f.read() #將檔案內容放入s2
text = s.split() #以空白字符區分儲存

text.sort()
dictionary = {}
term = {}
df = {}

count = 0
dftemp = 1

for i in text:
    if(count == 0):
        term[count] = i
        count = count+1
    elif(i == term[count-1]):
        dftemp = dftemp + 1
    else:
        term[count] = i
        df[count-1] = dftemp
        count = count + 1
        dftemp = 1
df[count-1] = dftemp
#print(term)
#print(df)

m = 1
fj = open('dictionary.txt','a')
fj.write('(%-7s)' % 't_index')
fj.write('(%-15s)' % 'term')
fj.write('(%-3s)' % 'df')
fj.write('\n')
for i in term:
    fj.write('(%-7s)' % m)
    fj.write('(%-15s)' % term[m-1])
    fj.write('(%-3s)' % df[m-1])
    fj.write('\n')
    m = m+1

fj.close

# 計算 tf-idf

for i in Path('data/').iterdir():
    pathname = i.name
    if(pathname[0] == '.'):
        continue
    f3 = open(i, encoding='utf-8',errors='ignore') #讀入檔案
    s3 = f3.read() #將檔案內容放入s
    text3 = s3.split() #以空白字符區分儲存 token 到 text 裏面 

    dict_term = {}
    temp_term = []
    token3 = {} #把指定讀入的
    temp4 = 0
    temp5 = 0
    count2 = 0 #計算此文件有幾個term
    tftemp = 1
    tf = []

    for k in text3:
        token3[temp4] = stemmer.stem(text3[temp4])
        temp4 = temp4+1

    #print(token3)
    #挑出文件i中有的term
    for j in token3:
        for k in term:
            if(token3[j]==term[k]):
                temp_term.append(term[temp5])
            temp5 = temp5 +1
        temp5 = 0

    temp_term.sort()

    #計算各個term 的tf
    for j in temp_term:
        if(count2 == 0):
            dict_term[count2] = j
            count2 = count2+1
        elif(j == dict_term[count2-1]):
            tftemp = tftemp + 1
        else:
            dict_term[count2] = j
            tf.append(tftemp)
            count2 = count2 + 1
            tftemp = 1
    tf.append(tftemp)

    x = 0
    for j in tf:
        tf[x] = j/(count2) #normalize tf
    filename = 'doc' + pathname
    fk = open('output/' + filename,'a')
    fk.write('%d' % count2)
    fk.write('\n')
    fk.write('t_index  ')
    fk.write('tf-idf')
    fk.write('\n')
    
    
    idf = []
    tfidf = []
    index = []
    length = 0
    y = 0
    z = 0
    #查出各個term的df 算 idf
    for j in dict_term:
        for k in term:
            if(dict_term[j]==term[k]):
                idf.append(math.log10(N/df[y]))
                tfidf.append(tf[j]*idf[j])
                length = length + (float(tfidf[j])**2)
                index.append(y)
                z = z+1
            y = y+1
        y = 0
    
    length = float(length)**(0.5)

    for l in range(z):
        fk.write(str(index[l]))
        fk.write('     ')
        fk.write(str(round((tfidf[l]/length),3)))
        fk.write('\n')
    
    fk.close

# 計算doc1 & doc2 的 cosine similarity

indexa = []
indexb = []
tfidfa = []
tfidfb = []
a = 0
b = 0
cs = 0

f4= open('output/doc1.txt') #讀入檔案
numa = int(f4.readline())
empty = f4.readline()
for i in range(numa):    
    s4 = f4.readline() 
    indexa.append(s4.split()[0]) #doc1的index
    tfidfa.append(s4.split()[1]) #doc1的tfidf
f4.close

f5= open('output/doc2.txt') #讀入檔案
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
