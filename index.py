import json
from prettytable import PrettyTable

MATA_KULIAH = "Sistem Informasi"

# BACA
def lihat_data():
    with open ("data.json", "r") as f:
        return json.load(f)

# SIMPAN
def simpan_data(data):
    with open ("data.json", "w") as f:
        json.dump(data, f, indent=4)

# TAMPILAN
def tampilkan_data():
    data = lihat_data()
    if len(data) == 0:
        print("Belum ada data Nilai")
        return
    tabel = PrettyTable()
    tabel.field_names = ["NO", "NAMA", "NIM", "MATA KULIAH", "NILAI"]
    tabel.align = "l"
    tabel.align["NILAI"] = "r"

    for i, mhs in enumerate(data, start=1):
        tabel.add_row([i, mhs["NAMA"], mhs["NIM"], MATA_KULIAH, mhs["NILAI"]], divider=True)

    print(tabel)

# INPUT
def tambah_data():
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")

    try:
        nilai = float(input("Masukkan nilai mahasiswa: "))
    except ValueError:
        print("NIlai harus berupa angka!")
        return

    if nama == "" or nim == "":
        print("Nama dan NIM tidak boleh kosong")
        return
    if nilai < 0 or nilai > 100:
        print("Nilai harus 0-100!")
        return
    
    data = lihat_data()
    data.append({"NAMA": nama, "NIM": nim, "MATA KULIAH": MATA_KULIAH, "NILAI": nilai})
    simpan_data(data)
    print("Data berhasil disimpan!")

while True:
    print("=" * 35)
    print("REKAP NILAI MAHASISWA SISTEM INFORMASI")
    print("1. Lihat data nilai")
    print("2. Tambah data Mahasiswa")
    print("0. Keluar")
    print("=" * 35)
    pilih = input("Pilih menu: ")

    if pilih == "1":
        tampilkan_data()
    elif pilih == '2':
        tambah_data()
    elif pilih == "0":
        print("Terima Kasih!!")
        break
    else:
        print("Pilihan tidak tersedia")