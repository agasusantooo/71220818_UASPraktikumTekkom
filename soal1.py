username=["brucewayne","victorstone","ciscoramon"]
anggotajusticeleague=[]
def menu():
    print("1. Tambah Anggota Justice League")
    print("2. Hapus Anggota Justice League")
    print("3. Tampilkan Anggota Justice League")
    print("4. Exit")
    pilihanmenu=int(input("Masukkan pilihan anda :"))
    if (pilihanmenu==1):
        anggotabaru=input("Nama Anggota baru :")
        anggotajusticeleague.append(anggotabaru)
        print("data '",anggotabaru,"'berhasil ditambahkan")
        menu()
    elif(pilihanmenu==2):
        anggotadihapus=input("Anggota yang akan dihapus :")
        if(anggotadihapus in anggotajusticeleague) :
            anggotajusticeleague.remove(anggotadihapus)
            print("data '",anggotadihapus,"' berhasil dihapus")
        else :
            print("data '",anggotadihapus,"' tidak ditemukan")
        menu()
    elif(pilihanmenu==3):
        print("Daftar Anggota Justice League")
        print(anggotajusticeleague)
        menu()
    elif(pilihanmenu==4) :
        print("see u nex time MR.",inputname,"GLHF")

print("==========================================")
print("************* Justice League *************")
print("==========================================")
inputname=input("Masukan username anda: ")
if(inputname in username) :
    print("===== WELCOME ", inputname,"======")
    menu()


else:
    print("Access Denied")
