import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Judul
st.title("FISIKA KOMPUTASI AWAN")
st.header("RIZKY SETYAWAN")
st.header("220322601527")

# Tombol untuk menghasilkan data acak
if st.button('Data'):
    # Buat data acak untuk plot lingkaran
    num_points = 100
    theta = 2 * np.pi * np.random.rand(num_points)
    r = np.sqrt(np.random.rand(num_points))

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    sizes = 1000 * np.random.rand(num_points)  # Ukuran lingkaran acak
    colors = np.random.rand(num_points)  # Warna acak

    # Perlebar plot dengan ukuran lebih besar
    fig, ax = plt.subplots(figsize=(8, 8))  # Tambah figsize untuk memperlebar plot

    # Plot lingkaran acak dengan warna dan ukuran yang berbeda
    scatter = ax.scatter(x, y, s=sizes, c=colors, alpha=0.6, cmap='viridis')

    # Tambahkan garis dari titik pusat (0, 0) ke setiap data acak
    for i in range(num_points):
        ax.plot([0, x[i]], [0, y[i]], color=plt.cm.viridis(colors[i]), alpha=0.5)

    # Atur tampilan lingkaran dengan radius 1
    circle = plt.Circle((0, 0), 1, color='black', fill=False)
    ax.add_artist(circle)

    # Atur batas tampilan agar lebih luas dan lingkaran terlihat jelas
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_aspect('equal', 'box')

    # Tambahkan grid untuk mempermudah penglihatan
    ax.grid(True)

    # Tampilkan plot
    st.pyplot(fig)
