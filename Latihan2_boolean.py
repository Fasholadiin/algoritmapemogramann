#setting variable
n1  = input("masukkan nim")
n2  = input("masukkan nama lengkap")
n3  = input("masukkan kelas")
n4  = input("masukkan nama prodi")

#setting variable nilai
b_ind  = int(input("Nilai Bahasa indonesia  :"))
b_ing  = int(input("Nilai Bahasa Inggris    :"))
pd     = int(input("Nilai Pemrograman Dasar :  "))
mtk    = int(input("Nilai Matematika        :  "))
kal1   = int(input("Nilai Kalkulus          :   "))

#perhitungan
rata = (b_ind+b_ing+pd+mtk+kal1)/5

if(rata > 0 and rata <=60):
   grade_rata = ("c")
elif(rata >60 and rata <=75) :
    grade_rata = ("b")
elif(rata >75 and rata <=85) :
    grade_rata = ("AB")
elif(rata >85 and rata <=100) :
    grade_rata = ("A")
else: 
    grade_rata =("Grade Anda Tidak ditemukan! ")
   
#menampilkan
print("----------------------")
print("    kartu hasil studi     ")
print("----------------------")
print ("Nim           :",n1)
print ("nama lengkap  :",n2)
print ("kelas         :",n3)
print ("program study :",n4)
print ("----------------------")
print ("No  Nama Makul   Nilai   Grade  ")
print ("----------------------")
print ("1.  bahasa Indonesia  ",b_ind)
print ("2.  bahasa Inggris    ",b_ing)
print ("3.  Pemrograman Dasar ",pd)
print ("4.  matematika        ",mtk)
print ("5.  Kalkulus 1        ",kal1)
print ("----------------------")
print ("Rata-Rata             ",rata," ",grade_rata)
print ("----------------------")
   
