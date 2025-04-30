# Data Science Dicoding Proyek: HR Attrition Analysis — PT. Jaya Jaya Maju

Proyek ini merupakan bagian dari submission kelas Belajar Penerapan Data Science di Dicoding. 
Segala kesamaan data dan nama merupakan bentuk ketidaksengajaan. Proyek ini bertujuan membantu PT Jaya Jaya Maju dalam mengidentifikasi faktor apa saka yang mempengaruhi tingginya angka resign karyawannya, serta memberikan rekomendasi yang harus dilakukan selanjutnya.

---

## Summary

- **Dataset:** HR employee data (terlampir, dataset fiktif, berjumlah 1.058 data)
- **Problem:** Tingginya angka resign karyawan (>10%)
- **Goal:** Mengidentifikasi faktor utama resign dan memprediksi karyawan yang berisiko resign
- **Model:** Random Forest Classifier x SMOTE
- **Akurasi:** 84%
- **Faktor Utama (Berdasarkan feature importance):** Stock Option Level

---

## Grafik Dashboard

Visual dashboard dapat diakses melalui link [Looker Studio](https://lookerstudio.google.com/reporting/7dd00bc8-5e16-42ac-9c06-4b81758f9a90)

---

## Rekomendasi Action Items

1. **Berikan kepemilikan saham lebih jauh lagi untuk karyawan** :terbukti dari chart dan feature importance, stock option ini memberikan pengaruh signifikan terhadap keputusan pegawai untuk stay atau resign. Karyawan merasa lebih "dipercaya" dan dihargai jika diberikan saham

2. **Audit gaji karyawan**: Masalah klasik, karyawan yang memiliki gaji lebih rendah akan memilih resign. Sebagai HR, harus bisa memastikan apakah gaji (rewards) yang diterima sudah sesuai dengan usaha dan perjuangan pekerjaannya. Jangan sampai karyawan merasa kompetitor malah bisa lebih menghargai usaha kerasnya.

