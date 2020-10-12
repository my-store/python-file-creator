
import os

credit = """
|
|   FILE CREATOR - ROMBAX FAMILY BREBES JAWA TENGAH
|
|   Creator  : Izzat alharis
|   Phone    : (+62) 813-9355-2220
|   Email    : izzatalharis@gmail.com
|   Github   : https://github.com/my-store
|"""

class NggaweFile :
    def __init__(NF,Aran_Folder,Aran_File,Type_File) :
        NF.Aran     = Aran_File
        NF.Folder   = Aran_Folder
        NF.Tipe     = Type_File
        NF.Mandor   = credit
        NF.gawe(NF.Tipe)

    def gawe(NF,fType) :
        if not os.path.isdir(NF.Folder) :
            os.mkdir(NF.Folder)

        NF.File = open(NF.Folder+"/"+NF.Aran+"."+fType,"w")
        NF.tulis(fType)
        NF.File.close()
        print("File `"+NF.Aran+"."+fType+"` teng folder `"+NF.Folder+"` sampun dados!")

    def tulis(NF,fType) :
        NF.File.write("\n/*\n"+NF.Mandor+"\n*/\n\n")

print("\n===== FILE CREATOR ======\n")
namaFile = input("Silahkan isi nama file : ")
jenisFile = input("Silahkan isi jenis file : ")
namaFolder = input("Silahkan isi nama folder : ")
NggaweFile(namaFolder,namaFile,jenisFile)