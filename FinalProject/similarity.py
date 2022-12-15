import csv

index_now = 0
movie_id = []

with open('mplot_final.csv',newline='') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        catch = []  #存當下的摘要
        index_now = int(row[0])
        movie_id.append(row[1]) #movie_id對上index
        catch.append(row[2])

querylist = []
f1 = open('query_list.txt')
s1 = f1.read()
querylist = s1.splitlines()
#print(querylist)

for i in querylist:
    
    i = i.strip('\n')
    is_this_clu = 0 #紀錄狀態
    samecluster = [] #放跟query同一個cluster的
    clusternumber = 1 #紀錄當下是第幾個cluster
    
    #把同一群的抓出來

    f2 = open('5.txt')
    lines = f2.readlines()
    for line in lines:
        samecluster.append(line)
        if(i == line):
            is_this_clu = 1
        elif(i == ''):
            if(is_this_clu == 1):
                break
            samecluster = []
            cluster = cluster + 1    
    f2.close

    #print(samecluster)

    #計算此電影之於其他電影的cosine similarity
    #然後寫入文件
    
    indexa = []
    indexb = []
    tfidfa = []
    tfidfb = []
    a = 0
    b = 0
    cs = 0

    #最後的結果
    pathnamea = i + '.txt'
    fi = open('similarity/' + pathnamea,'a')
    fi.write(str(i))
    fi.write('\n')
    fi.write('%-15s' % 'movie_id')
    fi.write('%-20s' % 'cosine_similarity')
    fi.write('\n')
    
    #本次query的電影
    f4= open('output/'+ pathnamea) #讀入檔案
    numa = int(f4.readline())
    empty = f4.readline()
    for i in range(numa):    
        s4 = f4.readline() 
        indexa.append(s4.split()[0]) #doc1的index
        tfidfa.append(s4.split()[1]) #doc1的tfidf
    f4.close
    
    #跟同一群做計算
    for j in samecluster:
        indexb = []
        tfidfb = []
        j = j.strip('\n')
        if(j == ''):
            break
        pathnameb = j +'.txt'
        f5= open('output/' + pathnameb) #讀入檔案
        numb = int(f5.readline())
        empty = f5.readline()
        for k in range(numb):    
            s5 = f5.readline() 
            indexb.append(s5.split()[0]) #doc2的index
            tfidfb.append(s5.split()[1]) #doc2的tfidf
        f5.close

        print(indexb)

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
        
        fi.write('%-15s' % j)
        fi.write('%-20f' % cs)
        fi.write('\n')
    fi.close

