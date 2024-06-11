dic={}
are = [1,2,2,3,3,4,4,4,5]

for i in are:
    if i in dic:
        dic[i]=dic[i]+1
    else:
        dic[i]=1
print(dic)

