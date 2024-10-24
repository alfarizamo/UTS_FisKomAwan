import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# judul
st.markdown("<h1 style='color: black;'>FISIKA KOMPUTASI AWAN</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: blue;'>Mohammad Khrisna Alfariza</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='color: blue;'>220322603846</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='color: black;'>Program Data/Warna Acak</h4>", unsafe_allow_html=True)

# button mengacak data
if st.button('Data'):
    # data/warna acak
    jumlah_titik = 200
    sudut = 2 * np.pi * np.random.rand(jumlah_titik)
    radius = np.sqrt(np.random.rand(jumlah_titik))
    x_posisi = radius * np.cos(sudut)
    y_posisi = radius * np.sin(sudut)
    ukuran_titik = 1000 * np.random.rand(jumlah_titik) 
    warna_titik = np.random.rand(jumlah_titik) 
    gambar, sumbu = plt.subplots(figsize=(10, 10))

    # plot data/warna acak
    scatter_plot = sumbu.scatter(x_posisi, y_posisi, s=ukuran_titik, c=warna_titik, alpha=0.6, cmap='viridis')
    for j in range(jumlah_titik):
        sumbu.plot([0, x_posisi[j]], [0, y_posisi[j]], linestyle='--', linewidth=0.5, color=plt.cm.viridis(warna_titik[j]), alpha=0.5)
    lingkaran = plt.Circle((0, 0), 1, color='red', fill=False)
    sumbu.add_artist(lingkaran)
    sumbu.set_xlim([-1.0, 1.0])
    sumbu.set_ylim([-1.0, 1.0])
    sumbu.set_aspect('equal', 'box')
    sumbu.grid(True, which='both', linewidth=0.3, color='grey')
    
    # tampilan grafik
    tick_values = [-1.0, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.0]
    sumbu.set_xticks(tick_values)
    sumbu.set_yticks(tick_values)
    sumbu.tick_params(axis='x', colors='red')
    sumbu.tick_params(axis='y', colors='red')

    # plot
    st.pyplot(gambar)
