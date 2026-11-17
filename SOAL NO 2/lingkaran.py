import math

print("LATIHAN LINGKARAN")
print("1. Menghitung Keliling Lingkaran")
print("2. Menghitung Luas Lingkaran")

pilihan = int(input("Masukkan pilihan (1/2) : "))
r = float(input("Masukkan nilai jari-jari : "))

if pilihan == 1:
    keliling = 2 * math.pi * r
    print(f"Keliling lingkaran adalah {keliling:.2f}")
elif pilihan == 2:
    luas = math.pi * r * r
    print(f"Luas lingkaran adalah {luas:.2f}")
else:
    print("Pilihan tidak valid! Masukkan 1 atau 2 saja.")