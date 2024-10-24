import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Judul dengan warna biru
st.markdown("<h1 style='color: blue;'>FISIKA KOMPUTASI AWAN</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: blue;'>Mohammad Khrisna Alfariza</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='color: blue;'>220322603846</h3>", unsafe_allow_html=True)

# Tombol untuk menghasilkan data acak
if st.button('Generate Random Data'):
    # Membuat data acak untuk lingkaran
    jumlah_titik = 100
    sudut = 2 * np.pi * np.random.rand(jumlah_titik)
    radius = np.sqrt(np.random.rand(jumlah_titik))
    x_posisi = radius * np.cos(sudut)
    y_posisi = radius * np.sin(sudut)
    ukuran_titik = 1000 * np.random.rand(jumlah_titik)  # Ukuran acak
    warna_titik = np.random.rand(jumlah_titik)  # Warna acak

    # Membuat plot dengan ukuran diperbesar
    gambar, sumbu = plt.subplots(figsize=(8, 8))

    # Menampilkan titik-titik acak dengan ukuran dan warna yang berbeda
    scatter_plot = sumbu.scatter(x_posisi, y_posisi, s=ukuran_titik, c=warna_titik, alpha=0.6, cmap='viridis')

    # Menggambar garis dari pusat ke setiap titik (garis putus-putus tipis)
    for j in range(jumlah_titik):
        sumbu.plot([0, x_posisi[j]], [0, y_posisi[j]], linestyle='--', linewidth=0.5, color=plt.cm.viridis(warna_titik[j]), alpha=0.5)

    # Menambahkan lingkaran dengan garis merah
    lingkaran = plt.Circle((0, 0), 1, color='red', fill=False)
    sumbu.add_artist(lingkaran)

    # Mengatur batas tampilan
    sumbu.set_xlim([-1.0, 1.0])
    sumbu.set_ylim([-1.0, 1.0])
    sumbu.set_aspect('equal', 'box')

    # Grid dengan jarak lebih kecil (0.125)
    sumbu.grid(True, which='both', linewidth=0.5, color='grey')
    sumbu.xaxis.set_major_locator(plt.MultipleLocator(0.125))
    sumbu.yaxis.set_major_locator(plt.MultipleLocator(0.125))

    # Ubah warna angka pada garis kartesian menjadi merah
    sumbu.tick_params(axis='x', colors='red')
    sumbu.tick_params(axis='y', colors='red')

    # Menampilkan plot
    st.pyplot(gambar)
