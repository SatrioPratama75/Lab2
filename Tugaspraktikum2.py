#Menampilkan bilangan terbesar

a = input("Masukan Bilangan A : ")
b = input("Masukan Bilangan B : ")
c = input("Masukan Bilangan C : ")

if a > b and a > c :
    print("Maka Bilangan A yang terbesar")
elif b > c and b > a :
    print("Maka Bilangan B yang terbesar")
else :
    print("Maka Bilangan C yang terbesar")