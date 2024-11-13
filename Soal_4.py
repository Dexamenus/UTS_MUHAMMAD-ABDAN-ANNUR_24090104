brt = float(input('Masukan Berat badan (Kg) : '))
ttg = float(input("Masukan Tinggi Badan (meter) : "))

bmi = brt/ttg

if bmi < 18.5:
    hasil = ("Berat Badan Kurang")
elif 18.5 <= bmi <24.9:
    hasil = ("Berat Badan Normal")
elif 25 <= bmi < 29.9:
    hasil = ("Kelebihan Berat Badan")
else:
    hasil = ("Obesitas")

print("Berat Badan  : ",brt)
print("Tinggi Badan : ",ttg)
print("-"*50)
print("Nilai BMI Anda   : ",bmi)
print("Kategori BMI     : ",hasil)

