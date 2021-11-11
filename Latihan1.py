#Membuat program menentukan niali akhir

nama = input("Masukan Nama : ")
uts = input("Masukan Nilai UTS : ")
uas = input("Masukan Nilai UAS : ")
tugas = input("Masukan Nilai Tugas : ")

hasil = (int(tugas)*.2) + (int(uts)*.4) + (int(uts)*.4)
keterangan = ("TIDAK LULUS" , "LULUS") [hasil > 60]
if hasil > 80:
    huruf = "A"
elif hasil > 70:
    huruf = "B"
elif hasil > 50:
    huruf = "C"
elif hasil > 40:
    huruf = "D"
else :
    huruf = "E"

print("\nNama", nama)
print("UTS", uts)
print("UAS", uas)
print("Tugas", tugas)
print("Hasil", hasil)
print("Huruf", huruf)
print("Keterangan", keterangan)