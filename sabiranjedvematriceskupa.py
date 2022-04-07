
#dve petlje, jedna ide kroz vrste druga kroz kolone
matt=[[1,2], [3,3]]
result= []
for i in matt:
    r=[]
    for j in i:
        r.append(j+j)
    result.append(r)
print(result)