# Searching & Sorting Algorithms in Python

Repository ini berisi implementasi dan penjelasan dasar algoritma **Searching** dan **Sorting** menggunakan bahasa Python sebagai materi Algoritma dan Struktur Data.

# Tujuan Pembelajaran
- Memahami konsep dasar searching dan sorting
- Mengimplementasikan algoritma dalam Python
- Melatih logika pemrograman
- Memahami perbedaan setiap jenis algoritma

# A). SEARCHING ALGORITHMS
# Pengertian Searching
Searching adalah proses untuk mencari data tertentu di dalam sekumpulan data.

# 1. Linear Search
Linear Search adalah metode pencarian data dengan cara memeriksa **setiap elemen satu per satu** dari awal hingga akhir.

# Karakteristik
- Tidak memerlukan data terurut
- Sederhana dan mudah dipahami
- Kurang efisien untuk data besar

# Contoh :
data = [12, 7, 25, 9, 15]
target = 9

# 2. Binary Search
Binary Search adalah metode pencarian dengan cara membagi data menjadi dua bagian secara berulang.

# Syarat
Data harus sudah dalam keadaan terurut.

# Karakteristik
- Lebih cepat dibanding linear search
- Tidak bisa digunakan pada data acak

# Contoh :
data = [10, 20, 30, 40, 50]
target = 40

# 3 Naive String Matching
Algoritma untuk mencari pola (pattern) dalam sebuah teks dengan membandingkan karakter satu per satu.

# Karakteristik
- Sederhana
- Kurang efisien untuk teks panjang

# Contoh :
text = "DATA STRUKTUR DATA"
pattern = "DATA"

# 4. KMP (Knuth-Morris-Pratt)
KMP adalah algoritma pencarian string yang lebih efisien dengan menggunakan tabel **LPS (Longest Prefix Suffix)**.

# Karakteristik
- Tidak mengulang pengecekan karakter yang sudah cocok
- Lebih efisien dibanding naive search

# Contoh :
pattern = "ABABAC"
lps = [0, 0, 1, 2, 3, 0]


# B SORTING ALGORITHMS
Sorting adalah proses mengurutkan data dari nilai kecil ke besar atau sebaliknya.

# 1. Bubble Sort
Bubble Sort bekerja dengan cara menukar elemen yang bersebelahan jika urutannya salah.
# Karakteristik
- Sederhana
- Lambat untuk data besar

# Contoh :
data = [5, 3, 8, 1]

# 2. Selection Sort
Selection Sort mencari nilai terkecil lalu menukarnya ke posisi awal secara berulang.
# Karakteristik
- Jumlah swap sedikit
- Kurang efisien untuk data besar

# 3. Insertion Sort
Insertion Sort mengurutkan data dengan cara menyisipkan elemen ke posisi yang tepat.
# Karakteristik
- Efektif untuk data kecil
- Mirip seperti menyusun kartu

# 4. Merge Sort
Merge Sort membagi data menjadi bagian kecil, mengurutkannya, lalu menggabungkannya kembali.
# Karakteristik
- Stabil
- Cepat untuk data besar
- Menggunakan memori tambahan
# Contoh :
data = [8, 4, 2, 6]

# 5. Quick Sort
Quick Sort menggunakan pivot untuk membagi data menjadi bagian lebih kecil, sama, dan lebih besar.
# Karakteristik
- Sangat cepat pada kasus umum
- Performa tergantung pivot

# Contoh :
data = [10, 7, 8, 9]


# KESIMPULAN

- Searching digunakan untuk mencari data dalam kumpulan data
- Sorting digunakan untuk mengurutkan data agar lebih terstruktur



#  AUTHOR

Nadila Juniarti
