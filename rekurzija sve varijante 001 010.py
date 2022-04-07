a=[0,0,0]
def rekurzija (i):
    if (i==len(a)):
        print(a)
    else:
        a[i]=0
        rekurzija(i+1)
        a[i]=1
        rekurzija(i+1)
rekurzija(0)
