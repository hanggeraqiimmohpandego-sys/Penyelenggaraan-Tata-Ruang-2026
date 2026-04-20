import pandas as pd
import plotly.express as px
import os

# 1. Alamat file data
file_path = 'data_ruang.csv'

# 2. Cek apakah file data ada, jika tidak buat data cadangan agar tidak error
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    df = pd.DataFrame({
        'tanggal': ['2026-04-20'],
        'status': ['Proses'],
        'jumlah': [10]
    })

# 3. Buat grafik batang sederhana
fig = px.bar(df, x='tanggal', y='jumlah', color='status', 
             title='Monitoring Penyelenggaraan Tata Ruang 2026')

# 4. Simpan hasilnya menjadi index.html (ini yang akan tampil di link)
fig.write_html('index.html')
print("Dashboard Berhasil Dibuat!")
