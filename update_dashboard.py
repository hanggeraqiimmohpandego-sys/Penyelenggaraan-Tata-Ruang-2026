import pandas as pd
import os

# 1. Nama file sesuai data Anda
file_excel = 'Rekap Layanan ITR_Laporan.xlsx'

if os.path.exists(file_excel):
    # Membaca data dari Excel
    df = pd.read_excel(file_excel)
    
    # 2. Mengubah DataFrame menjadi Tabel HTML yang rapi
    # Kita tambahkan style CSS agar tampilannya profesional (seperti tabel dinas)
    html_table = df.to_html(classes='table table-striped', index=False)
    
    # 3. Membuat struktur halaman HTML lengkap
    html_content = f"""
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <title>Data Rekap Layanan ITR 2026</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
        <style>
            body {{ padding: 20px; background-color: #f8f9fa; }}
            .container {{ background: white; padding: 20px; border-radius: 10px; shadow: 0 0 10px rgba(0,0,0,0.1); }}
            h2 {{ color: #0d6efd; margin-bottom: 20px; }}
            .table-responsive {{ overflow-x: auto; }}
        </style>
    </head>
    <body>
        <div class="container-fluid">
            <h2>Data Rekap Layanan ITR - Laporan 2026</h2>
            <div class="table-responsive">
                {html_table}
            </div>
        </div>
    </body>
    </html>
    """
    
    # 4. Simpan menjadi index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Tabel data berhasil dibuat!")
else:
    print(f"Error: File {file_excel} tidak ditemukan.")
