import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# Jumlah titik data
num_points = 1000

# Generate data acak dalam rentang -1 hingga 1
x = np.random.uniform(-1, 1, num_points)
y = np.random.uniform(-1, 1, num_points)

# Ukuran titik acak
sizes = np.random.randint(10, 100, num_points)

# Warna titik acak
colors = np.random.rand(num_points, 3)  # RGB

# Membuat plot
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5)

# Batas sumbu
plt.xlim(-1.1, 1.1)
plt.ylim(-1.1, 1.1)

# Judul dan label sumbu
plt.title('Data Acak')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')

# Tampilkan plot
plt.show()

st.pyplot(plt)
