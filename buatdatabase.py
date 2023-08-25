import sqlite3

# Membuat atau terhubung ke database
conn = sqlite3.connect('nilai_siswa.db')

# Membuat objek cursor
cursor = conn.cursor()

# Membuat tabel 'siswa' dengan kolom-kolom yang sesuai
cursor.execute('''
    CREATE TABLE IF NOT EXISTS siswa (
        id INTEGER PRIMARY KEY,
        nama TEXT,
        mata_pelajaran TEXT,
        nilai INTEGER
    )
''')

# Menambahkan data ke dalam tabel
data_siswa = [
    ('John Doe', 'Matematika', 85),
    ('Jane Smith', 'Bahasa Inggris', 92),
    ('Alice Johnson', 'Fisika', 78)
]

for data in data_siswa:
    cursor.execute('INSERT INTO siswa (nama, mata_pelajaran, nilai) VALUES (?, ?, ?)', data)

# Commit perubahan dan tutup koneksi
conn.commit()
conn.close()

print("Database nilai siswa telah berhasil dibuat dan diisi.")
