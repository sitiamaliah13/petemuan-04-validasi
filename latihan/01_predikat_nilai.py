# Input: satu nilai akhir 
# Aturan: menentukan predikat A sampe E 
# Output: predikat nilai

nilai = float(input("Nilai akhir (0-100): "))

if nilai >= 85 :
    predikat = "A"
elif nilai >= 70 :
    predikat = "B"
elif nilai >= 60 :
    predikit = "C"
elif nilai >= 50 :
    predikat = "D"
else:
    predikat = "E"

print(f"Nilai {nilai:.2f} memperoleh predikat{predikat}.")
