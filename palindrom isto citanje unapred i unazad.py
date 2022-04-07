a=[1,2,3,3,2,3]
ind=True 
for i in range(len(a)//2):   # i da ide do pola, do polovine ove liste
     if(a[i]!=a[len(a)-1-i]): 
        ind=False
        break

if (ind==True):
    print (a)
    print ("JESTE PALINDROM")
    
else:
    print (a)
    print ("NIJE PALINDROM")




'''PODPROGRAM U PYTHON-u je FUNKCIJA
a=3
b=4
c=a+b
print(c)

def imePodprograma(): #podprogram, uvek ide () na kraju podprograma.
    imePodprograma() # poziv podprograma
    print(ABV)#telo podprograma'''




# def zbir(a,b):
#     print (a+b)

# zbir(5,4)



