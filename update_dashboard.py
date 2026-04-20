import pandas as pd
import plotly.express as px
import os

# 1. Nama file sesuai data asli Anda
file_excel = 'Rekap Layanan ITR_Laporan.xlsx'

if os.path.exists(file_excel):
    # Membaca data dari Excel
    df = pd.read_excel(file_excel)
    
    # Membersihkan nama kolom (menghapus spasi di awal/akhir)
    df.columns = df.columns.str.strip()

    # 2. Membuat Grafik (Asumsi kolom 'Status' atau 'Keterangan' ada di file Anda)
    # Jika nama kolomnya berbeda, silakan ganti 'Status' di bawah ini
    kolom_status = 'Status' if 'Status' in df.columns else df.columns[0]
    
    fig = px.pie(df, names=kolom_status, 
                 title=f'Progres Layanan ITR 2026 - Data: {file_excel}',
                 hole=0.4)

    # 3. Simpan ke HTML untuk dashboard
    fig.write_html('index.html')
    print("Dashboard dari data Excel asli berhasil dibuat!")
else:
    print(f"Error: File {file_excel} tidak ditemukan di repositori.")
