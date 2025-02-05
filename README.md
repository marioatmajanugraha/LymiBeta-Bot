# LymiBeta-Bot

LymiBeta-Bot adalah sebuah bot untuk membantu pendaftaran email secara otomatis di situs Lymi Beta. Bot ini menggunakan Selenium untuk mengotomatisasi input email ke situs web.

## Fitur

- Otomatis membuat email acak berdasarkan username yang diberikan.
- Mengirimkan email yang dibuat ke situs Lymi Beta.
- Menyimpan daftar email yang berhasil didaftarkan ke dalam file `accounts.txt`.
- Menampilkan log status pendaftaran email (sukses/gagal).

## Prasyarat

Pastikan Anda telah menginstal semua dependensi yang diperlukan sebelum menjalankan bot ini. Anda dapat menginstalnya dengan menjalankan perintah berikut:

```bash
pip install selenium webdriver-manager colorama pyfiglet
```

**Penggunaan**
1.Clone repositori ini ke lokal Anda:
```bash
git clone https://github.com/marioatmajanugraha/LymiBeta-Bot.git
```
2.Pindah ke direktori proyek:
```bash
cd LymiBeta-Bot
```
3.Jalankan script main.py:
```bash
python main.py
```

Ikuti instruksi yang muncul di terminal untuk memasukkan username dan jumlah email yang ingin didaftarkan.

```
Masukan Username: exampleuser
Berapa email yang mau di submit? 2
[Success] - Register exampleuser12345@mailnesia.com
[Success] - Register exampleuser67890@mailnesia.com
Berhasil - 2 Email Terdaftar, Gagal - 0 Email
```

**Catatan**
Pastikan Anda memiliki koneksi internet yang stabil saat menjalankan bot ini.
Jangan lupa untuk memeriksa file accounts.txt untuk melihat daftar email yang berhasil didaftarkan.

**Kontribusi**
Jika Anda ingin berkontribusi pada proyek ini, silakan fork repositori ini dan buat pull request dengan perubahan Anda.

**Lisensi**
Proyek ini dilisensikan di bawah lisensi MIT. Lihat file LICENSE untuk informasi lebih lanjut.

**Kontak**
Jika Anda memiliki pertanyaan atau masukan, silakan hubungi saya di telegram @airdroplocked








