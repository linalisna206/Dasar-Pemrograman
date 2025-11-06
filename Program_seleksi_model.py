#Lina Lisnawati
#1A
#NIM: 2507427

print("program 'Discover The Next Talent'")
print("Selamat datang ke dalam program, silahkan lengkapi identitas anda")

gender = input("Masukan jenis kelamin anda : ")
umur = int(input("Masukkan umur anda : "))
tinggi = int(input("Masukkan tinggi badan anda : "))
iq = int(input("Masukkan besaran IQ anda : "))

if( umur >=18 and umur <= 25 and iq >= 130):
    if( gender == "wanita" and tinggi == 170):
        print(" Selamat Anda layak untuk menjadi model Catwalk!")
    if( gender == "pria" and tinggi == 175):
        print(" Selamat Anda layak untuk menjadi model Catwalk!")
else :
    print(" Maaf, Anda belum layak untuk menjadi model Catwalk")
