import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Judul
st.title("FISIKA KOMPUTASI AWAN")
st.header("NAMA")

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

    # Plot
    fig, ax = plt.subplots()
    ax.scatter(x, y, s=sizes, c=colors, alpha=0.6, cmap='viridis')

    # Atur tampilan lingkaran dengan radius 1
    circle = plt.Circle((0, 0), 1, color='black', fill=False)
    ax.add_artist(circle)

    ax.set_xlim([-1.2, 1.2])
    ax.set_ylim([-1.2, 1.2])
    ax.set_aspect('equal', 'box')

    st.pyplot(fig)
