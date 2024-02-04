def hitung_karakter(string):
    kapital = sum(1 for char in string if char.isupper())
    kecil = sum(1 for char in string if char.islower())

    return kapital ,kecil

kalimat = input("masukan sebuah kalimat: ")

jumlah_kapital, jumlah_kecil = hitung_karakter(kalimat)

print(f"Jumlah Huruf Kapitals: {jumlah_kapital}")
print(f"Jumlah Huruf kecil: {jumlah_kecil}")

print(f"Total Huruf Keseluruhan: {jumlah_kapital + jumlah_kecil + 1}")