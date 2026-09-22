# Input: satu bilangan bulat
# Aturan: menentukan bilangan negatif,nol,potisif genap, atau positif ganjil
# Output: kategori bilangan

x  = int(input("Masukan bilangan bulat:"))

if x < 0:
   print("bilangan negatif")
elif x == 0:
   print("Nol")
elif x % 2 == 0:
   print("bilangan positif genap")
else:
   print("bilangan positif ganjil")