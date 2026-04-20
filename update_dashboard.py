import pandas as pd
import plotly.express as px
import datetime
import random
import os

# 1. Simulasi pengambilan data baru (Progres harian)
hari_ini = datetime.datetime.now().strftime("%Y-%m-%d")
status_pilihan = ['Disetujui', 'Proses', 'Ditolak']
data_baru = pd.DataFrame({
    'tanggal': [hari_ini],
    'status': [random.choice(status_pilihan)],
    'jumlah': [random.randint(1, 20)]
})

# 2. Update file CSV
file_path = 'data_ruang.csv'
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    df = pd.concat([df, data_baru], ignore_index=True)
else:
    df = data_baru

df.to_csv(file_path, index=False)

# 3. Buat Visualisasi untuk Dashboard
fig = px.bar(df, x='tanggal', y='jumlah', color='status', 
             title='Progres Penyelenggaraan Tata Ruang 2026',
             barmode='group')

# Simpan sebagai HTML agar bisa dilihat di browser
fig.write_html('index.html')
print("Dashboard berhasil diperbarui!")
