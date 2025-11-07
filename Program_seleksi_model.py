#Lina Lisnawati
#1A
#NIM: 2507427

while True :
    print("program 'Discover The Next Talent'")
    print("Selamat datang ke dalam program Discover The Next Talent!\n Apakah Anda akan menjadi bintang selanjutnya?")
    print("Silahkan masukkan data diri anda.")

    gender = input("Masukan jenis kelamin anda : ")
    umur = int(input("Masukkan umur anda : "))
    tinggi = int(input("Masukkan tinggi badan anda : "))
    iq = int(input("Masukkan besaran IQ anda : "))

    if(gender == "wanita"):
        if(umur >=18 and umur <= 25):
            if(tinggi == 170):
                if(iq >= 130):
                    print(" Selamat Anda layak untuk menjadi model Catwalk!")
                else:
                    print(" mohon maaf, Iq anda belum memenuhi kriteria. ")
            else:
                print(" Mohon maaf, Tinggi anda tidak memenuhi kriteria.")
        else:
            print(" Mohon maaf, Umur anda tidak memenuhi kriteria.")
    elif( gender == "pria"):
        if(umur >=18 and umur <= 25):
            if(tinggi == 175):
                if(iq >= 130):
                    print(" Selamat Anda layak untuk menjadi model Catwalk!")
                else:
                    print("Mohon maaf, Iq anda belum memenuhi kriteria.")
            else:
                print("Mohon maaf, Tinggi anda tidak memenuhi kriteria.")
        else:
            print("Mohon maaf, Umur anda tidak memenuhi kriteria.")
    else:
        print("Input jenis kelamin yang dimasukkan tidak valid, harap masukkan 'Pria' atau 'Wanita'.")

    lanjutan = input("apakah anda ingin mencoba lagi? ketik 'Ya' atau 'Tidak': ").lower
    if lanjutan == "tidak":
        print("\nTerima kasih telah mengikuti program 'Discover The Next Talent'!")
        break