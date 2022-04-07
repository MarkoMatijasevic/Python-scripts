# brc=0
# for i in range(1,1001):
#     m=i
#     brc=0
#     while(m>0):
#         brc+=1
#         m=m//10
#     print(brc)

#pokazuje koliko ima cifara, armstrongovih brojeva u nizu od 1 do 1000

#drugacije resenje i to za brojeve od 1 do 1.000.000
brojcifara=1
for i in range(1,1000001):
    if (i==10 or i==100 or i==1000 or i==10000 or i==100000 or i==1000000):
        brojcifara+=1
    suma=0
    pom=i
    while(pom>0):
        suma=suma+(pom%10)**brojcifara
        pom = pom//10
    if(i==suma):
        print(i,end=" ")

