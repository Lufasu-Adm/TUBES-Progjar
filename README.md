# TUBES-Progjar

## Dibuat Oleh
## Nama 
Jordan Wijayanto

## Nim
1203220149


##

## SOAL
Buatlah sebuah permainan yang menggunakan soket dan protokol UDP. Permainannya cukup sederhana, dengan 1 server dapat melayani banyak klien (one-to-many). Setiap 10 detik, server akan mengirimkan kata warna acak dalam bahasa Inggris kepada semua klien yang terhubung. Setiap klien harus menerima kata yang berbeda (unik). Selanjutnya, klien memiliki waktu 5 detik untuk merespons dengan kata warna dalam bahasa Indonesia. Setelah itu, server akan memberikan nilai feedback 0 jika jawabannya salah dan 100 jika benar.

##


## SERVER-SIDE

[![Code-Server]()](https://github.com/Lufasu-Adm/TUBES-Progjar/blob/main/TuBes/server.py)

1. Membuat Server Socket: Pada sisi server, terlebih dahulu membuat objek socket untuk koneksi UDP.
2. Binding ke IP dan Port: Mengikat socket server ke alamat IP dan port tertentu (dalam contoh ini, 127.0.0.1:12345).
3. Menunggu Koneksi: Server akan terus-menerus dalam loop utama (while True) untuk menerima permintaan dari klien.
4. Menerima Permintaan: Jika ada data yang diterima dari klien, server akan mendekode data tersebut.
5. Menangani Permintaan "request_color": Jika data yang diterima adalah "request_color", server akan memilih secara acak sebuah warna dari daftar warna yang telah ditentukan.
6. Mengirim Warna ke Klien: Server kemudian akan mengirimkan warna yang dipilih ke klien yang meminta.
7. Menyimpan Koneksi Klien: Server melacak koneksi klien yang terhubung saat ini.
8. Menangani Keyboard Interrupt: Jika server menerima sinyal KeyboardInterrupt (biasanya ketika tombol Ctrl+C ditekan), server akan memberhentikan dirinya dan menutup socket.

Output

![Output Server](https://github.com/Lufasu-Adm/TUBES-Progjar/blob/main/TuBes/ASSETS/outputserver.jpg)

Penjelasam :

1. Membuat Socket Server:
Pertama-tama, kita membuat objek socket menggunakan socket.socket(socket.AF_INET, socket.SOCK_DGRAM). socket.AF_INET menunjukkan bahwa kita akan menggunakan alamat IPv4, dan socket.SOCK_DGRAM menunjukkan bahwa kita akan menggunakan protokol UDP untuk koneksi.

2. Binding Socket ke IP dan Port:
Selanjutnya, kita mengikat socket server ke alamat IP dan port tertentu menggunakan server_socket.bind((server_ip, server_port)). server_ip adalah alamat IP yang digunakan (dalam contoh ini adalah 127.0.0.1 atau localhost), dan server_port adalah nomor port (dalam contoh ini adalah 12345).

3. Menerima Koneksi dari Klien:
Server memasuki loop utama (while True) untuk terus-menerus menerima pesan dari klien. Ketika pesan diterima, server_socket.recvfrom(1024) digunakan untuk menerima data (dalam format byte) dari klien. 1024 adalah ukuran buffer maksimum untuk data yang diterima.

4. Dekode Pesan dari Klien:
Data yang diterima dari klien kemudian didekode dari byte menjadi string menggunakan .decode("utf-8"), sehingga kita mendapatkan pesan dalam bentuk teks.

5. Mengelola Koneksi Klien:
Server melacak klien yang terhubung dengan menyimpan alamat klien dalam connected_clients (menggunakan set() untuk menghindari duplikasi).

6. Mengirim Warna ke Klien:
Jika pesan dari klien adalah "request_color", maka server akan memilih warna acak dari daftar warna yang telah ditentukan menggunakan fungsi generate_random_color(). Warna tersebut dikirim kembali ke klien dengan menggunakan server_socket.sendto(color.encode("utf-8"), client_address).

7. Menangani Keyboard Interrupt:
Server dilengkapi dengan penanganan KeyboardInterrupt (except KeyboardInterrupt:) agar server dapat berhenti dengan aman jika pengguna menekan Ctrl+C.

8. Menutup Socket Server:
Setelah loop utama berhenti (misalnya, karena KeyboardInterrupt), socket server ditutup dengan server_socket.close().
Dengan demikian, kode server tersebut berfungsi sebagai server UDP sederhana yang menerima permintaan dari klien untuk mendapatkan warna acak, kemudian mengirimkan warna tersebut kembali ke klien yang meminta. Server terus-menerus berjalan dan siap menerima pesan dari klien selama dijalankan.

Dengan demikian, kode server tersebut berfungsi sebagai server UDP sederhana yang menerima permintaan dari klien untuk mendapatkan warna acak, kemudian mengirimkan warna tersebut kembali ke klien yang meminta. Server terus-menerus berjalan dan siap menerima pesan dari klien selama dijalankan.


##


## CLIENT-SIDE

[![Code-Client Mulai Dari Client 1]()](https://github.com/Lufasu-Adm/TUBES-Progjar/blob/main/TuBes/client_1.py)

1. Membuat Client Socket: Pada sisi klien, membuat objek socket untuk koneksi UDP.
2. Melakukan Loop Terus-Menerus: Klien akan terus berada dalam loop utama (while True), mengirim permintaan untuk warna dan menerima respon dari server.
3. Mengirim Permintaan: Klien mengirimkan pesan "request_color" ke server untuk meminta warna.
4. Menerima Warna: Klien menerima warna yang dikirimkan oleh server.
5. Menampilkan Warna: Warna yang diterima kemudian ditampilkan oleh klien.
6. Meminta Jawaban dari Pengguna: Klien meminta pengguna untuk menerjemahkan warna yang ditampilkan dalam bahasa Indonesia dalam batas waktu tertentu.
7. Memproses Jawaban: Klien membandingkan jawaban pengguna dengan terjemahan warna yang benar.
8. Memberikan Feedback: Klien memberikan nilai feedback berdasarkan kebenaran jawaban pengguna.
9. Menunggu Sebelum Permintaan Selanjutnya: Klien akan menunggu beberapa saat (dalam contoh ini 10 detik) sebelum meminta warna lagi.

Kedua kode ini (server dan client) menggunakan socket untuk komunikasi jaringan menggunakan protokol UDP (User Datagram Protocol), yang memungkinkan pertukaran pesan antara server dan klien secara asinkron dan ringan tanpa koneksi permanen.

Output Satu Server banyak Klien

![Output client](https://github.com/Lufasu-Adm/TUBES-Progjar/blob/main/TuBes/ASSETS/client.jpg)

![Output client](https://github.com/Lufasu-Adm/TUBES-Progjar/blob/main/TuBes/ASSETS/banyak%20client.jpg)

Penjelasan 

1. Membuat Socket Klien:
Pertama-tama, klien membuat objek socket menggunakan socket.socket(socket.AF_INET, socket.SOCK_DGRAM). Ini menunjukkan bahwa klien akan menggunakan alamat IPv4 dan protokol UDP untuk koneksi.

2. Mengirim Permintaan ke Server:
Klien mengirim pesan "request_color" ke server menggunakan client_socket.sendto("request_color".encode("utf-8"), (server_ip, server_port)). Pesan ini dikodekan ke dalam byte sebelum dikirim.

3. Menerima Respon dari Server:
Klien kemudian menunggu untuk menerima respon dari server menggunakan client_socket.recvfrom(1024). Data yang diterima (berupa warna yang dikirimkan oleh server) kemudian didekode dari byte menjadi string.

4. Menampilkan Warna yang Diterima:
Warna yang diterima dari server kemudian ditampilkan ke layar dengan menggunakan print(f"Warna yang diterima: {color}").

5. Meminta Input dari Pengguna:
Klien meminta input dari pengguna untuk menerjemahkan warna yang ditampilkan ke dalam bahasa Indonesia. Ini dilakukan dengan fungsi input_with_timeout(prompt, timeout), yang menampilkan pesan prompt kepada pengguna.

6. Menerjemahkan Warna:
Warna yang diterima kemudian diterjemahkan dari bahasa Inggris ke bahasa Indonesia menggunakan fungsi english_to_indonesian_color(color). Fungsi ini menggunakan kamus (dictionary) untuk mencocokkan warna dalam bahasa Inggris dengan terjemahannya dalam bahasa Indonesia.

7. Memberikan Feedback:
Klien membandingkan jawaban pengguna dengan terjemahan warna yang benar. Jika jawaban pengguna benar, klien mencetak "Jawaban benar! Nilai feedback: 100". Jika tidak, klien mencetak "Jawaban salah. Nilai feedback: 0".

8. Menunggu Sebelum Permintaan Selanjutnya:
Setelah memberikan feedback kepada pengguna, klien akan menunggu selama beberapa saat (dalam contoh ini 10 detik) sebelum mengirim permintaan warna lagi ke server.

9. Penanganan Keyboard Interrupt:
Klien juga dilengkapi dengan penanganan KeyboardInterrupt (except KeyboardInterrupt:) agar klien dapat berhenti dengan aman jika pengguna menekan Ctrl+C.

10. Menutup Socket Klien:
Setelah selesai, socket klien ditutup dengan client_socket.close().
Dengan demikian, klien tersebut berfungsi sebagai aplikasi yang terus-menerus mengirim permintaan ke server untuk mendapatkan warna, kemudian menerjemahkan warna tersebut dan memberikan feedback kepada pengguna berdasarkan jawaban yang diberikan. Proses ini terus berulang selama klien dijalankan dalam loop utama (while True).

Dengan demikian, klien tersebut berfungsi sebagai aplikasi yang terus-menerus mengirim permintaan ke server untuk mendapatkan warna, kemudian menerjemahkan warna tersebut dan memberikan feedback kepada pengguna berdasarkan jawaban yang diberikan. Proses ini terus berulang selama klien dijalankan dalam loop utama (while True).

[![Untuk Menjalankan Server dan Semua Client]()](https://github.com/Lufasu-Adm/TUBES-Progjar/blob/main/TuBes/Mulai.py)

## NOTE

- Jawaban yang benar = 100
- Jawaban yang salah 0
- Jika tidak ada input yang diberikan dalam batas waktu 5 detik, pesan timeout muncul yang meminta Anda untuk melanjutkan.
- Server mengirim warna baru kepada setiap klien setiap 10 detik, terlepas dari respons.
