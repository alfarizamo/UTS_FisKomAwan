import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("FISIKA KOMPUTASI AWAN")
st.header("RIZKY SETYAWAN")
st.header("220322601527")

# tombol data untuk mengacak data
if st.button('Data'):
    num_points = 100
    theta = 2 * np.pi * np.random.rand(num_points)
    r = np.sqrt(np.random.rand(num_points))
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    sizes = 1000 * np.random.rand(num_points)
    colors = np.random.rand(num_points)

    fig, ax = plt.subplots(figsize=(8, 8))

    # data/warna acak
    scatter = ax.scatter(x, y, s=sizes, c=colors, alpha=0.6, cmap='viridis')

    # garis
    for i in range(num_points):
        ax.plot([0, x[i]], [0, y[i]], color=plt.cm.viridis(colors[i]), alpha=0.5)

    # lingkaran
    circle = plt.Circle((0, 0), 1, color='red', fill=False)
    ax.add_artist(circle)
    ax.set_xlim([-1.0, 1.0])
    ax.set_ylim([-1.0, 1.0])
    ax.set_aspect('equal', 'box')

    # grid
    ax.grid(True)

    # menampilkan plot
    st.pyplot(fig)
