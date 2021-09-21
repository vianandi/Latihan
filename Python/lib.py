class mahasiswa(object):
    def __init__(self,nim,nama,nUTS, nUAS, nTugas):
        #Konstruktor
        self.nim = nim
        self.nama = nama
        self.nUTS = nUTS
        self.nUAS = nUAS
        self.nTugas = nTugas

    def uts(self):
        return self.nUTS*(35/100)
    
    def uas(self):
        return self.nUAS*(35/100)

    def tugas(self):
        return self.nTugas*(30/100)

    def nilaiakhir(self):
        return self.uts()+self.uas()+self.tugas()

    def nilaihuruf(self):
        nHuruf = ''
        if (self.nilaiakhir()>=85 and self.nilaiakhir()<=100):
            nHuruf = 'A'
        elif (self.nilaiakhir()>=70 and self.nilaiakhir()<=85):
            nHuruf = 'B'
        elif (self.nilaiakhir()>=60 and self.nilaiakhir()<=70):
            nHuruf = 'C'
        elif (self.nilaiakhir()>=40 and self.nilaiakhir()<=60):
            nHuruf = 'D'
        else:
            nHuruf = 'E'
        return nHuruf
        
    def predikat(self):
        if (self.nilaihuruf()=='A'):
            return "Cumlaude"
        elif (self.nilaihuruf()=='B'):
            return "Baik"
        elif (self.nilaihuruf()=='C'):
            return "Cukup"
        elif (self.nilaihuruf()=='D'):
            return "Kurang"
        else:
            return "Sangat Kurang"

    def __str__(self):
        cetak = """
        Nim         : {}
        Nama        : {}
        Nilai UTS   : {}
        Nilai UAS   : {}
        Nilai Tugas : {}
        Nilai Akhir : {} + {} + {} = {}
        Nilai Huruf : {}
        Predikat    : {}
        """.format(self.nim,self.nama,self.nUTS,self.nUAS,self.nTugas,self.uts(),self.uas(),self.tugas(),self.nilaiakhir(),self.nilaihuruf(),self.predikat())
        return cetak

def main():
    Vian = mahasiswa("A11.2020.12920","Oktavian Andi Cahya Nugraha",100,100,100)
    print(Vian)
if __name__=='__main__':
    main()

