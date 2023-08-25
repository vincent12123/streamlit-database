import streamlit as st
import sqlite3

# Membuat atau terhubung ke database
conn = sqlite3.connect('nilai_siswa.db')
cursor = conn.cursor()

# Fungsi untuk menambahkan data siswa ke dalam tabel
def tambah_data(nama, mata_pelajaran, nilai):
    query = "INSERT INTO siswa (nama, mata_pelajaran, nilai) VALUES (?, ?, ?)"
    cursor.execute(query, (nama, mata_pelajaran, nilai))
    conn.commit()

# Antarmuka Streamlit
st.title('Tambah Data Nilai Siswa')
st.write('Masukkan informasi siswa baru:')

nama = st.text_input('Nama:')
mata_pelajaran = st.text_input('Mata Pelajaran:')
nilai = st.number_input('Nilai:', min_value=0, max_value=100)

if st.button('Tambah Data'):
    tambah_data(nama, mata_pelajaran, nilai)
    st.success('Data berhasil ditambahkan!')
    query = "SELECT * FROM siswa"
    cursor.execute(query)
    data_siswa = cursor.fetchall()
    st.table(data_siswa)
# Menutup koneksi
conn.close()
