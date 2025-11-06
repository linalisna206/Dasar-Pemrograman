#Lina Lisnawati
#kelas: 1A
#NIM: 2507427

tugas = int(input("masukkan nilai penguasaan materi : "))
uts =int(input ("masukkan nilai kreatifitas : "))
uas = int(input("masukkan nilai presentasi : "))

jumlah_total = (tugas + uts + uas / 3 )

if(jumlah_total == 0):
    print("Anda BELUM LULUS, Silahkan lakukan remedial")
elif(jumlah_total >= 70):
    if(tugas >= 60 and uts >= 60 and uas >= 60):
        print(f"nilai Tugas anda {tugas}, nilai UTS anda {uts}, nilai UAS anda {uas} nilai akhir anda {jumlah_total.round()}")
        print("selamat anda LULUS tanpa remedial")
    else :
        print(f"nilai Tugas anda {tugas}, nilai UTS anda {uts}, nilai UAS anda {uas} nilai akhir anda {jumlah_total}")
        print("Selamat anda LULUS dengan remedial")
elif(jumlah_total < 70):
    if(jumlah_total<= 50):
        print(f"nilai Tugas anda {tugas}, nilai UTS anda {uts}, nilai UAS anda {uas} nilai akhir anda {jumlah_total}")
        print("Maaf Anda Tidak Lulus dan boleh remedial")
    else :
        print(f"nilai Tugas anda {tugas}, nilai UTS anda {uts}, nilai UAS anda {uas} nilai akhir anda {jumlah_total}")
        print("Maaf Anda TIDAK LULUS dan tidak boleh remedial")
