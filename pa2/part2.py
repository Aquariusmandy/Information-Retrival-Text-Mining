from nltk.stem import PorterStemmer
stemmer = PorterStemmer()


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


# 輸入要計算的文件
# 計算 tf-idf

name = input()

f3 = open('data/'+name) #讀入檔案
s3 = f3.read() #將檔案內容放入s3
text3 = s3.split() #以空白字符區分儲存

dict = {} #存 t_index : df
token3 = {} #把指定讀入的
temp4 = 0
temp5 = 0

for i in text3:
    token3[temp4] = stemmer.stem(text3[temp4])
    temp4 = temp4+1

#print(token3)

for i in token3:
    for j in term:
        if(token3[i]==term[j]):
            dict[temp5] = df[temp5]
        temp5 = temp5 +1
    temp5 = 0

print(dict)

