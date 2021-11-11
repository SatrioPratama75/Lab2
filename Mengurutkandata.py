#Mengurutkan data dari kecil kebesar

print("~"*39)

umur_adik = input("Umur adik : ")
umur_kakak = input("Umur kakak : ")
umur_ayah = input("Umur ayah : ")
umur_ibu = input("Umur ibu : ")

data = [umur_adik, umur_kakak, umur_ayah, umur_ibu]

#Fungsi .sort() untuk mengurutkan bilangan kecil ke besar
data.sort()

print("Maka urutan umur dari termuda hingga tertua adalah :",data)