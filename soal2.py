print("===== Selamat datang di XXV ====")
tanggal=int(input("Masukkna tanggal hari ini: "))
if(tanggal%2==0):
    print("== Berikut genre film yang tersedia ==")
    print("1. Horror")
    print("2. Action")
    genre=int(input("Silahkan pilih mau nonton film bergenre apa :"))
    if(genre==1) :
        print("== Berikut pilihan film horror yang sedang tayang ==")
        print("1. The Devil's Light")
        print("2. Pengabdi Setan")
        pilihanfilm=int(input("Silahkan mau nonton film apa :"))
        jumlahtiket=int(input("Mau memesan tiket sebanyak :"))
        harga=jumlahtiket*25000
        print("Total yang harus dibayar adalah RP", harga-(harga*2/100))
    elif(genre==2) :
        print("== Berikut pilihan film horror yang sedang tayang ==")
        print("1. Black Panther : Wakanda Forever")
        print("2. Avatar: The Way of Water")
        pilihanfilm=int(input("Silahkan mau nonton film apa :"))
        jumlahtiket=int(input("Mau memesan tiket sebanyak :"))
        harga=jumlahtiket*25000
        print("Total yang harus dibayar adalah RP", harga-(harga*2/100))
    elif(genre>2) :
        print("Pilihan yang anda pilih tidak tersedia di bioskop ini")
else:
    print("== Berikut genre film yang tersedia ==")
    print("1. Horror")
    print("2. Action")
    genre=int(input("Silahkan pilih mau nonton film bergenre apa :"))
    if(genre==1) :
        print("== Berikut pilihan film horror yang sedang tayang ==")
        print("1. The Devil's Light")
        print("2. Pengabdi Setan")
        pilihanfilm=int(input("Silahkan mau nonton film apa :"))
        jumlahtiket=int(input("Mau memesan tiket sebanyak :"))
        harga=jumlahtiket*25000
        print("Total yang harus dibayar adalah RP", harga)
    elif(genre==2) :
        print("== Berikut pilihan film horror yang sedang tayang ==")
        print("1. Black Panther : Wakanda Forever")
        print("2. Avatar: The Way of Water")
        pilihanfilm=int(input("Silahkan mau nonton film apa :"))
        jumlahtiket=int(input("Mau memesan tiket sebanyak :"))
        harga=jumlahtiket*25000
        if (jumlahtiket>4):
            hargadiskon=harga-(harga*5/100)
            print("Total yang harus dibayar adalah RP", hargadiskon)
        else:
            print("Total yang harus dibayar adalah RP", harga)
    elif(genre>2) :
        print("Pilihan yang anda pilih tidak tersedia di bioskop ini")