# Sistem Pencatatan Nilai Mahasiswa
**Nama :** Nova Cynthia <br>
**NIM :** 2609116031 <br>
**Program Studi :** Sistem Informasi <br>
**Kelas :** A 2026 <br>
**Mata Kuliah :** Dasar-Dasar Pemograman <br>

## DESKRIPSI
Program ini digunakan untuk keperluan guru atau dosen dalam menginput nilai tugas atau nilai ujian. Data yang sudah diinput tidak akan hilang ketika Pengguna keluar dari program. Saya menggunakan data JSON untuk menyimpan semua inputtan Pengguna, berikut kode-kode yang saya gunakan : <br>
1. ``JSON`` adalah cara menggunakan dan mengolah data. Data pemograman ini saya gunakan untuk menyimpan data-data yang sudah diinputkan oleh Pengguna.
2. ``prettytable`` adalah salah satu jenis library yang berfungsi untuk membuat tabel. Jenis library ini saya gunakan untuk membuat table dalam menu tampilan agar terlihat lebih rapi.
3. ``function`` berfungsi untuk blok kode dalam fungsi yang tidak akan dijalankan jika tidak dipanggil. Jenis tipe data ini saya gunakan di bagian pilihan menu.
4. ``While`` berfungsi melakukan perulangan atau *looping* pada intruksi yang diberikan yang tidak akan berhenti, kecuali terdapat transfer statement (continue dan break). Jenis *looping* ini digunakan pada bagian menu pilihan.
5. ``if`` berfungsi dalam pengambilan keputusan yang dilakukan oleh Pengguna dan program akan dijalankan sesuai dengan intruksi yang dibuat. Jenis *conditional statement* ini digunakan saat Pengguna memilih di menu pilihan.
6. ``elif`` berfungsi dalam menangani keputusan yang banyak pada pengambilan keputusan. Jenis *conditional statement* ini juga digunakan saat Pengguna memilih di daftar menu.
7. ``else`` berfungsi dalam pengambilan keputusan jika *if* tidak terpenuhi atau terlaksana. Jenis *conditional statement* ini digunakan saat Pengguna memilih di daftar menu ketika Pengguna memasukkan angka yang tidak sesuai dengan yang disediakan.
8. ``Error Handling`` berfungsi untuk mencegah program berhenti mendadak saat terjadi *exception*. Saya menggunakan *"try"* dan *"except"* dalam peng*input*an saat kondisi menambahkan dan menghapus menggunakan nomor.
9. ``break``berfungsi untuk menghentikan secara paksa program. Jenis *transfer statement* ini digunakan pada pemilihan "Exit" di bagian daftar menu.
10. ``continue`` berfungsi untuk melewatkan intruksi setelahnya atau kembali ke intruksi awal. Jenis *transfer statement* ini digunakan saat Pengguna memilih di daftar menu ketika Pengguna memasukkan angka yang tidak sesuai dengan yang disediakan.
11. ``print`` berfungsi untuk menampilkan intruksi yang kita berikan.
12. ``input`` berfungsi untuk memasukkan data dari Pengguna.
13. ``return`` berfungsi untuk menghentikan eksekusi sebuah fungsi dan mengembalikan nilai ke bagian program yang memanggilnya. Digunakan untuk mengembalikan nilai ke bagian menu pilihan.

## OUTPUT
### Output Menu Pilihan
Pada bagian ini, Pengguna diminta untuk menginputkan menu pilihan yang ingin Pengguna lakukan. Menu pilihan hanya akan mengeksekusi apabila input berupa angka, jika tidak berupa angka dan angka tidak tersedia akan menampilkan "Harus berupa angka!". Lalu program akan melakukan *looping* sampai Pengguna menginputkan berupa angka atau angka yang tersedia. <br>
<img width="450" alt="Screenshot 2026-10-07 213405" src="https://github.com/user-attachments/assets/d642b1ed-ef56-4b9e-8fa8-1e438297d66d" />
### Output Lihat Data
Pada salah satu bagian menu pilihan ini, Pengguna hanya dapat melihat data saat ini dan seteleah diperbarui. <br>
<img width="300" alt="Screenshot 2026-10-07 213727" src="https://github.com/user-attachments/assets/9a406775-9867-4450-b185-e9c66c58d845" />
### Output Input atau Menambahkan
Pada salah satu bagian menu pilihan ini, Pengguna dapat menginputkan nama, NIM, dan nilai untuk menambahkannya ke data JSON dan disimpan. Namun, apabila Pengguna tidak memasukkan nama atau NIM maka program tidak akan menambahkan data tersebut, lalu rogram akan melakukan *looping* sampai Pengguna menginputkan nama atau NIM. <br>
<img width="400" alt="Screenshot 2026-10-07 214120" src="https://github.com/user-attachments/assets/4da580af-26e2-4c41-91a1-7b401a34a4a1" />
<br>
#### Output apabila tidak memasukkan nama atau NIM <br>
<br>
<img width="300" alt="Screenshot 2026-10-07 214302" src="https://github.com/user-attachments/assets/ed323851-7d75-42db-8b32-4830d32f840d" />

### Output Lihat Data Setelah Ditambahkan
Berikut hasil output apabila data ditambahkan. Data tersebut akan tersimpan meskipun Pengguna keluar dari program tersebut.
<img width="300" alt="Screenshot 2026-10-07 214302" src="https://github.com/user-attachments/assets/627b1707-c603-4564-9a47-4e26c2cb613d" />




