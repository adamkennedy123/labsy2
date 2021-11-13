def sorting (data):
    ganti = True
    while len(data)-1 > 0 and ganti:
        ganti= False
        for i in range (len(data)-1):
            if data [i] > data [i+1]:
                ganti =True
                swap = data[i]
                data[i] = data[i+1]
                data [i+1] = swap
               
data = []
print("program mengurutkan angka")
inputBilangan =int(input("masukan angka A:"))
data.append(inputBilangan)
masukanBilangan  =int(input("masukan angka B:"))
data.append(masukanBilangan)
Bilangandata =int(input("masukan angka C:"))
data.append(Bilangandata)
sorting(data)
print('urutkan:',data)
