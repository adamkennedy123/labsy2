#Menampilkan bilangan, berhenti ketika bilangan 0, dan menampilkan bilangan terbesar
a=1
max=0
while a!=0:
    if a>max:
        max=a
    a=int(input('Masukkan bilangan :'))
    if a==0:
         break
        
print ('Nilai terbesarya adalah :',max)
