# Nama : Lina Lisnawati
# NIM : 2507427
# kelas : 1A

print("PROGRAM Discover The Next Talent")

print("selamat datang Discoverers! di program login Discover The Next Talent,\n Silahkan Login (^__^) ")
kesempatan = 3

for i in range (kesempatan):
    username = input("Masukkan Username anda : ")
    Password = input("masukkan Password anda : ")

    if username == "Star" and Password == "talent234":
        print("Login Berhasil! Selamat datang di sistem TechnoWorks!")
    else:
        Sisa = kesempatan - (i+1)
        if Sisa > 0 :
            print (f"Login Salah! Kesempatan tersisa {Sisa} kali lagi.")
        else :
            print ("Akses ditolak. Anda telah gagal login 3 kali. Silakan hubungi Kepala HRD untuk mereset password")
