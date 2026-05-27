# Streamlit-Netflix-Dashboard
Dashboard web interaktif berbasis Streamlit &amp; Plotly untuk visualisasi dan analisis data film serta TV Show di Netflix. Menyajikan tren rilis tahunan, distribusi tipe konten, filter negara, hingga pencarian data mentah secara dinamis dan real-time dari data netflix_titles.csv. 

# 🎬 Netflix Data Analytics Dashboard

[![Streamlit App](https://static.streamlit.io/badge_svg.svg)](https://streamlit.io)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

Sebuah aplikasi **Dashboard Interaktif** berbasis web yang dibangun menggunakan **Streamlit** dan **Plotly Express** untuk mengeksplorasi, menganalisis, dan memvisualisasikan data film serta acara TV yang tersedia di Netflix (`netflix_titles.csv`). Dashboard ini dirancang untuk memberikan wawasan mendalam mengenai tren konten, distribusi tipe media, negara produsen terbesar, hingga pola penambahan konten dari tahun ke tahun secara dinamis dan real-time.

---

## ✨ Fitur Utama

- **Panel Filter Sticky (Sidebar):** Memudahkan pengguna menyaring konten berdasarkan *Tipe Konten* (Movie/TV Show) dan *Negara Asal* secara instan tanpa mengganggu tata letak visual utama.
- **Ringkasan Metrik Otomatis (KPIs):** Menampilkan total judul, jumlah film, dan jumlah TV Show yang berubah secara dinamis mengikuti filter yang dipilih.
- **Visualisasi Interaktif (Plotly):**
  - **Pie Chart:** Analisis proporsi persentase antara Movies vs TV Shows.
  - **Line Chart:** Tren perilisan konten dari tahun ke tahun untuk melihat pertumbuhan industri hiburan secara historis.
- **Eksplorasi Data Mentah (Interactive Data Table):** Menampilkan sampel data tabular yang dapat diurutkan (*sortable*) dan dicari langsung melalui antarmuka dashboard.

---

## Pratinjau Antarmuka

### Mode Gelap (Dark Mode - Default)
<p align="center">
  <img src="Images/Mode gelap.png" alt="Dashboard Dark Mode" width="100%" style="border-radius: 8px; border: 1px solid #334155;">
  <br>
  <em>Gambar 2.1: Tampilan Utama Dashboard Pusat Kendali dalam Skema Mode Gelap.</em>
</p>

### Mode Terang (Light Mode)
<p align="center">
  <img src="Images/Mode terang.png" alt="Dashboard Light Mode" width="100%" style="border-radius: 8px; border: 1px solid #cbd5e1;">
  <br>
  <em>Gambar 2.2: Transisi Skema Warna ke Mode Terang untuk Kebutuhan Presentasi Formal.</em>
</p>

---

## 📊 Detail Dataset

Dataset yang digunakan dalam proyek ini adalah data publik berisi informasi konten Netflix hingga tahun 2021 dengan total **8.807 baris data**. Atribut data yang dianalisis meliputi:
- `show_id`: Id unik untuk setiap konten.
- `type`: Klasifikasi konten (*Movie* atau *TV Show*).
- `title`: Judul film atau acara TV.
- `director`: Sutradara konten.
- `country`: Negara tempat konten diproduksi (Top 5: *United States, India, United Kingdom, Japan, South Korea*).
- `release_year`: Tahun rilis asli dari konten (Rentang data: 1925 - 2021).
- `rating`: Target penonton atau klasifikasi usia (*TV-MA, PG-13, R, dll.*).
- `listed_in`: Kategori atau genre konten.

---
