from pathlib import Path
import os
path = Path('/Users/mandy/documents/01institute/04 class 110/IR/R11725045_PA2/IRTM/')
x = 0
for i in path.iterdir():
    pathname = i.name
    print(pathname)
    if(pathname[0] == '.'):
        continue
    f = open(i, encoding='utf-8',errors='ignore') #讀入檔案
    s = f.read() #將檔案內容放入s
    text = s.split() #以空白字符區分儲存 token 到 text 裏面 
    #print(i) #測試一下text的內容
    x = x+1
    f.close

print(x)