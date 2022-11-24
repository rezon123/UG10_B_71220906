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
    vol_limas = alaslimas * alaslimas * tinggilimas * 1/3
    print("volume limas tersebut adalah", vol_limas)
    pilihan = int(input("masukkan pilihan anda: "))
elif pilihan == 2:
    pjarijaribola = int(input("masukkan panjang jari-jari bola: "))
    vol_bola = (4/3 * pjarijaribola**3*3.14)
    print("volume bola tersebut adalah", vol_bola)
    pilihan = int(input("masukkan pilihan anda: "))
