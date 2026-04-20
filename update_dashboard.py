import pandas as pd
import plotly.express as px
import os

# 1. Nama file Excel asli Anda
file_excel = 'rekap_tataruang.xlsx'

# 2. Cek apakah file ada
if os.path.exists(file_excel):
    # Membaca file excel
    df = pd.read_excel(file_excel)
    
    # 3. Buat Visualisasi (Sesuaikan nama kolom dengan di Excel Anda)
    # Contoh: Menghitung jumlah layanan per status
    # Ganti 'Status' dengan nama kolom status di Excel Anda
    fig = px.pie(df, names='Status', title='Distribusi Status Layanan Tata Ruang 2026',
                 hole=0.4, color_discrete_sequence=px.colors.sequential.RdBu)
    
    # 4. Simpan ke HTML
    fig.write_html('index.html')
    print("Dashboard dari data Excel berhasil diperbarui!")
else:
    print(f"File {file_excel} tidak ditemukan. Silakan upload file tersebut.")
