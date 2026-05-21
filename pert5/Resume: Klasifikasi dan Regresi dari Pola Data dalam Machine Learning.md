# Resume: Klasifikasi dan Regresi dari Pola Data dalam Machine Learning

> **Sumber:** Coursera, GeeksforGeeks, Medium, Google ML Crash Course, PMC (2024–2026)



## 📌 Pendahuluan

Klasifikasi dan regresi adalah dua teknik paling populer dalam **supervised machine learning**, masing-masing dirancang untuk jenis masalah yang berbeda bergantung pada sifat output yang ingin diprediksi dari pola data.

- **Klasifikasi** → memprediksi **label/kategori** (output diskrit)
- **Regresi** → memprediksi **nilai numerik kontinu** (output kontinu)

> Keduanya bekerja dengan cara mempelajari pola hubungan dari data berlabel, lalu menggeneralisasi pengetahuan tersebut ke data baru.



## 📊 Regresi *(Regression)*

### Definisi
Regresi adalah teknik supervised learning yang digunakan untuk **memodelkan hubungan antara variabel independen (prediktor) dan variabel dependen (target) yang bersifat kontinu**. Tujuannya adalah memprediksi nilai numerik berdasarkan pola dalam data input.

> 💡 **Contoh:** Memprediksi harga rumah berdasarkan luas, lokasi, dan jumlah kamar.

### Cara Kerja
Model regresi belajar memetakan fungsi:

```
f(x) → y
```

di mana fitur input `x` dipetakan ke output kontinu `y`. Model meminimalkan **error** antara nilai prediksi dan nilai aktual menggunakan **loss function**.

### Jenis-Jenis Regresi

| Tipe | Deskripsi |
|------|-----------|
| **Linear Regression** | Memodelkan hubungan linear antara input dan output dengan garis lurus |
| **Multiple Linear Regression** | Menggunakan beberapa variabel input untuk prediksi lebih akurat |
| **Polynomial Regression** | Memodelkan hubungan non-linear dengan memperkenalkan term polinomial |
| **Decision Tree Regression** | Memprediksi nilai kontinu dengan membagi data berdasarkan kondisi fitur |
| **Random Forest Regression** | Ensemble dari banyak decision tree untuk meningkatkan akurasi dan mengurangi variansi |
| **Support Vector Regression (SVR)** | Menggunakan optimasi margin dan kernel function untuk prediksi nilai kontinu |
| **Neural Network Regression** | Belajar pola kompleks menggunakan lapisan neuron yang saling terhubung |

### Loss Function dalam Regresi

| Metrik | Deskripsi |
|--------|-----------|
| **MSE** *(Mean Squared Error)* | Rata-rata kuadrat error; menghukum kesalahan besar lebih berat |
| **MAE** *(Mean Absolute Error)* | Rata-rata selisih absolut antara nilai aktual dan prediksi |
| **Huber Loss** | Kombinasi MSE dan MAE; lebih robust terhadap outlier |

### Aplikasi Regresi

- **Business Forecasting** — Estimasi penjualan, pendapatan, dan permintaan pelanggan
- **Healthcare Predictions** — Prediksi perkembangan penyakit dan skor risiko pasien
- **Market Trend Analysis** — Identifikasi pergerakan harga dan tren keuangan
- **Agriculture** — Estimasi hasil panen dan analisis nutrisi tanah
- **Energy Demand** — Prakiraan konsumsi listrik dan kebutuhan beban



## 🏷️ Klasifikasi *(Classification)*

### Definisi
Klasifikasi adalah teknik supervised learning yang digunakan untuk **mengkategorikan data ke dalam kelompok atau kelas yang telah ditentukan** berdasarkan karakteristik yang dipelajari dari data. Output model adalah label atau kategori yang bersifat diskrit.

> 💡 **Contoh:** Mendeteksi apakah email adalah spam atau bukan; mendiagnosis ada/tidaknya penyakit.

### Cara Kerja
Model klasifikasi mempelajari **decision boundary** yang memisahkan satu kelas dari kelas lainnya. Model menggunakan fungsi aktivasi untuk menghasilkan probabilitas:

- **Sigmoid** — Untuk binary classification; memetakan output antara 0 dan 1
- **Softmax** — Untuk multi-class classification; mengonversi skor menjadi probabilitas yang totalnya 1

Kelas dengan probabilitas tertinggi dipilih sebagai prediksi akhir.

### Tipe-Tipe Klasifikasi

| Tipe | Deskripsi | Contoh |
|------|-----------|--------|
| **Binary Classification** | Dua kelas output | Spam/Not Spam, Fraud/Not Fraud |
| **Multiclass Classification** | Lebih dari dua kelas tanpa overlap | Klasifikasi jenis anjing (Dalmatian, Collie, Poodle) |
| **Multilabel Classification** | Satu data bisa masuk ke beberapa kelas | Genre film (Action + Comedy sekaligus) |

### Algoritma Klasifikasi Utama

| Algoritma | Deskripsi |
|-----------|-----------|
| **Logistic Regression** | Model linear untuk binary & multi-class classification |
| **Decision Tree** | Membagi data ke cabang-cabang berdasarkan kondisi fitur |
| **Random Forest** | Ensemble decision tree untuk akurasi lebih tinggi |
| **Support Vector Machine (SVM)** | Mencari hyperplane terbaik untuk memisahkan kelas |
| **K-Nearest Neighbors (KNN)** | Klasifikasi berdasarkan "k" data point terdekat |
| **Neural Network** | Menangani pola kompleks dengan lapisan neuron dalam |
| **Naive Bayes** | Berbasis probabilitas dengan asumsi independensi antar fitur |

### Aplikasi Klasifikasi

- **Email Spam Detection** — Menyaring email spam/bukan spam
- **Medical Diagnosis** — Mendeteksi ada/tidaknya penyakit dari scan medis
- **Fraud Detection** — Mengidentifikasi transaksi mencurigakan
- **Sentiment Analysis** — Mengkategorikan ulasan sebagai positif/negatif/netral
- **Image Recognition** — Mengenali objek atau wajah dalam gambar
- **Customer Segmentation** — Mengelompokkan pelanggan berdasarkan perilaku

## 📏 Metrik Evaluasi

### Untuk Klasifikasi

| Metrik | Deskripsi |
|--------|-----------|
| **Accuracy** | Proporsi prediksi benar dari total prediksi; ideal untuk data seimbang |
| **Precision** | Proporsi prediksi positif yang benar-benar positif |
| **Recall (Sensitivity)** | Proporsi data positif aktual yang berhasil terdeteksi |
| **F1-Score** | Harmonic mean dari Precision dan Recall; baik untuk data tidak seimbang |
| **AUC-ROC** | Kemampuan model membedakan kelas positif dan negatif |

> ⚠️ **Catatan Penting:** Accuracy saja bisa menyesatkan pada dataset tidak seimbang. Misalnya, jika 99% data adalah "tidak fraud", model yang selalu prediksi "tidak fraud" akan punya accuracy 99% padahal tidak berguna. Gunakan Precision, Recall, dan F1-Score untuk gambaran yang lebih lengkap.

### Untuk Regresi

| Metrik | Deskripsi |
|--------|-----------|
| **MSE** *(Mean Squared Error)* | Rata-rata kuadrat perbedaan antara nilai aktual dan prediksi |
| **RMSE** *(Root MSE)* | Akar dari MSE; lebih mudah diinterpretasi karena satuan sama dengan data |
| **MAE** *(Mean Absolute Error)* | Rata-rata selisih absolut; tidak terlalu sensitif terhadap outlier |
| **R² (R-Squared)** | Proporsi variansi data yang dijelaskan model; semakin mendekati 1, semakin baik |


## 🆚 Perbandingan Klasifikasi vs Regresi

| Aspek | Klasifikasi | Regresi |
|-------|-------------|---------|
| **Output** | Label/Kategori diskrit | Nilai numerik kontinu |
| **Tujuan** | Memetakan data ke kelas | Memprediksi nilai numerik |
| **Contoh Output** | "Spam" / "Tidak Spam" | Harga: Rp 500.000.000 |
| **Loss Function** | Cross-Entropy, Hinge Loss | MSE, MAE, Huber Loss |
| **Metrik Evaluasi** | Accuracy, F1, AUC-ROC | MSE, RMSE, R² |
| **Decision Boundary** | Memisahkan kelas | Garis/kurva fitting data |
| **Algoritma Utama** | SVM, Logistic Reg., KNN | Linear Reg., SVR, RF Reg. |

## 🔄 Kapan Menggunakan Masing-Masing?

```
Output yang diinginkan berupa KATEGORI?
     ├── Ya  → Gunakan KLASIFIKASI
     │         (Binary jika 2 kelas, Multiclass jika >2 kelas)
     └── Tidak → Output berupa NILAI NUMERIK?
                  └── Ya → Gunakan REGRESI
```

**Pilih Klasifikasi jika:**
- Output adalah kategori atau label (ya/tidak, jenis, tipe)
- Ingin mendeteksi fraud, spam, atau penyakit
- Mengelompokkan gambar, teks, atau audio

**Pilih Regresi jika:**
- Output adalah angka yang bisa bervariasi di range kontinu
- Ingin memprediksi harga, suhu, atau pendapatan
- Memodelkan tren dan hubungan antar variabel numerik

## 📚 Referensi

1. Coursera Staff. (2026). *Classification vs. Regression in Machine Learning.* https://www.coursera.org/articles/classification-vs-regression-machine-learning
2. GeeksforGeeks. (2025). *Classification vs Regression in Machine Learning.* https://www.geeksforgeeks.org/machine-learning/ml-classification-vs-regression/
3. Salunke, M. (2024). *Regression vs Classification in Machine Learning.* Medium.
4. Google Developers. (2026). *Classification: Accuracy, Recall, Precision, and Related Metrics.* https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall
5. Gulhane, A. (2025). *Evaluation/Performance Metrics — Regression vs Classification Model.* Medium.
6. PMC / NCBI. (2024). *Evaluation Metrics and Statistical Tests for Machine Learning.*

---

*Dibuat untuk keperluan akademik — Teknik Informatika, Universitas Esa Unggul Bekasi*
