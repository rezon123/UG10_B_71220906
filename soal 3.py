print ("Selamat Datang Di Program Pengurutan Bilangan")
print ("")
print ("Silahkan Pilih Metode Yang Akan Dipakai")
print ("1. Ascending")
print ("2. Descending")
print ("")
pil1 = int(input(">> "))
print ("")

if pil1 == 1:
    pil1 = int(input("Masukan Bilangan Bulat Pertama >> "))
    pil2 = int(input("Masukan Bilangan Bulat Kedua >> "))
    pil3 = int(input("Masukan Bilangan Bulat Ketiga >> "))
    pil4 = int(input("Masukan Bilangan Bulat Keempat >> "))
    list1 = [pil1 , pil2 , pil3 , pil4]
    print ("Urutan angka anda ", sorted(list1))
elif pil1 == 2:
    pil1 = int(input("Masukan Bilangan Bulat Pertama >> "))
    pil2 = int(input("Masukan Bilangan Bulat Kedua >> "))
    pil3 = int(input("Masukan Bilangan Bulat Ketiga >> "))
    pil4 = int(input("Masukan Bilangan Bulat Keempat >> "))
    list1 = [pil1 , pil2 , pil3 , pil4]
    print ("Urutan angka anda ", sorted(list1,reverse=True))
else:
    print ("Input anda salah")