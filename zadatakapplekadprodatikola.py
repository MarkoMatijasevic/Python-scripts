a= [9,11,8,5,7,10]
max=0
for i in range(len(a)):
    for j in range(i,len(a)):
        if (a[j]-a[i]>max):
            max= a[j]-a[i]
            maxi=a[i]
            maxj=a[j]
print("Zarada:"+str(max)+"Kupljeno:"+str(maxi)+"Prodato:"+str(maxj))
