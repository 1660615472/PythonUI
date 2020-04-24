
#可用于参数化,web自动化参数化。
#读取文件内容
file = open("C:\\Users\\HP\Desktop\\CSV.txt","r")
data=[]
for x in file:
    #split() 拆分函数，以每行中的空格拆分
    data = x.split()

print(data)
#可用于参数化

