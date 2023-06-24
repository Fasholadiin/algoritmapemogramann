#setting Variable
n1  =   input("MASUKAN NAMA LENGKAP ANDA  ")
n2  =   input("MASUKKAN NIM ANDA  ")
n3  =   input("MASUKKAN KELAS ANDA  ")
n4  =   input("MASUKKAN PRODI ANDA  ")

print('\nPERHATIAN!!\n UNTUK MENJAWAB SOAL CUKUP DENGAN MENGETIK A/B/C/D LALU ENTER\n')
#setting variable soal
s1  =   str(input("1.   KAMBING MEMILIKI KAKI BERAPA? \n A. 3    C.4 \n B. 2 D. 1\n "))
s2  =   str(input("2.   Negara terluas keempat di dunia adalah? \n A. Indonesia    C. Rusia \n B. Amerika D. Afrika\n "))
s3  =   str(input("3.   Jenis kumbang terbesar adalah kumbang? \n A. Goliath    C. Ladybug \n B. Kunang-kunang D. Kumbang Daun\n "))
s4  =   str(input("4.   Arah jam 9 itu sama dengan arah? \n A. Utara    C. Timur \n B. Selatan D. Barat\n "))
s5  =   str(input("5.   Pulau Komodo terletak di provinsi?  \n A.Bali     C. NTT \n B. NTB D. Jawa Timur\n "))


#setting variable jawaban

#jawaban soal 1
if(s1=='C'): 
    j1=('C. (4) \nSelamat jawaban anda benar')
else :
    j1=('C. (4) \nmaaf jawaban anda salah')

#jawaban soal 2
if(s2=='B'): 
    j2=('B. (Amerika) \nSelamat jawaban anda benar')
else :
    j2=('B. (Amerika) \nmaaf jawaban anda salah')

#jawaban soal 3
if(s3=='A'): 
    j3=('A. (Goliath) \nSelamat jawaban anda benar')
else :
    j3=('A. (Goliath) \nmaaf jawaban anda salah')

#jawaban soal 4
if(s4=='D'): 
    j4=('D. (Barat) \nSelamat jawaban anda benar')
else :
    j4=('D. (Barat) \nmaaf jawaban anda salah')

#jawaban soal 5
if(s5=='C'): 
    j5=('C. (NTT) \nSelamat jawaban anda benar')
else :
    j5=('C. (NTT) \nmaaf jawaban anda salah')

#MENAMPILKAN
print("-----------------------------")
print("    KARTU IDENTITAS MAHASISWA     ")
print("-----------------------------")
print ("Nim           :",n1)
print ("nama lengkap  :",n2)
print ("kelas         :",n3)
print ("program study :",n4)
print ("-----------------------------")

print ('KAMBING MEMILIKI KAKI BERAPA? ', j1)
print ('Negara terluas keempat di dunia adalah? ', j2 )
print ('Jenis kumbang terbesar adalah kumbang? ', j3)
print ('Arah jam 9 itu sama dengan arah? ', j4)
print ('Pulau Komodo terletak di provinsi? ', j5)
