#Membuat program menampilkan status gaji karyawan

gaji = int(input("Masukan gaji : "))
berkeluarga = (False, True)[input("Sudah berkeluarga? (Ya/Tidak) ") == "Ya"]
punya_rumah = (False, True)[input("Punya rumah? (Ya/Tidak) ") == "Ya"]
if gaji > 3000000:
    print("Gaji sudah diatas UMR")
    if berkeluarga:
        print("Wajib mengikuti asuransi dan menabung untuk pensiun")
    else:
        print("Tidak perlu mengikuti asuransi dan menabung untuk pensiun")
    if punya_rumah:
        print("Wajib membayar pajak rumah")
    else:
            print("Tidak wajib membayar pajak rumah")
else :
    print("Gaji belum UMR")