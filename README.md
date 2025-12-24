# Dashboard Analisis Sentimen Komentar (LSTM)

## Deskripsi Proyek
Proyek ini membangun sistem **klasifikasi sentimen komentar** berbahasa Indonesia.  
Input sistem berupa teks komentar (kolom **`textDisplay`**) dan output berupa **Label sentimen** (misalnya **POSITIF / NEGATIF / NETRAL / OTHER**).

Website dibuat menggunakan **Streamlit** untuk mendemonstrasikan model pembelajaran mesin.  
Model yang dipakai pada website adalah **LSTM** dan sudah **disimpan** dalam file `lstm_label_komen.keras`, sehingga saat menjalankan dashboard **tidak perlu training ulang**.

---

## Isi Repository 
Repository ini berisi file inti berikut:
- `app.py` → Source code Streamlit Dashboard
- `lstm_label_komen.keras` → Model LSTM tersimpan (Keras/TensorFlow)
- `labels.json` → Urutan label kelas yang dipakai model
- `LABEL_KOMEN.csv` → Dataset (opsional: bisa diupload atau hanya tautan)

Struktur folder sederhana:
```text
.
├─ app.py
├─ labels.json
├─ lstm_label_komen.keras
└─ LABEL_KOMEN.csv   (opsional)
```

> Catatan: Pada implementasi lokal (laptop), **ketiga file** `app.py`, `labels.json`, dan `lstm_label_komen.keras` harus berada dalam **folder yang sama** (sesuai struktur di atas).

---

## Dataset
Dataset: `LABEL_KOMEN.csv`  
Kolom yang digunakan:
- `textDisplay` → fitur teks (input)
- `Label` → target kelas

Catatan:
- Dataset bersifat **imbalanced** (kelas NEGATIF dominan). Karena itu evaluasi juga memakai metrik **Macro F1-score** agar penilaian lebih adil antar kelas.

Jika dataset tidak diupload ke repo (ukuran/privasi), isi tautan di sini:
- Link dataset: **(isi link Google Drive / Kaggle / dsb)**

---

## Preprocessing (Ringkas)
Preprocessing yang digunakan saat training (ringkas):
1. **Normalisasi label** (menyeragamkan variasi penulisan label jika ada).
2. **Cleaning teks**, misalnya:
   - lowercase
   - menghapus URL / mention / hashtag
   - menghapus karakter non-alfanumerik
   - menghapus spasi berlebih

> Detail langkah preprocessing, kode lengkap, serta contoh output sebelum/sesudah preprocessing dapat dilihat pada notebook pelatihan (`.ipynb`) yang diupload ke repository.

---

## Model yang Digunakan 
Pada eksperimen di notebook, dilakukan pelatihan dan evaluasi **3 model**:
1. **LSTM (Base Neural Network)** → dipakai sebagai implementasi dashboard (model tersimpan `lstm_label_komen.keras`)
2. **IndoBERT (Pretrained Transformer)**
3. **DistilBERT (Pretrained Transformer)**

Pemilihan model terbaik dilakukan berdasarkan metrik evaluasi (terutama **MacroF1**) dan analisis **Confusion Matrix**.

---

## Hasil Evaluasi & Analisis Perbandingan
Komponen evaluasi yang wajib tersedia pada notebook:
- **Classification Report**
- **Confusion Matrix**
- **Grafik Loss dan Accuracy**

Metrik yang dipakai untuk perbandingan:
- **Accuracy**
- **Macro F1-score (MacroF1)** → rata-rata F1 tiap kelas (lebih adil untuk data imbalanced)

Ringkasan hasil akhir:
| Model | Accuracy | MacroF1 |
|------|----------|---------|
| LSTM (Base NN) | (0.465097) | (0.207198) |
| IndoBERT (Pretrained) | (0.275862) | (0.171360) |
| DistilBERT (Pretrained) | (0.080740) | (0.087006) |

**Kesimpulan:** Model terbaik berdasarkan **ACCURACY** dan **MACROF1** adalah **LSTM** oleh sebab itu dipilihlah algoritma **LSTM** sebagai algoritma penjalan DASHBOARD

---

## Cara Menjalankan Website Secara Lokal (VSCode)

### Prasyarat
- **Python 3.11.x** (disarankan, agar kompatibel dengan TensorFlow)
- `pip` aktif
- File `app.py`, `labels.json`, `lstm_label_komen.keras` berada dalam folder yang sama

### 1) Buka folder project
Contoh (Windows PowerShell):
```powershell
cd "C:\Users\...\sentimen-dashboard"
```

### 2) Buat virtual environment 
```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Jika muncul error PowerShell “running scripts is disabled”, jalankan:
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```
Lalu aktifkan venv lagi:
```powershell
.\.venv\Scripts\Activate.ps1
```

### 3) Install dependencies
Minimal:
```powershell
python -m pip install --upgrade pip
python -m pip install tensorflow streamlit numpy
```

### 4) Jalankan Streamlit
```powershell
python -m streamlit run app.py
```

Buka di browser:
- http://localhost:8501

---

## Menjalankan di Google Colab + ngrok (Opsional / Live Demo)
Website pernah didemokan melalui **Google Colab** dan diakses lewat **ngrok** (tunnel).

Catatan penting:
- ngrok membutuhkan akun terverifikasi & **authtoken**.
- Link ngrok bersifat **sementara** dan dapat berubah jika runtime restart.

### Link Live Demo 
- https://catchable-unenlightenedly-lennie.ngrok-free.dev/

---

## Author
Nama: **Ilham Wijaya Kusuma**  
NIM: **202210370311199**
