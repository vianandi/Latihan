from lib import *

def main():

    jml_mhs = int(input("Masukkan banyak mahasiswa = "))
    mhs = []
    urutan=1
    for m in range(jml_mhs):
        print("mahasiswa ke-",urutan)
        urutan+=1

        nim = input("masukkan NIM = ")
        nama = input("masukkan Nama = ")
        nilai_uts = float(input("masukkan nilai UTS = "))
        nilai_uas = float(input("masukkan nilai UAS = "))
        nilai_tugas = float(input("masukkan nilai Tugas = "))

        mhs_baru = mahasiswa(nim, nama, nilai_uts, nilai_uas, nilai_tugas)

        mhs.append(mhs_baru)
        print("")

    i = 1
    print("| No\t| NIM\t | Name\t| Nilai Akhir\t|")
    print("-----------------------------------")
    for m in mhs:
        print("| {}\t| {}\t| {}\t| {}\t\t".format(i, m.nim, m.nama, m.nilaiakhir()))
        i+=1

    pil = input("Apakah ingin mengupdate nilai tugas mahasiswa (y/n)? ")
    if(pil=="y" or pil=='Y'):
        pilU = int(input("mahasiswa dengan nomor urut berapa? "))
        nilaiTugasBaru = float(input("berapa nilai tugas baru? "))
        mhs[pilU-1].nTugas = nilaiTugasBaru
    else:
        print("Data mahasiswa tidak berubah")

    i = 1
    print("| No\t| NIM\t| Nama\t| Nilai akhir\t|")
    print("-----------------------------------------")
    for m in mhs:
        print("| {}\t| {}\t| {}\t| {}\t\t|".format(i, m.nim, m.nama, m.nilaiakhir()))
        i+=1

    pil = input("Apakah ingin menghapus data mahasiswa (y/n)? ")
    if(pil=="y" or pil=='y'):
        pilH = int(input("Masukkan dengan nomor urut berapa? "))
        del mhs[pilH-1]
    else:
        print("Data mahasiswa tidak berubah")

    i = 1
    print("| No\t| NIM\t| Nama\t| Nilai Akhir\t|")
    print("------------------------------------------")
    for m in mhs: 
        print("| {}\t| {}\t| {}\t| {}\t\t|".format(i, m.nim, m.nama, m.nilaiakhir()))
        i+=1

    min = 100
    max = 0
    for m in mhs:
        if m.nilaiakhir()<min:
            min = m.nilaiakhir()
            namaMin = m.nama
        if m.nilaiakhir()>max:
            max = m.nilaiakhir()
            namaMax = m.nama
    print("Masukan data Ipk terendah adalah {} dengan perolehan IPK {}".format(namaMin, min))
    print("Masukan data Ipk tertinggi adalah {} dengan perolehan IPK {}".format(namaMax, max))

if __name__=="__main__":
    main()




