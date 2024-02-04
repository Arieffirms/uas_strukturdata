class Gudang:
    def __init__(self) -> None:
        self.daftar_barang = []

    def tambah_barang(self,barang):
        self.daftar_barang.append(barang)
    
    def tampilkan_barang(self):
        for barang in self.daftar_barang:
            print(barang)
    
    def mengurutkan_angka(self):
        self.daftar_barang.sort()

gudang_saya = Gudang()

while True:
    tambah_barang = input("Masukkan barang (atau ketik 'selesai' untuk mengakhiri): ")
    if tambah_barang == "selesai":
        break
    gudang_saya.tambah_barang(tambah_barang)

print("Daftar Barang:")
gudang_saya.mengurutkan_angka()
gudang_saya.tampilkan_barang()

