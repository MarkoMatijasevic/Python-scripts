def fun4(i):
    if(i<0):
        print("Poziv iz funkcije ", i)
        fun4(i-1)

print(fun4(3))

