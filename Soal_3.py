jml = int(input("Masukan Jumlah Barang : "))
ttl = 0
for x in range (jml):
    nilai = int(input(f"Masukan Harga Barang Ke-{x + 1} : "))
    ttl += nilai

print("Total Belanjaan : Rp.",ttl)
