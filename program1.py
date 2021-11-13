print("Program Menghitung Laba Perusahaan Dengan Modal Awal 100 Juta")
print("")
print("Note:")
print("Bulan Pertama Dan Ke-2 = 0%")
print("Pada Bulan Ke-3 = 1$")
print("Pada Bulan Ke-5 = 5%")
print("Pada Bulan Ke-8 = 2%")
print("")

a = 100000000
for x in range(1,9):
    if(x>=1 and x<=2):
        b = a*0
        print("Laba Bulan Ke-",x," : ",b)
    if(x>=3 and x<=4):
        c = a*0.1
        print("Laba Bulan Ke-",x," : ",c)
    if(x>=5 and x>=7):
        d = a*0.5
        print("Laba Bulan Ke-",x," : ",d)
    if(x==8):
        e = a*0.2
        print("Laba Bulan Ke-",x," : ",e)
total=b+b+c+c+d+d+d+e
print("\nTotal : ",total)
