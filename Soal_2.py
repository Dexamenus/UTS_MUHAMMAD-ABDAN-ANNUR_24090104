thn = int(input('Masukan Tahun : '))

if thn % 400 == 0:
    hasil = (f"Tahun {thn} merupakan TAHUN KABISAT")
elif thn % 4 == 0 :
    hasil = (f"Tahun {thn} merupakan TAHUN KABISAT")
else:
    hasil = ("Bukan Tahun Kabisat")

print(hasil)
    