import os

path = os.getcwd()
files = os.listdir(path)
# print(files) ['rename.py', '뉴런활성화함수.m4a', '뉴런활성화함수_memo.txt',
num = 0
for file in files:
    if '_memo' in file:
        num+=1
        print(num,file)
        pre_file = f'{path}/{file}'
        re_file = pre_file.replace('_memo','')
        # print(pre_file,re_file)
        os.rename(pre_file,re_file)
