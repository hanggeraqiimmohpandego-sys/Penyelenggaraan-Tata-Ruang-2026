import pandas as pd
import os

# 1. Nama file Excel Anda
file_excel = 'Rekap Layanan ITR_Laporan.xlsx'

if os.path.exists(file_excel):
    # 2. Membaca spesifik sheet REKAP_ITR
    # 'skiprows=5' digunakan untuk melompati baris kosong/filter di bagian atas
    # Jika tabel masih berantakan, coba ganti angka 5 menjadi 4 atau 6
    df = pd.read_excel(file_excel, sheet_name='REKAP_ITR', skiprows=5)
    
    # 3. Membersihkan data
    # Menghapus kolom yang isinya 'NaN' (kosong) semua
    df = df.dropna(how='all', axis=1)
    # Menghapus baris yang isinya kosong semua
    df = df.dropna(how='all', axis=0)
    
    # 4. Mengubah menjadi Tabel HTML yang interaktif
    html_table = df.to_html(classes='table table-hover table-bordered', index=False, na_rep='-')
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dashboard Layanan ITR 2026</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
        <style>
            body {{ padding: 30px; background-color: #f4f7f6; font-family: sans-serif; }}
            .header-box {{ background: #004d40; color: white; padding: 20px; border-radius: 10px; margin-bottom: 30px; }}
            .container-fluid {{ background: white; padding: 25px; border-radius: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }}
            .table-responsive {{ max-height: 700px; overflow-y: auto; }}
            th {{ background-color: #00796b !important; color: white; position: sticky; top: 0; }}
        </style>
    </head>
    <body>
        <div class="container-fluid">
            <div class="header-box">
                <h1>Data Penyelenggaraan Tata Ruang 2026</h1>
                <p>Sumber Sheet: <strong>REKAP_ITR</strong> | Update Otomatis</p>
            </div>
            <div class="table-responsive">
                {html_table}
            </div>
        </div>
    </body>
    </html>
    """
    
    # 5. Simpan jadi index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Dashboard REKAP_ITR Berhasil Diperbarui!")
else:
    print(f"Error: File {file_excel} tidak ditemukan.")
