import streamlit as st
import sqlite3

# Membuat atau terhubung ke database
conn = sqlite3.connect('nilai_siswa.db')

# Membuat objek cursor
cursor = conn.cursor()

# Query untuk mengambil data siswa
query = "SELECT * FROM siswa"
cursor.execute(query)
data_siswa = cursor.fetchall()

# Menampilkan data siswa menggunakan Streamlit
st.title('Data Nilai Siswa')
st.write('Berikut adalah data nilai siswa yang telah tersimpan dalam database:')

# Membuat tabel untuk menampilkan data
st.table(data_siswa)

# Menutup koneksi
conn.close()
