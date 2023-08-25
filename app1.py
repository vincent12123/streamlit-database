import streamlit as st
import sqlite3
import pandas as pd

# Membuat atau terhubung ke database
conn = sqlite3.connect('nilai_siswa.db')

# Membuat objek cursor
cursor = conn.cursor()

# Query untuk mengambil data siswa
query = "SELECT * FROM siswa"
cursor.execute(query)
data_siswa = cursor.fetchall()

# Menutup koneksi
conn.close()

# Membuat DataFrame dari data siswa
df = pd.DataFrame(data_siswa, columns=['id', 'nama', 'mata_pelajaran', 'nilai'])

# Menambahkan kolom indeks baris sebagai nomor
df.insert(0, 'No', range(1, 1 + len(df)))

# Menampilkan data siswa menggunakan Streamlit
st.title('Data Nilai Siswa')
st.write('Berikut adalah data nilai siswa yang telah tersimpan dalam database:')

# Membuat tabel untuk menampilkan data (tanpa indeks)
st.table(df, index=False)
