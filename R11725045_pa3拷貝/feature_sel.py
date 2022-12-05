import numpy as np
import math

C = 0 #總class數
N = 0 #總文章數
T = 0 #dictionary中的字數
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

f2= open('dictionary.txt') #算dictionary中有多少字
empty = f2.readline()
lines2 = f2.readlines()

fi = open('scoreboard.txt','a')
fi.write('class/t_index  ')
    
for line in lines2:
    T = T + 1
    fi.write(str(T))
    fi.write(' ')

fi.write('\n')
f2.close
print(T) 

T = T+1

num_t_d = 0 #每個文章裡面有幾個terms

classnum = 0

f3 = open('training.txt') #讀入檔案
lines3 = f3.readlines()
for line in lines3:    
    
    n11 = np.zeros(T,dtype=float) #是此class且有出現這個term
    n10 = np.zeros(T,dtype=float) #是此class且沒有出現這個term 即 count_c - n11
    n01 = np.zeros(T,dtype=float) #不是此class但有出現這個字
    n00 = np.zeros(T,dtype=float) #不是此class也沒出現這個字 總篇數減前三項

    num_c_temp = [] #每個class有的文章編號暫存
    terms_in_doc = []
    classnum = int(line.split()[0]) #class編號
    num_c_temp = line.split()[1:16] #class中的文章編號放進去
    print(num_c_temp)

    for j in num_c:
        for m in j:
            terms_in_doc = []
            ontopic = 0
            filename ='doc' + str(m) + '.txt'
            f4 = open('output/'+filename,'r')
            num_t_d = int(f4.readline())
            empty = f4.readline()
            for k in range(num_t_d):
                line4 = f4.readline()
                terms_in_doc.append(int(line4.split()[0])) #文章裡面有的字的編號    
            
            for k in num_c_temp:
                #print(k)
                if(m == k): #如果當前的文章屬於當前的class
                    ontopic = 1
                    break
            
            if(ontopic == 1): #如果這篇文章屬於此class
                for l in terms_in_doc:
                    n11[l] = n11[l]+1 #在這篇文章中的字都是n11
                    
            elif(ontopic == 0): #如果這篇文章不屬於此class
                for l in terms_in_doc:
                    n01[l] = n01[l]+1 #在這篇文章中的字都是n01
                    
    #計算每個字之於當前 class 的 likelihood ratios
    print(n11[3786])
    fi.write(str(classnum))
    fi.write('       ')
    
    for j in range(1,T):
        
        n10[j] = count_c - n11[j]
        n00[j] = N - n10[j] - n01[j] - n11[j]
        C1 = (math.factorial(n11[j]+n10[j])//(math.factorial(n11[j])*math.factorial(n10[j])))
        C2 = math.factorial(n01[j]+n00[j])//(math.factorial(n01[j])*math.factorial(n00[j]))
        pt = (n11[j]+n01[j])/N
        p1 = n11[j]/(n11[j]+n10[j])
        p2 = n01[j]/(n01[j]+n00[j])
        LH1 = C1*math.pow(pt,n11[j])*math.pow((1-pt),n10[j])*C2*math.pow(pt,n01[j])*math.pow((1-pt),n00[j])
        LH2 = C1*math.pow(p1,n11[j])*math.pow((1-p1),n10[j])*C2*math.pow(p2,n01[j])*math.pow((1-p2),n00[j])
        score = (-2)*math.log(LH1/LH2)
        #print(score)

        #把分數寫入 scoreboard
        fi.write(str(score))
        fi.write(' ')
    
    fi.write('\n')
f3.close
fi.close

t_index=[]
class_id = []

#score_terms = np.zeros(T,dtype=float)


f5 = open('scoreboard.txt')
t_index.append(f5.readline())
lines4 = f5.readlines()
fj = open('selected2.txt','a')

for line in lines4:  #修改這邊
    class_id.append(line.split()[0])
    temp4 = []
    score_terms ={}
    term_sel1 = {}
    for i in range(T):
        j = i+1
        temp4.append(float(line.split()[j])) #現在此class所有的terms的分數都得到了
    for i in range(T-1):
        j = i+1    
        score_terms[j] =  temp4[i]
    term_sel1 = sorted(score_terms.items(),key=lambda x:x[1],reverse=True)
    for i in range(40):
        j = i+1
        fj.write(str(term_sel1[j]))
        fj.write('\n')
f5.close

#count = 0

#for i in range(T-1):
#    j = i+1
#    if(score_terms[j]>35):
#        term_sel1[j] = score_terms[j]
#        count = count + 1

#print(count)

#print(term_sel1)



fj.close