from stringprep import in_table_c21
import math as m

print('Hello World')

bil1=input('Masukan bil1: ')
bil2=input('Masukan bil2: ')

bil1=float(bil1)
bil2=float(bil2)

result=bil1+bil2 
print('Sum of %0.2f and %0.2f is %0.2f' % (bil1, bil2,result))

result1= bil1*bil2

print('%0.2f * %0.2f = %0.2f' % (bil1, bil2,result1))

C=float(input('Masukkan temperatur C: '))

F=1.8*C+32
K=273.15+C

print("%0.3f C = %0.3f F" %(C, F))
print("%0.3f C = %0.3f K" %(C, K))

p=float(input("Masukan jumlah uang: "))
t=float(input("Masukan waktu: "))
rate= float(input("Masukkan rate: "))

simple_interest= (p*t*rate)/100
compound_interest= p*((1+rate/100)**t -1)

print('simple interest: %f' %(simple_interest))
print('Compund interest: %f' %(compound_interest))

panjang=float(input("Masukkan panjang: "))
lebar=float(input("Masukkan luas: "))

luas_persegi_panjang=panjang*lebar 

keliling_persergi_panjang=2*(panjang+lebar)

print("luas pesergi panjang = ", luas_persegi_panjang)
print("Keliling persegi panjang= ", keliling_persergi_panjang)

jari_jari=float(input("Masukkan jari-jari: "))

luas_lingkaran=m.pi*jari_jari**2

keliling_lingkaran=2*m.pi*jari_jari

luas_bola=4*m.pi*jari_jari**2

volume_bola=(4/3)*m.pi*jari_jari**3

print("luas lingkaran = %0.4f" % luas_lingkaran)
print("Keliling lingkaran = %0.4f" % keliling_lingkaran)

print("luas bola = %0.4f" % luas_bola)
print("Volume bola = %0.4f" % volume_bola)


alas=float(input("Masukkan alas: "))
tinggi=float(input("Masukkan tinggi: "))

luas_segitiga=(1/2)*alas*tinggi 

print("Luas segitiga: %f" %(luas_segitiga))

major=float(input("Masukkan panjang major: "))
minor=float(input("Masukkan panjang minor: "))

luas_elips=m.pi*major*minor 

print("Luas elips: ", luas_elips)

jari_jari_kerucut=float(input("Masukkan jari-jari:"))
tinggi_kerucut = float(input("Masukkan tinggi : "))
luas_kerucut = m.pi*jari_jari_kerucut*(jari_jari_kerucut+m.sqrt(jari_jari_kerucut**2+tinggi_kerucut**2))
print("luas kerucut: ", luas_kerucut)

x1=float(input("Masukkan x1: "))
y1=float(input("Masukkan y1: "))
x2=float(input("Masukkan x2: "))
y2=float(input("Masukkan y2: "))

jarak_dua_titik=m.sqrt((x2-x1)**2+(y2-y1)**2)
print("jarak dua titik = %f" %(jarak_dua_titik))

x=float(input("Masukkan koordinat x: "))
y=float(input("Masukkan koordinat y: "))
