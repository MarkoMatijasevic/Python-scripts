n = 357
m=n   #ovo se dodaje ako hocemo da vidimo da li je palindrom
inverz=0
while(n>0):
    inverz = 10*inverz+n%10
    n=n//10
print(inverz)

if (m==inverz): #ovo se dodaje ako hocemo da vidimo da li je palindrom
    print("JESTE PALINDROM")#ovo se dodaje ako hocemo da vidimo da li je palindrom
else:
    print ("Nije palindrom")


