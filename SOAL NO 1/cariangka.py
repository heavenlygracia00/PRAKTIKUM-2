x = float(input("Masukkan angka pertama : "))
y = float(input("Masukkan angka kedua : "))

if x > y:
    print(f"Angka maksimal adalah {x}")
elif y > x:
    print(f"Angka maksimal adalah {y}")
else:
    print(f"Kedua angka sama besar, yaitu {x}")