n = 12321
m=n#ovo se dodaje ako hocemo da vidimo da li je palindrom
inverz=0
while(n>0):
    inverz = 10*inverz+n%10
    n=n//10
print(inverz)

if (m==inverz): #ovo se dodaje ako hocemo da vidimo da li je palindrom
    print("JESTE PALINDROM")#ovo se dodaje ako hocemo da vidimo da li je palindrom



def rek(m,inverz):
    if(m==0):
        return inverz
    return rek(m=m//10,inverz=10*inverz+m%10) #repna rekurzija, tail recursion koja uvek moze da se pretvori u iterativno resenje, sto nije slucaj sa svakom rekurzijom




print(rek(m,0))
