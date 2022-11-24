print ("~~~~~~~~~~~~~~~ \('v')/ ~~~~~~~~~~~~~~~")
print ("PROGRAM PENGHITUNG VOLUME BANGUN RUANG")
print ("~~~~~~~~~~~~~~~ \('v')/ ~~~~~~~~~~~~~~~")
print ("pilihlah salah satu bangun ruang yang ingin dihitung volumenya")
print ("1. limas")
print ("2. bola")
print ("3. prisma")
print ("4. kerucut")

pilihan = int(input("masukkan pilihan anda: "))
if pilihan == 1:
    alaslimas = int(input("masukkan panjang sisi alas limas: "))
    tinggilimas = int(input("masukkan tinggi limas: "))
    vol_limas = alaslimas * alaslimas * tinggilimas
    print("volume limas tersebut adalah", vol_limas)